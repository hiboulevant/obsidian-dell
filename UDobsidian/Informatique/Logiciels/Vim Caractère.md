# Vim Caractère

- le mode "commande" ou certains caractères ont une action spécifique (x supprime un caractère, D supprime la fin de la ligne, etc)
- le mode "insert" où là les caractères tapés s'insèrent dans le texte,
-  ---- 

Vim, l'éditeur de texte puissant, utilise une variété de commandes pour naviguer et éditer des fichiers. Voici un aperçu des principales commandes et caractères utiles dans Vim :

### Modes de Vim

1. **Normal Mode** : Mode par défaut pour naviguer et donner des commandes.
2. **Insert Mode** : Pour insérer du texte. Accéder en appuyant sur `i` (inserer), `a` (ajouter), ou `o` (ouvrir une nouvelle ligne).
3. **Visual Mode** : Pour sélectionner du texte. Accéder en appuyant sur `v` (visual) ou `V` (visual en ligne).

### Commandes de base

- `h` : Déplacer le curseur à gauche.
- `j` : Déplacer le curseur vers le bas.
- `k` : Déplacer le curseur vers le haut.
- `l` : Déplacer le curseur à droite.

### Commandes de navigation

- `gg` : Aller au début du fichier.
- `G` : Aller à la fin du fichier.
- `:n` : Aller à la ligne n.
- `%` : Aller à la parenthèse/brace correspondante.

### Commandes de modification

- `i` : Passer en mode insertion avant le curseur.
- `a` : Passer en mode insertion après le curseur.
- `o` : Ouvrir une nouvelle ligne en dessous.
- `O` : Ouvrir une nouvelle ligne au-dessus.
- `x` : Supprimer le caractère sous le curseur.
- `dd` : Supprimer la ligne entière.
- `yy` : Copier (yanker) la ligne entière.
- `p` : Coller le texte copié ou coupé après le curseur.

### Commandes de recherche

- `/mot` : Rechercher "mot" vers l'avant.
- `?mot` : Rechercher "mot" vers l'arrière.
- `n` : Aller à la prochaine occurrence de la recherche.
- `N` : Aller à l'occurrence précédente.

### Commandes d'enregistrement

- `:w` : Enregistrer le fichier.
- `:q` : Quitter Vim.
- `:wq` : Enregistrer et quitter.
- `:q!` : Quitter sans enregistrer.

### Annuler et rétablir

- `u` : Annuler la dernière action.
- `Ctrl + r` : Rétablir l'action annulée.

### Autres commandes utiles

- `:set number` : Afficher les numéros de ligne.
- `:set nonumber` : Cacher les numéros de ligne.
- `:syntax on` : Activer la coloration syntaxique.
- `:help` : Ouvrir l'aide de Vim.

Ces commandes couvrent une grande partie des fonctionnalités courantes de Vim. En fonction de vos besoins, il existe de nombreuses autres commandes et options que vous pourriez explorer. N'hésitez pas à consulter la documentation de Vim pour des informations plus approfondies.

---- 
Si vous avez besoin d'utiliser le slash inverse dans une commande ou une expression, vous n'avez pas besoin de préfixe particulier. Enfin, si vous êtes en mode normal et que vous souhaitez insérer un caractère sans passer en mode insertion, vous pouvez utiliser `Ctrl + V` suivi de la touche du caractère que vous souhaitez insérer. Par exemple, `Ctrl + V`, puis `\` pour insérer un slash inverse.





































































