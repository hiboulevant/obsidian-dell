---
feature: thumbnails/external/bfd28def9f54a16ed8f5f5aac30ade07.failed.png
thumbnail: thumbnails/resized/a569ce4e8f9dbadb26e1c775e05d9d9c_86cf658e.webp
---
# Insérer une image Url OU LOCAL
---
title: "Comment insérer une image ..."
source: "https://gemini.google.com/app/3f16ca1efda3af66"
author:
  - "[[Gemini]]"
published:
created: 2025-10-07
description: "Voici Gemini, l'assistant IA de Google. Obtenez de l'aide pour la rédaction de contenu, la planification, le remue-méninges et plus encore. Découvrez la puissance de l'IA générative."
tags:
  - "clippings"
---
Comment insérer une image à partir de l'adresse d'un site Web dans obsidian.

---

Pour insérer une image à partir de l'adresse d'un site Web (lien externe) dans Obsidian, vous devez utiliser la **syntaxe Markdown standard pour les images**.

## Comment insérer l'image

1. **Obtenez l'adresse directe de l'image**:
	- Sur la page Web, faites un clic droit sur l'image que vous voulez insérer.
	- Sélectionnez généralement l'option **"Copier l'adresse de l'image"** (ou une option similaire). L'URL doit se terminer par l'extension du fichier image (par exemple, `.jpg`, `.png`, `.gif`, `.webp`).
2. **Utilisez la syntaxe Markdown**:
	- Dans votre note Obsidian, tapez la syntaxe suivante, en remplaçant le texte entre parenthèses et crochets:
	Markdown
	```
	![Texte alternatif](Adresse de l'image sur le Web)
	```
	- **`Texte alternatif`**: Une courte description de l'image. Ce texte s'affiche si l'image ne peut pas être chargée.
	- **`Adresse de l'image sur le Web`**: L'URL que vous avez copiée à l'étape 1.

### Exemple concret

Si l'adresse de votre image est `https://exemple.com/photos/image-test.jpg`, la syntaxe sera:

Markdown

```
![Logo d'exemple](https://exemple.com/photos/image-test.jpg)
```

Une fois que vous passez en mode **Aperçu (Reading view)**, l'image devrait s'afficher directement dans votre note.

---

## Optionnel: Modifier la taille

Vous pouvez spécifier la largeur de l'image en pixels en ajoutant une barre verticale (`|`) et la largeur désirée juste après la parenthèse fermante du texte alternatif.

Markdown

```
![Texte alternatif|Largeur en pixels](Adresse de l'image sur le Web)
```

### Exemple avec taille modifiée

Pour afficher l'image à une largeur de 300 pixels:

Markdown

```
![Logo d'exemple|300](https://exemple.com/photos/image-test.jpg)
```

**Note importante**: L'image reste hébergée sur le site Web d'origine. Si le site supprime ou déplace l'image, celle-ci n'apparaîtra plus dans votre note Obsidian. Pour une référence pérenne, il est préférable de télécharger l'image et de l'insérer comme fichier local dans votre coffre-fort Obsidian.