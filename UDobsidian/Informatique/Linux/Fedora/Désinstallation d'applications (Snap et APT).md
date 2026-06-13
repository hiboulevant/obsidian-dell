---
tags:
  - list/snap
  - list/apt
  - linux
  - "#remove"
---
# Désinstallation d'applications (Snap et APT)


### Lister les applications Snap installées
```bash
snap list
```

### Désinstaller une application Snap
```bash
sudo snap remove nom_du_paquet
```

### Désinstaller complètement (avec les données de configuration)
```bash
sudo snap remove --purge nom_du_paquet
```

## Désinstaller une application APT

### Lister les applications APT installées
```bash
apt list --installed
```
Ou
```bash
dpkg -l
```

### Désinstaller une application APT

**Option 1 : Supprimer le paquet (conserve les fichiers de configuration)**
```bash
sudo apt remove nom_du_paquet
```

**Option 2 : Supprimer complètement (avec les fichiers de configuration)**
```bash
sudo apt purge nom_du_paquet
```

**Option 3 : Supprimer et nettoyer les dépendances inutilisées**
```bash
sudo apt autoremove nom_du_paquet
```

## Exemples pratiques

```bash
# Désinstaller Firefox (Snap)
sudo snap remove firefox

# Désinstaller VLC (APT) avec purge
sudo apt purge vlc
sudo apt autoremove
```

## Rechercher une application spécifique

Si vous ne connaissez pas le nom exact du paquet :

```bash
# Pour Snap
snap list | grep -i "nom"

# Pour APT
apt list --installed | grep -i "nom"
dpkg -l | grep -i "nom"
```

**Remarque** : Remplacez `nom_du_paquet` par le nom réel de l'application que vous souhaitez désinstaller.# Désinstallation d'applications dans Ubuntu (Snap et APT)

## Désinstaller une application Snap

### Lister les applications Snap installées
```bash
snap list
```

### Désinstaller une application Snap
```bash
sudo snap remove nom_du_paquet
```

### Désinstaller complètement (avec les données de configuration)
```bash
sudo snap remove --purge nom_du_paquet
```

## Désinstaller une application APT

### Lister les applications APT installées
```bash
apt list --installed
```
Ou
```bash
dpkg -l
```

### Désinstaller une application APT

**Option 1 : Supprimer le paquet (conserve les fichiers de configuration)**
```bash
sudo apt remove nom_du_paquet
```

**Option 2 : Supprimer complètement (avec les fichiers de configuration)**
```bash
sudo apt purge nom_du_paquet
```

**Option 3 : Supprimer et nettoyer les dépendances inutilisées**
```bash
sudo apt autoremove nom_du_paquet
```

## Exemples pratiques

```bash
# Désinstaller Firefox (Snap)
sudo snap remove firefox

## Désinstallation d'applications dans Ubuntu (Snap et APT)

## Désinstaller une application Snap

### Lister les applications Snap installées
```bash
snap list
```

### Désinstaller une application Snap
```bash
sudo snap remove nom_du_paquet
```

### Désinstaller complètement (avec les données de configuration)
```bash
sudo snap remove --purge nom_du_paquet
```

## Désinstaller une application APT

### Lister les applications APT installées
```bash
apt list --installed
```
ou
```bash
dpkg -l
```

### Désinstaller une application APT

**Option 1 : Supprimer le paquet (conserve les fichiers de configuration)**
```bash
sudo apt remove nom_du_paquet
```

**Option 2 : Supprimer complètement (avec les fichiers de configuration)**
```bash
sudo apt purge nom_du_paquet
```

**Option 3 : Supprimer et nettoyer les dépendances inutilisées**
```bash
sudo apt autoremove nom_du_paquet
```

## Exemples pratiques

```bash
# Désinstaller Firefox (Snap)
sudo snap remove firefox

# Désinstaller VLC (APT) avec purge
sudo apt purge vlc
sudo apt autoremove
```

## Rechercher une application spécifique

Si vous ne connaissez pas le nom exact du paquet :

```bash
# Pour Snap
snap list | grep -i "nom"

# Pour APT
apt list --installed | grep -i "nom"
dpkg -l | grep -i "nom"
```

**Remarque** : Remplacez `nom_du_paquet` par le nom réel de l'application que vous souhaitez désinstaller.# Désinstallation d'applications dans Ubuntu (Snap et APT)

## Désinstaller une application Snap

### Lister les applications Snap installées
```bash
snap list
```

### Désinstaller une application Snap
```bash
sudo snap remove nom_du_paquet
```

### Désinstaller complètement (avec les données de configuration)
```bash
sudo snap remove --purge nom_du_paquet
```

## Désinstaller une application APT

### Lister les applications APT installées
```bash
apt list --installed
```
Ou
```bash
dpkg -l
```

### Désinstaller une application APT

**Option 1 : Supprimer le paquet (conserve les fichiers de configuration)**
```bash
sudo apt remove nom_du_paquet
```

**Option 2 : Supprimer complètement (avec les fichiers de configuration)**
```bash
sudo apt purge nom_du_paquet
```

**Option 3 : Supprimer et nettoyer les dépendances inutilisées**
```bash
sudo apt autoremove nom_du_paquet
```

## Exemples pratiques

```bash
# Désinstaller Firefox (Snap)
sudo snap remove firefox

# Désinstaller VLC (APT) avec purge
sudo apt purge vlc
sudo apt autoremove
```

## Rechercher une application spécifique

Si vous ne connaissez pas le nom exact du paquet :

```bash
# Pour Snap
snap list | grep -i "nom"

# Pour APT
apt list --installed | grep -i "nom"
dpkg -l | grep -i "nom"
```

**Remarque** : Remplacez `nom_du_paquet` par le nom réel de l'application que vous souhaitez désinstaller.# Désinstallation d'applications dans Ubuntu (Snap et APT)

## Désinstaller une application Snap

### Lister les applications Snap installées
```bash
snap list
```

### Désinstaller une application Snap
```bash
sudo snap remove nom_du_paquet
```

### Désinstaller complètement (avec les données de configuration)
```bash
sudo snap remove --purge nom_du_paquet
```

## Désinstaller une application APT

### Lister les applications APT installées
```bash
apt list --installed
```
Ou
```bash
dpkg -l
```

### Désinstaller une application APT

**Option 1 : Supprimer le paquet (conserve les fichiers de configuration)**
```bash
sudo apt remove nom_du_paquet
```

**Option 2 : Supprimer complètement (avec les fichiers de configuration)**
```bash
sudo apt purge nom_du_paquet
```

**Option 3 : Supprimer et nettoyer les dépendances inutilisées**
```bash
sudo apt autoremove nom_du_paquet
```

## Exemples pratiques

```bash
# Désinstaller Firefox (Snap)
sudo snap remove firefox

# Désinstaller VLC (APT) avec purge
sudo apt purge vlc
sudo apt autoremove
```

## Rechercher une application spécifique

Si vous ne connaissez pas le nom exact du paquet :

```bash
# Pour Snap
snap list | grep -i "nom"

# Pour APT
apt list --installed | grep -i "nom"
dpkg -l | grep -i "nom"
```

**Remarque** : Remplacez `nom_du_paquet` par le nom réel de l'application que vous souhaitez désinstaller. Désinstaller VLC (APT) avec purge
sudo apt purge vlc
sudo apt autoremove
```

## Rechercher une application spécifique

Si vous ne connaissez pas le nom exact du paquet :

```bash
# Pour Snap
snap list | grep -i "nom"

# Pour APT
apt list --installed | grep -i "nom"
dpkg -l | grep -i "nom"
```

**Remarque** : Remplacez `nom_du_paquet` par le nom réel de l'application que vous souhaitez désinstaller.