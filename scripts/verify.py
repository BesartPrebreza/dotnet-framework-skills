"""Verify catalog coverage, references and project-local installation."""
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import tomllib

from build_catalog import render

ROOT = Path(__file__).resolve().parents[1]

def main():
    matrix = json.loads((ROOT / 'verification/matrix.json').read_text())
    expected = {row['skill'] for row in matrix}
    assert len(matrix) == len(expected) == 50
    assert len({row['spring_skill'] for row in matrix if row['spring_skill']}) == 44
    codex = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
    claude = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    for tfm in ('net48', 'net481'):
        tree = ROOT / 'skills' / tfm
        assert {p.name for p in tree.iterdir()} == expected
        for name in expected:
            folder = tree / name
            skill = (folder / 'SKILL.md').read_text(encoding='utf-8')
            assert re.match(rf'^---\nname: {name}\ndescription: Use when [^\n]+\n---\n', skill)
            assert (folder / 'examples/pattern.md').is_file()
            meta = json.loads((folder / 'agents/openai.yaml').read_text())
            assert '$' + name in meta['interface']['default_prompt']
        plugin = f'dotnet-framework-{tfm}-skills'
        claude_entry = next(entry for entry in claude['plugins'] if entry['name'] == plugin)
        assert (ROOT / claude_entry['skills'][0]).resolve() == tree
        codex_entry = next(entry for entry in codex['plugins'] if entry['name'] == plugin)
        path = ROOT / codex_entry['source']['path']
        meta = json.loads((path / '.codex-plugin/plugin.json').read_text())
        assert meta['name'] == plugin
        linked = path / meta['skills']
        assert linked.resolve() == tree or linked.read_text().strip() == '../../skills/' + tfm
        for client in ('claude', 'codex'):
            with tempfile.TemporaryDirectory() as directory:
                project = Path(directory)
                command = [sys.executable, str(ROOT / 'scripts/install.py'), '--client', client, '--target', tfm, '--project', directory, '--all', '--specialists']
                subprocess.run(command + ['--dry-run'], capture_output=True, check=True)
                assert not list(project.iterdir())
                subprocess.run(command, capture_output=True, check=True)
                installed = project / ('.claude' if client == 'claude' else '.agents') / 'skills'
                assert {p.name for p in installed.iterdir()} == expected
                assert subprocess.run(command, capture_output=True).returncode != 0
    for agent in (ROOT / 'specialists/codex').glob('*.toml'):
        assert tomllib.loads(agent.read_text())['name'] == agent.stem
    assert (ROOT / 'website/index.html').read_text(encoding='utf-8') == render()
    print('Verified 100 skill folders, package manifests, four install configurations and generated catalog.')

if __name__ == '__main__':
    main()
