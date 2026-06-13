---
tags:
  - guide/Ubuntu
  - baobab
  - disque/sata
---
# Lenteur Ubuntu Pro



```markdown
# Guide de dépannage : Ubuntu Pro lent avec souris qui colle

## Symptômes
- Ralentissements généralisés
- Curseur de souris qui "colle" ou lag
- Retards à la frappe
- Tout fonctionne mais au ralenti

## 1. Diagnostic rapide : Identifier le coupable

### Ouvrir un terminal (Ctrl+Alt+T)

### Commandes de diagnostic essentielles :

**a. Vérifier l'utilisation des ressources en temps réel :**
```bash
htop
```
Ou
```bash
top
```

**Dans htop/top, observez :**
- Processus utilisant le plus de **CPU** (%) ou **MÉMOIRE** (MEM%)
- **%id** (CPU idle) - si proche de 0 = problème
- Utilisation de la **swap** - indique un manque de RAM
- **%wa** (I/O wait) - si >10-20% = problème disque

**b. Vérifier l'utilisation de la mémoire :**
```bash
free -h
```
*Signe de problème :* La colonne `available` est faible (< 10-15% de la RAM totale)

**c. Vérifier les logs système pour erreurs :**
```bash
journalctl --since "2 days ago" -p 3 -xb
```
(Affiche les erreurs critiques des 2 derniers jours)

**d. Vérifier l'espace disque :**
```bash
df -h
```
*Problème si :* Partition racine (`/`) > 95% pleine

## 2. Causes probables et solutions

### A. Mémoire RAM saturée / Swap excessive
**Symptômes :** Ralentissements extrêmes, swap fortement utilisée

**Solutions :**
1. **Redémarrer l'ordinateur** (solution temporaire)
2. Fermer les applications gourmandes identifiées via `htop`
3. Réduire le nombre d'onglets navigateur (Chrome/Firefox consomment beaucoup)
4. Nettoyer le cache mémoire :
```bash
sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
```

### B. Processus incontrôlé (100% CPU)
**Dans htop :**
1. Appuyer sur `P` (tri par CPU) ou `M` (tri par mémoire)
2. Identifier le processus problématique en tête
3. Noter son **PID**
4. Arrêter le processus :
```bash
kill [PID]
```
Si résistant :
```bash
kill -9 [PID]
```

### C. Problème de disque dur / SSD (I/O Wait élevé)
**Diagnostic :**
```bash
# Vérifier santé du disque
sudo smartctl -a /dev/sda | grep -i "reallocated\|pending\|uncorrectable"

# Vérifier I/O
iotop
```

**Solutions :**
1. Libérer de l'espace disque :
```bash
# Nettoyer paquets inutiles
sudo apt autoremove --purge

# Nettoyer journaux système
sudo journalctl --vacuum-time=3d

# Analyser l'espace utilisé
sudo apt install ncdu
ncdu /
```

### D. Problème graphique / pilotes
**Souris qui colle = problème interface graphique**

**Solutions :**
1. **Redémarrer le gestionnaire d'affichage :**
   - Ctrl+Alt+F 3 (passer en terminal texte)
   - Se connecter
   - Arrêter l'interface :
   ```bash
   sudo systemctl stop gdm3  # ou lightdm, sddm
   ```
   - Redémarrer :
   ```bash
   sudo systemctl start gdm3
   ```
   - Revenir à l'interface : Ctrl+Alt+F 1 ou F 2

2. **Changer de session graphique :**
   - Sur l'écran de connexion
   - Cliquer sur l'icône roue dentée
   - Choisir "Ubuntu sur Xorg" au lieu de "Ubuntu" (Wayland)

3. **Mettre à jour les pilotes graphiques :**
```bash
# Pour NVIDIA
sudo ubuntu-drivers autoinstall
```

### E. Problèmes de mises à jour (Ubuntu Pro)
**Si problème après mise à jour :**
1. **Changer de noyau :**
   - Redémarrer
   - Menu GRUB (Échap ou Maj au démarrage)
   - "Advanced options for Ubuntu"
   - Choisir un noyau plus ancien

2. **Vérifier les mises à jour :**
```bash
sudo apt update
sudo apt upgrade
```

3. **Annuler une mise à jour problématique :**
```bash
# Voir l'historique
apt list --installed | grep -i kernel

# Revenir à une version spécifique
sudo apt install linux-image-XXX
```

## 3. Actions immédiates si système quasi inutilisable

1. **Utiliser le terminal texte (TTY) :**
   - Ctrl+Alt+F 3 (ou F 3 à F 6)
   - Interface 100% texte, souvent plus réactive
   - Se connecter avec son compte

2. **Libérer de la mémoire d'urgence :**
```bash
# Tuer les processus les plus gourmands
ps aux --sort=-%mem | head -10
```

3. **Tester avec un nouvel utilisateur :**
```bash
# Créer un utilisateur test
sudo adduser testuser

# Lui donner droits sudo (optionnel)
sudo usermod -aG sudo testuser
```
- Se déconnecter
- Se connecter comme `testuser`
- Si tout fonctionne : problème dans votre profil utilisateur

4. **Mode sans échec :**
   - Menu GRUB au démarrage
   - "Advanced options for Ubuntu"
   - " (recovery mode)"
   - "root" ou "clean"

## 4. En dernier recours

### A. Restauration système avec Timeshift
**Si Timeshift est configuré :**
```bash
# Lancer depuis un TTY
sudo timeshift --restore
```
Choisir un snapshot datant d'avant les problèmes.

### B. Réparer paquets système
```bash
# Vérifier intégrité paquets
sudo dpkg --configure -a
sudo apt install -f

# Réinstaller bureau Ubuntu
sudo apt install --reinstall ubuntu-desktop
```

### C. Support Ubuntu Pro
1. Accéder au portail support Canonical
2. Ouvrir un ticket avec :
   - Sorties des commandes de diagnostic
   - Description détaillée du problème
   - Actions déjà tentées

### D. Sauvegarde et réinstallation
1. **Sauvegarder données importantes :**
```bash
# Monter un disque externe
sudo mkdir /mnt/backup
sudo mount /dev/sdX1 /mnt/backup

# Copier données personnelles
cp -r /home/votrenom/Documents /mnt/backup/
```

2. **Options de réinstallation :**
   - Réinstaller Ubuntu Pro en conservant les fichiers personnels
   - Installation propre après sauvegarde complète

## Commandes de synthèse rapide

```bash
# 1. Diagnostic complet
htop
free -h
df -h
journalctl --since "2 days ago" -p 3 -xb

# 2. Nettoyage de base
sudo apt autoremove --purge
sudo journalctl --vacuum-time=3d
sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches

# 3. Réparation
sudo dpkg --configure -a
sudo apt install -f
```

## Prévention future
1. **Monitoring régulier :**
   - Installer `gnome-system-monitor` pour interface graphique
   - Configurer des alertes avec `monit` ou `systemd`

2. **Maintenance programmée :**
```bash
# Script de nettoyage mensuel
sudo apt update && sudo apt upgrade
sudo apt autoremove --purge
sudo journalctl --vacuum-time=30d
```

3. **Surveillance espace disque :**
   - Garder au moins 15% d'espace libre
   - Utiliser `baobab` (Disk Usage Analyzer) régulièrement
```

---

### Pour télécharger ce fichier :

1. **Copier-coller** tout le contenu ci-dessus dans un éditeur de texte
2. **Sauvegarder** avec le nom : `depannage_ubuntu_lent. Md`
3. Ou utiliser cette commande dans le terminal :

```bash
# Créer directement le fichier
Cat > ~/Téléchargements/depannage_ubuntu_lent. Md << 'EOF'
[Coller tout le contenu du guide ici]
EOF
```

Ce guide vous permettra de suivre une méthodologie structurée pour identifier et résoudre votre problème de lenteur sur Ubuntu Pro.