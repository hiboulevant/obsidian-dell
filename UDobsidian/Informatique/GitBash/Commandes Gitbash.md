# Commandes Gitbash
## **NAVIGATION DANS LES DOSSIERS**

# Voir où vous êtes
Pwd

# Lister les fichiers et dossiers (comme "dir" mais en mieux !)
Ls
Ls -la          # Détails complets
Ls -l           # Liste détaillée
Ls -la | head   # Premiers fichiers seulement

# Changer de dossier
Cd /c/Users/VotreNom
Cd Desktop      # Aller sur le Bureau
Cd ..           # Remonter d'un niveau
Cd ~            # Retour au dossier personnel

## 📋 **MANIPULATION DE FICHIERS**

# Créer un fichier
Touch mon_script. Sh

# Créer un dossier
Mkdir mes_scripts

# Voir le contenu d'un fichier
Cat mon_script. Sh

# Copier un fichier
Cp mon_script. Sh backup. Sh

# Supprimer un fichier
Rm backup. Sh

## ✍️ **VOTRE PREMIER SCRIPT SHELL**

# 1. Créer le script
Touch bonjour. Sh

# 2. L'éditer avec nano
Nano bonjour. Sh

**Dans nano, tapez :**

#!/bin/bash
Echo "🎉 Bonjour le monde du shell scripting !"
Echo "Je suis dans le dossier : $(pwd)"
Echo "Aujourd'hui nous sommes : $(date)"
Ls -la

**Sauvegarder** : Ctrl + O, puis **Entrée**  
**Quitter** : Ctrl + X

## 🚀 **EXÉCUTER LE SCRIPT**

bash

# Rendre le script exécutable
Chmod +x bonjour. Sh

# L'exécuter
./bonjour. Sh

## 🔍 **COMMANDES UTILES**
# Voir l'historique des commandes
History

# Chercher un fichier
Find . -name "*. Sh"

# Compter les fichiers
Ls | wc -l

# Voir l'espace disque
Df -h

# Voir les processus
Ps aux

## 🎯 **EXERCICE PRATIQUE**

**Créez un script qui :**

#!/bin/bash
Echo "=== MON PREMIER SCRIPT ==="
Echo "Utilisateur : $USER"
Echo "Dossier courant : $(pwd)"
Echo "Fichiers dans ce dossier : "
Ls -l | grep "^-" | wc -l
Echo "scripts .sh trouvés : "
Find . -name "*. Sh" 2>/dev/null

**Testez ces commandes une par une et voyez le résultat !** 😊

Qu'est-ce qui vous intéresse en particulier ? Navigation, manipulation de fichiers, ou écrire des scripts ?



