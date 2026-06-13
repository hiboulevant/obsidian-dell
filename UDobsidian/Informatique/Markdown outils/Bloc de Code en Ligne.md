# Bloc de Code en Ligne

#BlocCode #markdown 

Pour reproduire le style d'un **petit carré** ou d'un **bloc de texte formaté** (comme celui que j'utilise pour le code ou les commandes), vous pouvez utiliser la syntaxe **Markdown pour les blocs de code** dans Obsidian.

---

## 1. Bloc de Code en Ligne (Inline Code)

Si vous voulez mettre en évidence un mot ou une petite phrase dans le corps d'un paragraphe, comme une commande ou une variable, utilisez les **accents graves simples** (backticks).

- **Syntaxe :**
    
    Markdown
    
    ```
    `votre texte ici`
    ```
    
- **Résultat :** Cela donne un petit carré gris et discret, comme : `votre texte ici`.
    
- **Utilisation :** Idéal pour les noms de fichiers (`note.md`), les raccourcis clavier (`Ctrl+C`), ou les petites valeurs.
    

---

## 2. Bloc de Code Multiligne

Si vous voulez encadrer un **paragraphe entier, un extrait de code, ou une série de commandes** pour qu'elles puissent être facilement copiées, utilisez les **trois accents graves** (fence code block).

- **Syntaxe :**
    
    Votre paragraphe
    
    ou plusieurs lignes de texte
    
    à mettre dans le carré.
    
- **Résultat :**
    
    ```
    Votre paragraphe
    ou plusieurs lignes de texte
    à mettre dans le carré.
    ```
    
- **Utilisation :** Ceci est la méthode que j'utilise pour présenter les syntaxes. C'est le style le plus proche du "petit carré" que vous souhaitez reproduire, car il crée un bloc distinct avec un fond différent et, dans de nombreuses vues Markdown, un bouton de copie.
    

### Optionnel : Spécifier la Langue

Vous pouvez améliorer ce bloc en spécifiant la langue de programmation ou le type de contenu juste après les trois accents graves d'ouverture (cela ne change rien pour le presse-papier, mais peut ajouter une coloration syntaxique si Obsidian le supporte).

- **Exemple (Syntaxe Markdown) :**
    
    Markdown
    
    ````
    ```markdown
    # Votre Note
    - Liste d'éléments
    ````
    
- Exemple (Texte simple) :
    
    Si vous ne spécifiez rien, vous obtenez un bloc de texte simple. Vous pouvez aussi utiliser text :
    
    Plaintext
    
    ```
    Ceci est un paragraphe
    dans un carré simple.
    ```
    

En résumé, utilisez les **trois accents graves (```)** pour créer un bloc de texte multiligne encadré et facile à copier.