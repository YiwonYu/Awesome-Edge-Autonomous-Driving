"""Render chronological index and section tables from catalog.json."""
import json,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
rows=json.loads((root/'catalog.json').read_text())
rows.sort(key=lambda r:(-r['year'],r['title'].casefold()))
readme=root/'README.md'
intro=readme.read_text().split('## Contents')[0].split('**Ordering:**')[0]
intro+='**Ordering:** Newest publication year first, both in the chronological index and within each section. Same-year entries are alphabetical. Preprint and issue-year differences are recorded in the evidence notes.\n\n'
groups=['Priority papers','Specialist and additional papers','Recent preprints','Perception and supporting systems','Simulation and offboard-control references','Open-source projects','Surveys','Foundations and legacy platforms']
out=intro+'## Contents\n\n- [Chronological index](#chronological-index)\n'+''.join(f'- [{g}](#{g.lower().replace(" ","-")})\n' for g in groups)
out+='\n## Chronological index\n\n| Year | Paper / Project | Category |\n|---|---|---|\n'
for r in rows:out+=f"| {r['year']} | [{r['title']}]({r['paper']}) | {r['group']} |\n"
for g in groups:
 out+=f'\n## {g}\n\n| Year | Paper / Project | Device | Model / Method | Task | Venue | Code / GitHub | Real / Simulation |\n|---|---|---|---|---|---|---|---|\n'
 for r in rows:
  if r['group']!=g:continue
  code=f"[Resource]({r['code']})" if r['code'].startswith('http') else r['code']
  out+=f"| {r['year']} | [{r['title']}]({r['paper']}) ([{r['id']}](VERIFICATION.md#{r['id'].lower()})) | {r['device']} | {r['method']} | {r['task']} | {r['venue']} | {code} | {r['validation']} |\n"
out+='\n## Reuse\n\nOriginal curation is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Papers, code and data retain their own licenses. This repository does not redistribute paper PDFs.\n'
readme.write_text(out)
