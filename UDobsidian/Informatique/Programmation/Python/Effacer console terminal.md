---
tags:
  - console
  - console/terminal
---
# Effacer console terminal


Effacer l'écran de la console (Terminal)

Il n'existe pas de fonction intégrée directe, mais vous pouvez utiliser le module `os` pour appeler la commande système appropriée selon votre système d'exploitation. 

**Code multiplateforme recommandé :**

python

```
import os

def clear():
    # 'nt' correspond à Windows, sinon c'est Linux/macOS (posix)
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
```
2. Vider une Liste, un Dictionnaire ou un Ensemble

Si vous souhaitez vider le contenu d'un objet de données (comme une liste) sans supprimer l'objet lui-même, utilisez la méthode `.clear()`. 

python

```
ma_liste = [1, 2, 3]
ma_liste.clear()  # La liste devient []
```

Utilisez le code avec précaution.

Solutions alternatives

- **Raccourci clavier :** Dans la plupart des terminaux, vous pouvez simplement appuyer sur **Ctrl + L** pour effacer l'affichage manuellement.
- **Séquence d'échappement :** Une méthode plus rapide (sans import) consiste à imprimer un caractère spécial, bien que cela ne fonctionne pas sur tous les terminaux :
    
    python
    
    ```
    print("\033c", end="")
    ```
    
    Utilisez le code avec précaution.
Python
python

```
import os

def clear():
    # 'nt' correspond à Windows, sinon c'est Linux/macOS (posix)
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
```
Pour vider l'écran terminal Ctrl L