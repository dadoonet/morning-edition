#!/usr/bin/env python3
"""Regenerate index.html: an archive listing of every magazines/YYYY-MM-DD.html (newest first); French is the default, with an EN link per issue."""
import pathlib, datetime
root = pathlib.Path(__file__).resolve().parent.parent
files = sorted((root / "magazines").glob("????-??-??.html"), reverse=True)
items = []
for f in files:
    d = datetime.date.fromisoformat(f.stem)
    en = f.with_name(f.stem + "-en.html")
    entxt = f'<a class="en" href="magazines/{en.name}">EN</a>' if en.exists() else ""
    jours = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    mois = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    items.append(f'<li><a href="magazines/{f.name}"><span>{jours[d.weekday()]}</span>{d.day} {mois[d.month-1]} {d.year}</a>{entxt}</li>')
html = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Morning Edition — archive</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,900&family=Inter:wght@700&display=swap" rel="stylesheet">
<style>html{{font-size:20px}}body{{margin:0;background:#14110f;color:#f4ecdc;font-family:Inter,sans-serif;padding:6vw}}
h1{{font-family:Fraunces,Georgia,serif;font-weight:900;font-size:clamp(4rem,14vw,12rem);line-height:.85;margin:0 0 3rem;letter-spacing:-.03em}}
ul{{list-style:none;padding:0;margin:0;max-width:900px}}li{{border-top:3px solid #f4ecdc;display:flex;align-items:center;gap:1rem}}li>a:first-child{{flex:1}}a.en{{flex:none;font-family:Inter,sans-serif;font-size:1rem;letter-spacing:.1em;border:3px solid #ffc857;color:#ffc857;border-radius:999px;padding:.3rem .9rem}}a.en:hover{{background:#ffc857;color:#14110f}}
a{{display:flex;justify-content:space-between;gap:1rem;padding:1.1rem 0;color:inherit;text-decoration:none;font-family:Fraunces,Georgia,serif;font-weight:900;font-size:2rem}}
a span{{font-family:Inter,sans-serif;font-size:1rem;letter-spacing:.12em;text-transform:uppercase;color:#ffc857;align-self:center}}a:hover{{color:#ffc857}}</style></head>
<body><h1>Morning Edition</h1><ul>{''.join(items)}</ul></body></html>"""
(root / "index.html").write_text(html, encoding="utf-8")
print(f"index.html: {len(items)} issue(s)")
