"""Install a target-specific catalog into an existing project."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--client', choices=['claude', 'codex'], required=True)
    parser.add_argument('--target', choices=['net48', 'net481'], required=True)
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--specialists', action='store_true')
    parser.add_argument('skills', nargs='*')
    args = parser.parse_args()
    if not args.project.is_dir():
        parser.error('Project directory must exist.')
    if args.all == bool(args.skills):
        parser.error('Select --all or provide skill names.')
    sources = {p.name: p for p in (ROOT / 'skills' / args.target).iterdir() if (p / 'SKILL.md').is_file()}
    selected = sorted(sources) if args.all else list(dict.fromkeys(args.skills))
    unknown = set(selected) - sources.keys()
    if unknown:
        parser.error('Unknown skills: ' + ', '.join(sorted(unknown)))
    destination = args.project / ('.claude' if args.client == 'claude' else '.agents')
    files = [(sources[name], destination / 'skills' / name) for name in selected]
    if args.specialists:
        codex_agents = args.project / '.codex'
        agent_dir = destination / 'agents' if args.client == 'claude' else codex_agents / 'agents'
        files.extend((p, agent_dir / p.name) for p in sorted((ROOT / 'specialists' / args.client).iterdir()))
    for _, target in files:
        for path in (target, *target.parents):
            if path == args.project or path == args.project.resolve():
                break
            if path.is_symlink() or (path == target and path.exists()):
                parser.error(f'Existing path: {path}')
    for source, target in files:
        print(target)
        if args.dry_run:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            with source.open('rb') as origin, target.open('xb') as output:
                shutil.copyfileobj(origin, output)

if __name__ == '__main__':
    main()
