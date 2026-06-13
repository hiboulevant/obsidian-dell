---
cssclasses:
  - cards
  - cards-cover
  - cards-cols-4
aliases:
  - Books {{date:YYYY}}
modified:
  - 2025-05-29T07:38:12-05:00
---
```dataviewjs
await dv.view("Simple Systems/Code/bookstats");
```

```dataviewjs
await dv.view("Simple Systems/Code/bookshelf", {year: {{date:YYYY}}, grouping: 'month'});
```
