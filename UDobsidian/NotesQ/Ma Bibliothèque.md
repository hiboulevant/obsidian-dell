# Ma Bibliothèque

```dataview
TABLE 
  WITHOUT ID 
  file.link AS "Livre", 
  author AS "Auteur", 
  cover AS "Couverture"
FROM "Livres"  # Remplacez par votre dossier
file.tasks = false
SORT title ASC
const pages = dv.pages('"Livres"') .where(p => p.cover) // Filtre seulement les livres avec couverture .sort(p => p.title, 'asc');

dv.list(pages.map(p => dv.span(dv.fileLink(p.file.path, false), dv.el("br")) + dv.span(`![[${p.cover}|200]]`) + // Affiche la couverture en 200px, ajustez la taille dv.span(`**${p.title}** par ${p.author || 'Inconnu'}`)

));



