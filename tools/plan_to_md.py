# Turns plan.json (from gen_day_plan.py) into 19_DAY_BY_DAY_PLAN.md.
# Usage: python plan_to_md.py <plan.json> <output.md>
import json, sys, datetime as dt

src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src, encoding="utf8"))
K = {"c": "C", "elec": "Electronics", "course": "Course", "proj": "Project", "read": "Reading", "eng": "English",
     "ielts": "IELTS", "ger": "German", "adm": "Admin", "app": "Application", "mile": "MILESTONE", "track": "Tracking", "rest": "Rest"}
L = ["# 19 — Day-by-Day Plan (Oct 5, 2026 → Oct 1, 2028)", "",
     "> Generated from `tools/gen_day_plan.py` (last run " + d["generated"][:10] + "). Same data as the online tracker: https://claude.ai/artifact/7hafZ8gt7CzNCSrRRy2Zd9",
     "> Source of truth for phases: `07_MONTHLY_TIMELINE.md`. Times are minutes. Tick days in the tracker, not here.", ""]
ph = {p["id"]: p for p in d["phases"]}
lastp = lastm = None
for day in d["days"]:
    t = dt.date.fromisoformat(day["d"])
    if day["p"] != lastp:
        p = ph[day["p"]]
        L += ["", f"## {p['id']} — {p['name']} ({p['from']} → {p['to']})", ""]
        lastp = day["p"]
    if day["d"][:7] != lastm:
        L += ["", f"### {t.strftime('%B %Y')}", ""]
        lastm = day["d"][:7]
    tot = sum(x["m"] for x in day["t"])
    L.append(f"**{t.strftime('%a %d %b')}**" + (" · deload" if day["dl"] else "") + (f" · {tot} min" if tot else ""))
    for x in day["t"]:
        L.append(f"- [{K[x['k']]}] {x['t']}" + (f" ({x['m']} min)" if x["m"] else "") + (f" — _{x['h']}_" if x["h"] else ""))
    L.append("")
open(out, "w", encoding="utf8").write("\n".join(L))
print(len(d["days"]), "days written")
