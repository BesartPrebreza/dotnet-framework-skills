"""Generate a self-contained HTML catalog from repository files."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def render():
    matrix = json.loads((ROOT / 'verification/matrix.json').read_text())
    cards = []
    for row in sorted(matrix, key=lambda entry: (entry['category'], entry['skill'])):
        skill = row['skill']
        body = (ROOT / f'skills/net48/{skill}/SKILL.md').read_text().split('---', 2)[-1]
        example = (ROOT / f'skills/net48/{skill}/examples/pattern.md').read_text()
        links = ' · '.join(f'<a href="../skills/{tfm}/{skill}/SKILL.md">{tfm}</a>' for tfm in row['targets'])
        cards.append(f'<article><small>{html.escape(row["category"])}</small><h2>{html.escape(skill)}</h2>{links}<details><summary>Preview</summary><pre>{html.escape(body.strip() + chr(10)*2 + example)}</pre></details></article>')
    return '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>.NET Framework Skills</title>
<style>
* { box-sizing: border-box; } body { font: 16px system-ui,sans-serif; background:#f4f4f8; color:#201736; margin:0; }
main { width:min(1100px,94vw); margin:3rem auto; } h1 { font-size:clamp(2rem,5vw,4rem); margin:0; }
label { display:block; margin:1.5rem 0 .5rem; } input { width:100%; padding:.8rem; font:inherit; border:1px solid #6f6680; border-radius:.5rem; }
#catalog { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr)); gap:1rem; }
article { background:white; border:1px solid #d8d0e2; border-radius:.7rem; padding:1rem; overflow-wrap:anywhere; }
small,a { color:#5634a0; } h2 { font-size:1.1rem; } details { margin-top:.8rem; } summary { cursor:pointer; } pre { white-space:pre-wrap; }
</style>
<main><h1>.NET Framework Skills</h1><p>Browse skills for .NET Framework 4.8 and 4.8.1.</p>
<label for="filter">Search by skill or category</label><input type="search" id="filter"><p id="count" aria-live="polite"></p>
<section id="catalog" aria-label="Skill catalog">''' + '\n'.join(cards) + '''</section></main>
<script>
const input = document.querySelector('#filter');
const cards = [...document.querySelectorAll('article')];
function filter() {
  const term = input.value.trim().toLowerCase();
  for (const card of cards) card.hidden = !card.textContent.toLowerCase().includes(term);
  document.querySelector('#count').textContent = cards.filter(card => !card.hidden).length + ' skills';
}
input.addEventListener('input', filter);
filter();
</script></html>
'''

if __name__ == '__main__':
    (ROOT / 'website/index.html').write_text(render(), encoding='utf-8')
