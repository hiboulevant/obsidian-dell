# Dashboard Tension
```dataview
TABLE WITHOUT ID
  date + " à " + heure AS "Date",
  systolique + "/" + diastolique + " mmHg" AS "Tension",
  pouls + " bpm" AS "Pouls",
  notes AS "Notes"
FROM "Tension Artérielle"
SORT date DESC, heure DESC
```