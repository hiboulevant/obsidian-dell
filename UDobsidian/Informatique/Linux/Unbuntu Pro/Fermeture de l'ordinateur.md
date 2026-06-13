---
tags:
  - fermeture/ubuntu
---
Plusieurs solutions selon votre environnement de bureau Ubuntu Pro :

## 1. **Solution la plus simple - Raccourcis clavier**
- `Alt + F4` (sur le bureau) : menu de fermeture
- `Super (Windows) + D` puis `Alt + F4`
- `Ctrl + Alt + Suppr` (fonctionne souvent)
- `Ctrl + Alt + T` pour ouvrir un terminal, puis `poweroff` ou `sudo shutdown now`

## 2. **Rechercher dans les applications**
- Appuyez sur la touche `Super` (Windows)
- Tapez "arrêt", "fermeture" ou "power"
- Cherchez dans les paramètres système

## 3. **Si vous utilisez GNOME (interface par défaut)**
- Cliquez sur le coin supérieur droit (barre du haut)
- Le menu système devrait apparaître
- Si ce n'est pas le cas, appuyez sur `Super + M`

## 4. **Ajouter un raccourci manuellement**
```bash
# Créer un raccourci sur le bureau
sudo apt install gnome-tweaks
# Puis configurer via gnome-tweaks
```

## 5. **Si l'interface est corrompue**
```bash
# Redémarrer l'interface graphique
sudo systemctl restart gdm  # ou lightdm selon votre gestionnaire
```

## 6. **Solution terminal**
```bash
# Fermer la session
gnome-session-quit --power-off
# Ou directement éteindre
sudo shutdown -h now
```

**Note :** Ubuntu Pro utilise généralement la même interface que Ubuntu standard. Le problème Plusieurs solutions selon votre environnement de bureau Ubuntu Pro :

## 1. **Solution la plus simple - Raccourcis clavier**
- `Alt + F4` (sur le bureau) : menu de fermeture
- `Super (Windows) + D` puis `Alt + F4`
- `Ctrl + Alt + Suppr` (fonctionne souvent)
- `Ctrl + Alt + T` pour ouvrir un terminal, puis `poweroff` ou `sudo shutdown now`

## 2. **Rechercher dans les applications**
- Appuyez sur la touche `Super` (Windows)
- Tapez "arrêt", "fermeture" ou "power"
- Cherchez dans les paramètres système

## 3. **Si vous utilisez GNOME (interface par défaut)**
- Cliquez sur le coin supérieur droit (barre du haut)
- Le menu système devrait apparaître
- Si ce n'est pas le cas, appuyez sur `Super + M`

## 4. **Ajouter un raccourci manuellement**
```bash
# Créer un raccourci sur le bureau
sudo apt install gnome-tweaks
# Puis configurer via gnome-tweaks
```

## 5. **Si l'interface est corrompue**
```bash
# Redémarrer l'interface graphique
sudo systemctl restart gdm  # ou lightdm selon votre gestionnaire
```

## 6. **Solution terminal**
```bash
# Fermer la session
gnome-session-quit --power-off
# Ou directement éteindre
sudo shutdown -h now
```

**Note :** Ubuntu Pro utilise généralement la même interface que Ubuntu standard. Le problème pourrait venir :
- D'une extension GNOME qui cache le menu
- D'une configuration personnalisée
- D'un environnement de bureau différent (KDE, XFCE, etc.)

Pouvez-vous me décrire ce que vous voyez dans le coin supérieur droit de votre écran ? Cela m'aidera à identifier votre interface.pourrait venir :
- D'une extension GNOME qui cache le menu
- D'une configuration personnalisée
- D'un environnement de bureau différent (KDE, XFCE, etc.)

Pouvez-vous me décrire ce que vous voyez dans le coin supérieur droit de votre écran ? Cela m'aidera à identifier votre interface.