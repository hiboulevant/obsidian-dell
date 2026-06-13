# Bibliothèque Dataview Grok
### . Prérequis

- Installez et activez **Dataview** (*Paramètres > Plugins communautaires > Parcourir > Dataview*).

- Assurez-vous que vos notes de livres ont un frontmatter YAML avec cover (URL ou chemin local, ex. : cover: attachments/mon-livre.jpg ou cover: https://exemple.com/couverture.jpg).

- Téléchargez les couvertures localement pour éviter les problèmes d'URLs : Utilisez le plugin **Book Search** (par Anpigon) pour importer automatiquement les livres avec téléchargement d'images dans un dossier "attachments". Activez l'option "Download cover images" dans ses paramètres.

  -- 

  ### 2. Créez votre vue étagère avec Dataview

  Dans une note dédiée (ex. : "Ma Bibliothèque.md"), insérez ce bloc de code Dataview pour une **table simple avec couvertures** :

  text

  ```
  ```dataview
  TABLE 
    WITHOUT ID 
    file.link AS "Livre", 
    author AS "Auteur", 
    cover AS "Couverture"
  FROM "Livres"  # Remplacez par votre dossier
  SORT title ASC
  ```

- Cela affiche une table où la colonne "Couverture" rend les images inline si `cover` est une URL valide ou un chemin local.

- **Astuce** : Pour masquer les colonnes inutiles et centrer, ajoutez `file.tasks = false` pour ignorer les tâches.

  ----

Pour une **vue grille/étagère plus visuelle** (comme des cartes), utilisez ce code DataviewJS avancé (qui rend les couvertures en vignettes) :



const pages = dv.pages('"Livres"')
  .where(p => p.cover)  // Filtre seulement les livres avec couverture
  .sort(p => p.title, 'asc');

dv.list(pages.map(p => 
  dv.span(dv.fileLink(p.file.path, false), dv.el("br")) + 
  dv.span(`![[${p.cover}|200]]`) +  // Affiche la couverture en 200px, ajustez la taille
  dv.span(`**${p.title}** par ${p.author || 'Inconnu'}`)

));

----

- Cela crée une liste de "cartes" avec : lien vers la note, image de couverture, titre et auteur.
- Si vos couvertures sont locales, utilisez `![[chemin-relatif.jpg]]` ; pour les URLs, Dataview les gère bien.

### 3. Personnalisez en grille avec CSS (pour un vrai look "étagère")
Pour transformer cela en grille masonry (comme une étagère), ajoutez du CSS personnalisé :
- Allez dans *Paramètres > Apparence > CSS personnalisé* et collez ce code (inspiré de tutoriels communautaires) :

/* Grille pour couvertures de livres

 .bookshelf-grid {

 display: grid;

 grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));  / Ajustez pour plus/moins de colonnes /

gap: 10px;

margin: 10px 0;

}

.book-card {

text-align: center;

border: 1px solid #ddd;

border-radius: 8px;

padding: 10px;

border-radius: 8px;

padding: 10px;

background: #f9f9f9;

box-shadow: 2px 2px 5px rgba(0,0,0,0.1);  / Ombre pour effet 3D */

}

.book-cover {

width: 100%;

 height: auto;

 border-radius: 4px; }

text

```
- Puis, enveloppez votre bloc Dataview dans un callout Markdown pour appliquer la classe :
```

> [!bookshelf-grid]

dataviewjs

// Même code que ci-dessus, mais ajoutez des classes CSS
const pages = dv.pages('"Livres"').where(p => p.cover).sort(p => p.title, 'asc');
dv.container.className = 'bookshelf-grid';  // Applique la grille
pages.forEach(p => {
  dv.container.createEl('div', { cls: 'book-card' }).innerHTML = `
    <img src="${p.cover}" class="book-cover" alt="${p.title}">
    <strong>${p.title}</strong><br>
    ${p.author || 'Inconnu'}
  `;
  dv.fileLink(p.file.path, false, { subPath: '' });
});

- Résultat : Une grille responsive avec couvertures en vignettes, titres et auteurs, comme une étagère virtuelle !

### 4. Dépannage rapide pour Bookshelf (si vous voulez retenter)
- Vérifiez la console Obsidian (*Ctrl/Cmd + Shift + I > Console*) pour des erreurs comme "Failed to load image" – cela pointe souvent vers des URLs cassées.
- Testez avec une URL Open Library : `cover: https://covers.openlibrary.org/b/isbn/XXXXX-M.jpg` (remplacez XXXXX par l'ISBN du livre).
- Si rien, signalez le bug sur le forum Obsidian ou Reddit (r/ObsidianMD) – des devs comme Philip Weinke y répondent parfois.

Cette approche Dataview + CSS est plus flexible et stable que Bookshelf pour les couvertures, et elle s'intègre parfaitement avec Book Search pour l'automatisation. Si vous partagez un exemple de votre YAML ou une capture d'écran de l'erreur, je peux affiner ! Qu'en pensez-vous, on teste ça ?

