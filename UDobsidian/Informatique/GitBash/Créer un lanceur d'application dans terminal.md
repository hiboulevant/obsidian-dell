# Créer un lanceur d'application dans terminal
Pour choisir l'icône dans un lanceur .desktop, voici les différentes méthodes :

## 1. **Utiliser une icône existante du système**

### Chercher les icônes disponibles :
```bash
# Rechercher toutes les icônes disponibles
find /usr/share/icons ~/.local/share/icons -name "*.png" -o -name "*.svg" | less

# Chercher par nom (exemple pour "terminal")
find /usr/share/icons -name "*terminal*" -o -name "*term*" | head -20

# Lister les icônes dans les thèmes courants
ls /usr/share/icons/gnome/scalable/apps/
ls /usr/share/icons/hicolor/scalable/apps/
```

### Utiliser une icône sans extension :
```ini
Icon=utilities-terminal
Icon=gnome-terminal
Icon=terminal
Icon=application-x-terminal
```

## 2. **Utiliser le chemin absolu vers une image**

```ini
# Fichier PNG
Icon=/chemin/complet/vers/mon-icone.png

# Fichier SVG (recommandé pour la qualité)
Icon=/chemin/complet/vers/mon-icone.svg

# Icône dans votre répertoire personnel
Icon=/home/votreuser/.local/share/icons/monapp.png
```

## 3. **Placer l'icône au bon endroit**

### Emplacements standards :
```bash
# Pour l'utilisateur courant
~/.local/share/icons/
~/.icons/

# Pour tout le système
/usr/share/icons/
/usr/share/pixmaps/
```

### Exemple de configuration :
```bash
# Créer le dossier si nécessaire
mkdir -p ~/.local/share/icons

# Copier votre icône
cp /chemin/source/icone.png ~/.local/share/icons/

# Dans le fichier .desktop
Icon=monapp  # Sans extension si dans un dossier d'icônes
# ou
Icon=/home/votreuser/.local/share/icons/monapp.png  # Avec chemin complet
```

## 4. **Trouver l'icône d'une application existante**

```bash
# Trouver le fichier .desktop d'une application
locate .desktop | grep firefox | head -5

# Voir l'icône utilisée
grep Icon /usr/share/applications/firefox.desktop

# Suivre le chemin de l'icône
grep -r "Icon=firefox" /usr/share/icons/
```

## 5. **Taille et format recommandés**

- **Formats supportés** : PNG, SVG, XPM
- **Tailles recommandées** :
  - 16 x 16, 24 x 24, 32 x 32, 48 x 48, 64 x 64, 128 x 128, 256 x 256
- **Meilleure pratique** : SVG (vectoriel) ou PNG 512 x 512

## 6. **Exemple complet avec icône personnalisée**

```bash
# 1. Préparer l'icône
mkdir -p ~/.local/share/icons
# Copier votre icône.svg dans ce dossier

# 2. Créer le fichier .desktop
cat > ~/.local/share/applications/monapp.desktop << 'EOF'
[Desktop Entry]
Name=Mon Application
Comment=L'application dans un terminal
Exec=gnome-terminal -- bash -c "commande; exec bash"
Icon=monapp  # Nom du fichier sans extension dans ~/.local/share/icons/
Terminal=false
Type=Application
Categories=Utility;
EOF
```

## 7. **Actualiser le cache des icônes**

Après avoir ajouté une icône :
```bash
# Reconstruire le cache
gtk-update-icon-cache -f ~/.local/share/icons/

# Si dans /usr/share/icons/ (nécessite sudo)
sudo gtk-update-icon-cache /usr/share/icons/hicolor/
```

## 8. **Tester l'icône**

```bash
# Voir comment l'icône sera interprétée
desktop-file-validate ~/.local/share/applications/monapp.desktop

# Tester l'affichage
gio launch ~/.local/share/applications/monapp.desktop
```

## 9. **Utiliser un outil graphique pour choisir**

Installer `gnome-icon-browser` :
```bash
sudo apt install gnome-icon-browser
```

Puis lancer :
```bash
gnome-icon-browser
```

## 10. **Exemples d'icônes courantes**

```ini
# Terminal
Icon=utilities-terminal
Icon=gnome-terminal

# Éditeur de texte
Icon=accessories-text-editor
Icon=gedit

# Navigateur
Icon=web-browser
Icon=firefox

# Système
Icon=system-file-manager
Icon=preferences-system

# Développement
Icon=applications-development
Icon=text-x-python
```

Le système cherchera l'icône dans cet ordre :
1. Chemin absolu spécifié
2. `~/.icons/`
3. `~/.local/share/icons/`
4. `/usr/share/icons/`
5. `/usr/share/pixmaps/`

Si l'icône ne s'affiche pas, vérifiez :
- Les permissions du fichier
- Le cache des icônes
- La présence effective du fichier à l'emplacement indiqué