# Masquer les éléments d'interfaces
## Masquer les éléments d'interfaces


Oui, il est tout à fait possible de masquer les éléments d'interface comme les thumbnails et autres fonctionnalités en mode lecture dans Obsidian. Il existe principalement deux approches pour y parvenir : l'utilisation de **plugins** ou de **fragments CSS**.

Voici comment procéder pour les deux méthodes.

### 🧩 Méthode 1 : Utiliser un plugin (approche la plus simple)

La manière la plus directe et sans code est d'utiliser un plugin dédié. Le plugin **Hider**, créé par Kepano, est parfait pour cela .

*   **Installation** : Rendez-vous dans les paramètres d'Obsidian, section "Plugins communautaires", désactivez le "Mode sans échec", puis parcourez la liste pour trouver et installer "Hider".
*   **Fonctionnalités** : Une fois installé et activé, le plugin ajoute une section dans vos paramètres. Vous pouvez alors simplement cocher les éléments que vous souhaitez masquer .
*   **Ce que vous pouvez masquer avec Hider** :
    *   `Hide metadata in Reading view` : C'est l'option qui vous intéresse pour masquer les thumbnails et les propriétés en mode lecture .
    *   Masquer le ruban d'applications, la barre d'onglets, la barre d'état, etc.

### ✨ Méthode 2 : Utiliser un fragment CSS personnalisé

Si vous préférez une solution plus personnalisée ou ne voulez pas installer de plugin, vous pouvez utiliser un fragment CSS. C'est une approche très puissante pour modifier l'apparence d'Obsidian .

1.  **Trouver le bon sélecteur** : Pour masquer les thumbnails (qui font partie des métadonnées), vous devez cibler la classe CSS `.metadata-property` ou le conteneur `.metadata-container` . L'élément exact peut varier selon le thème que vous utilisez.
2.  **Créer le fragment CSS** :
    *   Ouvrez les paramètres d'Obsidian, allez dans "Apparence".
    *   Dans la section "Fragments CSS", cliquez sur le dossier (icône de dossier) pour ouvrir le dossier des fragments.
    *   Créez un nouveau fichier texte, par exemple `hide-thumbnails.css` , et ouvrez-le avec un éditeur de texte.
    *   Collez-y le code suivant :

```css
/* Masque toute la section des métadonnées (propriétés) en mode lecture */
.markdown-reading-view .metadata-container {
    display: none;
}
```

*   **Attention** : Le code ci-dessus masque **toutes** les propriétés de la note (tags, dates, etc.) et pas seulement les thumbnails .

3.  **Appliquer le fragment** : Revenez dans les paramètres d'Obsidian, toujours dans "Apparence", et cliquez sur l'icône de rafraîchissement à côté de "Fragments CSS". Votre nouveau fragment `hide-thumbnails.css` devrait apparaître. Activez-le.

> **💡 Alternative pour masquer seulement l'icône en mode lecture/édition**
> Si votre objectif n'est pas de masquer les thumbnails, mais plutôt les icônes de vue (les petits icônes en haut à droite pour passer du mode édition au mode lecture), vous pouvez utiliser ce fragment CSS à la place  :
> ```css
> button[aria-label*="Current view"] {
>   display: none !important;
> }
> ```

### 💎 Résumé

| Méthode | Niveau de difficulté | Avantages | Idéal pour |
| :--- | :--- | :--- | :--- |
| **Plugin Hider** | Facile | Simple, sans code, options claires | Masquer rapidement des éléments comme les métadonnées sans se soucier de la syntaxe CSS |
| **Fragments CSS** | Intermédiaire | Contrôle total, plus léger qu'un plugin | Personnaliser finement l'apparence et masquer des éléments spécifiques |

**En résumé** : Si vous souhaitez une solution rapide et simple, installez le plugin **Hider**. Si vous voulez un contrôle plus précis sur ce qui est masqué ou si vous préférez éviter les plugins, la méthode du **fragment CSS** est la voie à suivre. N'hésitez pas à commencer avec le plugin, et à explorer les fragments CSS plus tard si vous avez besoin de personnalisations supplémentaires .
