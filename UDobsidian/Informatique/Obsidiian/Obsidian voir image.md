---
feature: thumbnails/external/14e32bd8041e70227b141e4540a15685.failed.png
thumbnail: thumbnails/resized/718e1d5390d505cdc7db204dd06fb3a9_86cf658e.webp
---
# Obsidian voir image


Comment dans Obsidian copier l'adresse d'un site Web et en voir une image les premières images sur la note.

Pour copier l'adresse d'un site web et en voir les premières images dans une note sur Obsidian, vous avez plusieurs options, de la simple copie manuelle à l'automatisation complète avec des plugins.

### Méthode 1 : Copie manuelle simple (sans plugin)

C'est la méthode la plus rapide pour une utilisation occasionnelle. Obsidian gère nativement le collage de contenu web.

1.  **Copiez le contenu** : Sur la page web, sélectionnez le texte et les images que vous voulez sauvegarder, puis copiez-les (Ctrl+C / Cmd+C).
2.  **Collez dans Obsidian** : Dans votre note, faites un collage (Ctrl+V / Cmd+V).
    - Obsidian convertit automatiquement le texte copié en Markdown.
    - **Important** : Les images seront affichées, mais leurs liens pointent vers l'URL d'origine en ligne . Si la page web est supprimée ou si vous n'avez plus de connexion Internet, ces images ne seront plus visibles.

### Méthode 2 : Téléchargement automatique des images (avec plugin)

Pour que les images soient sauvegardées localement dans votre vault, le meilleur outil est le plugin **Image Embedder**.

Voici comment l'utiliser :
1.  **Installation** : Allez dans *Paramètres* → *Plugins communautaires* → *Parcourir*, puis recherchez "Image Embedder" et installez-le .
2.  **Fonctionnement** :
    - Copiez l'URL d'une image (ou un contenu web contenant des images).
    - Collez-la dans votre note.
    - Le plugin détecte automatiquement qu'il s'agit d'une image, la télécharge et l'enregistre dans votre vault .
3.  **Personnalisation** : Vous pouvez configurer dans les paramètres du plugin :
    - Le dossier où sauvegarder les images.
    - Le format du nom de fichier.
    - Une demande de confirmation avant chaque téléchargement .

### Méthode 3 : Récupérer l'adresse et la vignette via le code Markdown

Si vous voulez garder le lien et ajouter une image de la page, vous pouvez le faire en écrivant manuellement la syntaxe Markdown.

1.  **Copiez l'URL** de la page web.
2.  **Dans votre note**, écrivez la syntaxe d'un lien, puis en dessous, celle d'une image.
    ```markdown
    # [Nom de votre lien](https://l-url-de-votre-site.com)
    ![Image de la page](https://l-url-de-l-image-que-vous-voulez-afficher.com)
    ```
    - `[Texte du lien](URL)` pour créer un lien cliquable vers le site .
    - `![Texte alternatif](URL_de_l_image)` pour afficher l'image. Vous devez trouver l'URL de l'image que vous voulez utiliser comme vignette (faites un clic droit sur l'image de la page web et sélectionnez "Copier l'adresse de l'image") .

En résumé :
- Pour un besoin **rapide et ponctuel**, utilisez le **copier/coller simple**.
- Pour un **archivage fiable** et une collection d'images locale, installez le plugin **Image Embedder**.
- Pour un contrôle **manuel**, utilisez directement la **syntaxe Markdown**.
- 
#### Voici les deux meilleures options, selon ce qui correspond le mieux à votre façon de travailler.
Merci pour la précision. Je comprends mieux ce que vous cherchez : un processus entièrement automatisé où, en collant une simple URL, la note affiche automatiquement la première image du site.

La bonne nouvelle, c'est qu'il existe des plugins conçus spécifiquement pour cela. Aucun ne fait exactement ce que vous décrivez en une seule action "coller et voir l'image", mais plusieurs s'en rapprochent avec des workflows simples.

Voici les deux meilleures options, selon ce qui correspond le mieux à votre façon de travailler.

---

### Option 1 : Le plus proche de votre demande — "Link Embed"

Le plugin ** [Obsidian Link Embed](https://github.com/Seraphli/obsidian-link-embed) **  est probablement ce qui se rapproche le plus de ce que vous voulez.

**Ce qu'il fait** : Il transforme une URL que vous avez collée en un "bloc de prévisualisation". Ce bloc inclut généralement le titre de la page, une description, et surtout **l'image principale du site** (souvent celle utilisée pour les aperçus sur les réseaux sociaux).

**Comment l'utiliser (le flux) :**
1.  Copiez l'URL du site.
2.  Collez-la dans votre note Obsidian.
3.  **Action unique** : Sélectionnez l'URL et lancez la commande `Link Embed: Embed link` (via la palette de commandes avec `Ctrl/Cmd+P` ).
4.  **Le résultat** : L'URL est remplacée par un bloc contenant l'image et les métadonnées.

**Pourquoi c'est une bonne option** :
- Vous ne manipulez que l'URL. Le plugin récupère le reste (image, titre, description) automatiquement via une API externe.
- Il gère un grand nombre de sites et peut même télécharger une copie locale de l'image pour que vous l'ayez hors ligne .
- Il propose une option "Auto Embed" dans ses paramètres. Si vous l'activez, coller une URL sur une ligne vide pourrait automatiquement la transformer en aperçu, sans avoir à lancer la commande à chaque fois .

---

### Option 2 : L'approche "image à la une" — "Featured Image"

Le plugin ** [Featured Image](https://github.com/johansan/obsidian-featured-image) **  adopte une philosophie différente, mais très puissante.

**Ce qu'il fait** : Il analyse automatiquement le contenu de votre note, y cherche la **première image** (ou un lien YouTube), et enregiste son chemin dans une propriété (frontmatter) de la note, comme `feature: chemin/de/l/image.png` .

**Comment l'utiliser (le flux) :**
1.  Copiez l'URL du site.
2.  Collez l'URL dans votre note.
3.  **Le plugin ne fait rien de visible immédiatement.** Il va simplement créer une propriété en haut de votre note avec le lien vers l'image.
4.  Pour **voir** l'image dans votre note, vous devez faire une petite étape supplémentaire : utiliser une formule Dataview ou un petit bout de code inline.
    ```dataview
    TABLE embed(link(feature)) AS "Image", file.name AS "Note"
    FROM "votre/dossier"
    ```
    Ou, si vous voulez afficher l'image directement dans la note qui contient l'URL, vous pouvez utiliser ce code (inspiré d'une solution du forum Obsidian ) :
    `="![](" + this.feature + ")"`

**Pourquoi c'est une bonne option** :
- Le plugin fait le gros du travail : trouver l'image et l'enregistrer en local .
- La visualisation (l'étape `="![](" + this.feature + ")"` ) vous donne un contrôle total. Vous pouvez la mettre où vous voulez, à la fin de la note, au début, etc. Une fois la formule écrite dans un template, le processus devient très rapide.

---

### À propos des méthodes que vous avez probablement essayées

*   **Copier/Coller simple** : Obsidian ne peut pas deviner quelle image vous voulez parmi toutes celles d'une page web. Il ne fait que coller ce qui est dans votre presse-papiers.
*   **Image Embedder** : Ce plugin  est excellent, mais son but est de télécharger une **image dont vous avez déjà l'URL directe**. C'est un plugin pour "copier l'adresse de l'image" et la sauvegarder. Ce n'est pas ce que vous cherchez.
*   **Auto Embed** : Ce plugin  sert à intégrer une page web entière dans votre note via une iframe, et non à en extraire une image.

### En résumé, quel plugin choisir ?

| Si vous voulez... | Le meilleur plugin est... |
| :--- | :--- |
| **...voir l'image immédiatement** après avoir collé l'URL, dans un joli bloc, sans étape de code | ** [Link Embed](https://github.com/Seraphli/obsidian-link-embed) ** (activez l'option "Auto Embed" dans ses réglages) |
| **...automatiser la collecte** et créer des galeries d'images, quitte à faire un peu de code au début pour la mise en page | ** [Featured Image](https://github.com/johansan/obsidian-featured-image) ** (avec la formule Dataview ou inline) |

Essayez **Link Embed** en premier. Il est très simple et semble correspondre exactement au flux "copier l'URL → voir l'image" que vous décrivez.

----------- 



La réponse courte est **non, ni Link Embed ni les plugins similaires ne fonctionnent correctement avec Facebook**.

Voici pourquoi, et quelles sont vos alternatives.

### Pourquoi Facebook ne fonctionne pas


Comment dans Obsidian copier l'adresse d'un site Web et en voir une image les premières images sur la note.

Le problème vient de Facebook lui-même, pas des plugins Obsidian :



1. **Restrictions techniques** : Facebook bloque les tentatives d'extraction automatique de contenu. Les services utilisés par les plugins (comme les API Open Graph ou iframely) ne peuvent pas récupérer les images ou les descriptions des publications Facebook .
    
2. **Authentification requise** : La plupart du contenu Facebook est privé ou nécessite d'être connecté. Les plugins ne peuvent pas se connecter à votre compte Facebook, donc ils ne voient que des pages vides ou des messages d'erreur.
    
3. **Absence de support** : Les plugins comme **Auto Embed** listent clairement les réseaux sociaux qu'ils supportent (X/Twitter, Reddit, TikTok), et **Facebook n'en fait pas partie** .
    

### Ce qui fonctionne (et ce qui ne fonctionne pas)

|**Méthode**|**Résultat avec Facebook**|
|---|---|
|Link Embed|❌ Ne fonctionne pas|
|Auto Embed|❌ Non supporté|
|Copier/coller simple|⚠️ Copie le texte mais rarement les images|
|Copier l'image individuellement|✅ Fonctionne, mais manuel|

### Alternatives possibles

Si vous avez besoin de capturer des publications Facebook, voici ce qui fonctionne réellement :

**Solution 1 : Capture d'écran manuelle**

- Faites une capture d'écran de la publication
    
- Collez-la dans votre note
    
- Ajoutez le lien Facebook à côté
    

**Solution 2 : Copie d'image individuelle**

- Clic droit sur l'image Facebook → "Copier l'adresse de l'image"
    
- Utilisez **Image Embedder** pour la télécharger automatiquement
    
- Collez le lien de la publication séparément
    

**Solution 3 : Alternative avec Reddit, X, TikTok** Si votre besoin est de capturer des contenus _autres_ que Facebook, ces plateformes sont supportées par certains plugins comme Auto Embed .

### Conclusion

Aucune méthode automatisée ne permet d'obtenir une prévisualisation d'un lien Facebook dans Obsidian. Si capturer des publications Facebook est important pour votre workflow, le plus fiable reste la capture d'écran ou la copie manuelle de l'image.

Souhaitez-vous que je vous détaille la procédure pour automatiser la copie d'image avec Image Embedder, même si cela reste un processus semi-