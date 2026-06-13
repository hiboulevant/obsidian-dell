---
tags:
  - Unbutu
  - désinstaller
---
# Désinstaller une application



Pour désinstaller l'application 

**Insync** sur Ubuntu Pro en 2026, vous pouvez utiliser le terminal pour une suppression propre et complète.

1. Suppression via le terminal (Recommandé)

Ouvrez votre terminal et exécutez les commandes suivantes selon vos besoins :

- **Désinstallation simple :**
    
    bash
    
    ```
    sudo apt-get remove insync
    ```
    
    Utilisez le code avec précaution.
    
    Cette commande supprime l'application mais conserve vos fichiers de configuration.
- **Désinstallation complète (incluant les fichiers de configuration) :**
    
    bash
    
    ```
    sudo apt-get purge insync
    ```
    
    Utilisez le code avec précaution.
    
    L'option `purge` efface également les fichiers de configuration système associés à l'application.
- **Nettoyage des dépendances inutiles :**  
    Après la désinstallation, il est conseillé de supprimer les paquets qui ont été installés comme dépendances et qui ne sont plus nécessaires :
    
    bash
    
    ```
    sudo apt-get autoremove
    ```
    
    Utilisez le code avec précaution.
    
     

2. Suppression manuelle des données utilisateur

Même après une purge, certains dossiers de données locales peuvent subsister dans votre répertoire personnel. Pour les supprimer, utilisez la commande suivante : 

bash

```
rm -rf ~/.config/Insync
```

Utilisez le code avec précaution.

_Note : Assurez-vous d'avoir sauvegardé vos données importantes avant de supprimer ce dossier._ 

3. Suppression via l'interface graphique (App Center)

Si vous préférez une méthode visuelle :

1. Ouvrez l'**App Center** (ou Logiciels Ubuntu).
2. Allez dans l'onglet **Installées**.
3. Cherchez **Insync** dans la liste.
4. Cliquez sur le bouton **Supprimer** (ou l'icône de corbeille) et confirmez avec votre mot de passe. 

5. Retrait du dépôt (Optionnel)

Si vous avez ajouté le dépôt officiel d'Insync à vos sources de logiciels, vous pouvez le retirer pour éviter des erreurs lors des futures mises à jour :

- Allez dans **Logiciels et mises à jour** > onglet **Autres logiciels**.
- Sélectionnez la ligne correspondant à `apt.insynchq.com` et cliquez sur **Supprimer**.