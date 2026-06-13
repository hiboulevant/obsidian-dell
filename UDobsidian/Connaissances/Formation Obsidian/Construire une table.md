# Construire une table

Pour créer une table avec Dataview dans Obsidian, vous pouvez suivre les étapes suivantes:

1. Assurez-vous d'avoir installé le plugin Dataview dans Obsidian.

2. Créez un fichier Markdown et ajoutez-y une liste de notes qui contiennent les données que vous souhaitez ajouter à votre table. Par exemple, vous pouvez créer une liste de notes contenant des informations sur des livres.

3. Dans votre fichier Markdown, créez une table en utilisant la syntaxe Markdown standard pour les tables. Par exemple:

```
| Titre | Auteur | Date de publication |
|-------|--------|---------------------|
| [[Le Seigneur des anneaux]] | J.R.R. Tolkien | 1954 |
| [[Harry Potter à l'école des sorciers]] | J.K. Rowling | 1997 |
```

4. Utilisez la fonction Dataview pour extraire les données de vos notes et les ajouter à votre table. Par exemple, pour extraire le titre, l'auteur et la date de publication de vos notes, vous pouvez utiliser la requête suivante:

```
table Titre, Auteur, "Date de publication"
from #livres
```

5. Actualisez votre fichier Markdown pour voir votre table mise à jour avec les données extraites.

J'espère que cela vous aidera à créer une table avec Dataview dans Obsidian!
