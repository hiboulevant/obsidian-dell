---
tags:
  - commandedu
  - copmmandedf
  - stockage
  - serveur
commandes:
---
# Commande Fedora
 
 Bios:

 **UEFI** (**U**nified **E**xtended **F**irmware **I**nterface)
 Pour savoir ce que vous utilisez, la commande suivante vous retournera soit **BIOS**, soit **UEFI** :
 
 [ -d /sys/firmware/efi ] && echo UEFI || echo BIOS
 UEFI

- **Dans le cas de Fedora, ce chargeur de démarrage est GRUB2. Pour cette brève introduction, disons que c’est lui qui s'occupe de charger et de lancer le noyau du système d’exploitation cible.**
-  **GRUB2** permet à l’utilisateur de choisir éventuellement le système à lancer et cela selon deux manières :

1. en présentant à l’utilisateur un menu dont chacune des lignes correspond à l’exécution d’une commande de démarrage pré-établie d’un système donné ;
2. en offrant à l’utilisateur un interpréteur de commandes pour lui permettre de démarrer le système de son choix à l’aide d’une commande personnalisée.
3. 
 

 [Mise à jour]( https://docs.fedoraproject.org/fr/quick-docs/upgrading-fedora-offline/#sect-performing-system-upgrade )

----- 

###   **Commandes de base** du terminal Linux, valables sur **Fedora 43** (sortie en octobre 2025),


Ces commandes sont standards sur toutes les distributions Linux modernes, y compris Fedora, qui utilise le gestionnaire de paquets **dnf**.

Je les ai classées par catégories pour plus de clarté, avec une brève description et des exemples.

### Navigation et gestion des fichiers/répertoires
- **pwd** → Affiche le répertoire courant.  
  Exemple : `pwd`
- **ls** → Liste les fichiers et dossiers.  
  Exemples : `ls`, `ls -l` (détails), `ls -a` (fichiers cachés), `ls -lh` (tailles lisibles).
- **cd** → Change de répertoire.  
  Exemples : `cd /home`, `cd ..` (remonter), `cd ~` (dossier personnel), `cd -` (retour précédent).
- **mkdir** → Crée un dossier.  
  Exemple : `mkdir nouveau_dossier`
- **rmdir** → Supprime un dossier vide.  
  Exemple : `rmdir dossier_vide`
- **touch** → Crée un fichier vide ou met à jour la date.  
  Exemple : `touch nouveau_fichier.txt`
- **cp** → Copie fichiers/dossiers.  
  Exemple : `cp fichier.txt /destination/`, `cp -r dossier/ /destination/` (récursif).
- **mv** → Déplace ou renomme.  
  Exemple : `mv ancien.txt nouveau.txt`, `mv fichier.txt /destination/`
- **rm** → Supprime fichiers/dossiers.  
  Exemple : `rm fichier.txt`, `rm -r dossier/` (récursif, attention !).

### Affichage et manipulation de contenu
- **cat** → Affiche le contenu d'un fichier.  
  Exemple : `cat fichier.txt`
- **less** → Affiche un fichier page par page.  
  Exemple : `less fichier.txt` (q pour quitter)
- **head** → Affiche les premières lignes.  
  Exemple : `head -n 10 fichier.txt`
- **tail** → Affiche les dernières lignes.  
  Exemple : `tail -n 10 fichier.txt`, `tail -f log.txt` (suivi en temps réel)
- **grep** → Recherche dans des fichiers.  
  Exemple : `grep "mot" fichier.txt`

### Gestion des paquets (spécifique à Fedora)
- **dnf search** → Recherche un paquet.  
  Exemple : `dnf search nom_paquet`
- **dnf install** → Installe un paquet.  
  Exemple : `sudo dnf install nom_paquet`
- **dnf update** → Met à jour le système.  
  Exemple : `sudo dnf update`
- **dnf remove** → Supprime un paquet.  
  Exemple : `sudo dnf remove nom_paquet`
- **dnf autoremove** → Supprime les paquets inutiles.

### Informations système
- **uname -a** → Infos sur le système/kernel.
- **df -h** → Espace disque disponible (format lisible).
- **free -h** → Mémoire disponible.
- **du -sh dossier** → Taille d'un dossier.
- **top** ou **htop** → Surveillance des processus (htop à installer si besoin).
- **ps aux** → Liste des processus
- .
- ## Recherche et informations

| Commande                    | Description                            |
| --------------------------- | -------------------------------------- |
| `find [chemin] -name [nom]` | Rechercher des fichiers                |
| `grep [motif] [fichier]`    | Rechercher du texte                    |
| `locate [fichier]`          | Trouver rapidement un fichier          |
| `which [commande]`          | Localiser une commande                 |
| `stat [fichier]`            | Informations détaillées sur un fichier |
| `file [fichier]`            | Déterminer le type de fichier          |
||Description|
|---|---|
|`ps aux`|Lister tous les processus|
|`top` ou `htop`|Moniteur de processus interactif|
|`kill [PID]`|Terminer un processus|
|`systemctl start [service]`|Démarrer un service|
|`systemctl stop [service]`|Arrêter un service|
|`systemctl status [service]`|État d'un service|
|`journalctl -xe`|Voir les logs système|
|`uname -a`|Informations sur le noyau|
|`neofetch`|Afficher des infos système stylisées|

---

## 📦 **Gestion des paquets (DNF - Fedora)**

| Commande                    | Description                    |
| --------------------------- | ------------------------------ |
| `sudo dnf update`           | Mettre à jour tous les paquets |
| `sudo dnf install [paquet]` | Installer un paquet            |
| `sudo dnf remove [paquet]`  | Supprimer un paquet            |
| `sudo dnf search [mot]`     | Rechercher un paquet           |
| `sudo dnf info [paquet]`    | Infos sur un paquet            |
| `rpm -qi [paquet]`          | Infos sur un paquet RPM        |
| `flatpak install [app]`     | Installer une app Flatpak      |

---

## 👥 **Utilisateurs et permissions**

|Commande|Description|
|---|---|
|`sudo [commande]`|Exécuter en superutilisateur|
|`su - [utilisateur]`|Changer d'utilisateur|
|`chmod [droits] [fichier]`|Modifier les permissions|
|`chown [user]:[group] [fichier]`|Changer propriétaire/groupe|
|`id`|Afficher les identifiants de l'utilisateur|
|`passwd`|Changer son mot de passe|

---

## 🌐 **Réseau**

|Commande|Description|
|---|---|
|`ip addr` ou `ip a`|Afficher les interfaces réseau|
|`ping [hôte]`|Tester la connectivité|
|`curl [URL]`|Télécharger depuis le web|
|`wget [URL]`|Télécharger un fichier|
|`ss -tulpn`|Ports en écoute|
|`nmcli`|Gestionnaire réseau en CLI|

---

## 💾 **Disques et espace**

|Commande|Description|
|---|---|
|`df -h`|Espace disque disponible|
|`du -sh [répertoire]`|Taille d'un répertoire|
|`lsblk`|Liste des périphériques de bloc|
|`mount` / `umount`|Monter/démonter un système de fichiers|

---

## 🛠️ **Utilitaires divers**

|Commande|Description|
|---|---|
|`history`|Historique des commandes|
|`man [commande]`|Manuel d'une commande|
|`tar -czf [archive.tar.gz] [dossier]`|Créer une archive|
|`tar -xzf [archive.tar.gz]`|Extraire une archive|
|`date`|Afficher date/heure|
|`alias`|Lister les alias|

---

## 🔧 **Spécifique Fedora**

|Commande|Description|
|---|---|
|`fedora-upgrade`|Mettre à niveau vers nouvelle version|
|`rpm-ostree`|Pour les versions Silverblue/Kinoite|
|`dnf history`|Historique des transactions DNF|
## 📊 **Processus et système**

|Commande|Description|
|---|---|
|`ps aux`|Lister tous les processus|
|`top` ou `htop`|Moniteur de processus interactif|
|`kill [PID]`|Terminer un processus|
|`systemctl start [service]`|Démarrer un service|
|`systemctl stop [service]`|Arrêter un service|
|`systemctl status [service]`|État d'un service|
|`journalctl -xe`|Voir les logs système|
|`uname -a`|Informations sur le noyau|
|`neofetch`|Afficher des infos système stylisées|

---

---

**Astuce** : Pour obtenir de l'aide sur une commande :

bash

man [commande]
[commande] --help
tldr [commande]  # si installé

  

|Commande|Description|
|---|---|
|`sudo dnf update`|Mettre à jour tous les paquets|
|`sudo dnf install [paquet]`|Installer un paquet|
|`sudo dnf remove [paquet]`|Supprimer un paquet|
|`sudo dnf search [mot]`|Rechercher un paquet|
|`sudo dnf info [paquet]`|Infos sur un paquet|
|`rpm -qi [paquet]`|Infos sur un paquet RPM|
|`flatpak install [app]`|Installer une app Flatpak|

---

## 👥 **Utilisateurs et permissions**

|Commande|Description|
|---|---|
|`sudo [commande]`|Exécuter en superutilisateur|
|`su - [utilisateur]`|Changer d'utilisateur|
|`chmod [droits] [fichier]`|Modifier les permissions|
|`chown [user]:[group] [fichier]`|Changer propriétaire/groupe|
|`id`|Afficher les identifiants de l'utilisateur|
|`passwd`|Changer son mot de passe|

---

## 🌐 **Réseau**

|Commande|Description|
|---|---|
|`ip addr` ou `ip a`|Afficher les interfaces réseau|
|`ping [hôte]`|Tester la connectivité|
|`curl [URL]`|Télécharger depuis le web|
|`wget [URL]`|Télécharger un fichier|
|`ss -tulpn`|Ports en écoute|
|`nmcli`|Gestionnaire réseau en CLI|

---

## 💾 **Disques et espace**

|Commande|Description|
|---|---|
|`df -h`|Espace disque disponible|
|`du -sh [répertoire]`|Taille d'un répertoire|
|`lsblk`|Liste des périphériques de bloc|
|`mount` / `umount`|Monter/démonter un système de fichiers|

---

## 🛠️ **Utilitaires divers**

|Commande|Description|
|---|---|
|`history`|Historique des commandes|
|`man [commande]`|Manuel d'une commande|
|`tar -czf [archive.tar.gz] [dossier]`|Créer une archive|
|`tar -xzf [archive.tar.gz]`|Extraire une archive|
|`date`|Afficher date/heure|
|`alias`|Lister les alias|

---

## 🔧 **Spécifique Fedora**

|Commande|Description|
|---|---|
|`fedora-upgrade`|Mettre à niveau vers nouvelle version|
|`rpm-ostree`|Pour les versions Silverblue/Kinoite|
|`dnf history`|Historique des transactions DNF|

---

**Astuce** : Pour obtenir de l'aide sur une commande :

bash

man [commande]  
[commande] --help  
tldr [commande]  # si installé

Ces commandes fonctionneront sur n'importe quelle version récente de Fedora. Si vous débutez, je vous recommande de commencer par `ls`, `cd`, `pwd`, `cat`, et `sudo dnf install`.

Ces commandes fonctionneront sur n'importe quelle version récente de Fedora. Si vous débutez, je vous recommande de commencer par `ls`, `cd`, `pwd`, `cat`, et `sudo dnf install`.
### Permissions et utilisateurs
- **chmod** → Change les permissions.  
  Exemple : `chmod 755 fichier` (exécutable)
- **chown** → Change le propriétaire.  
  Exemple : `sudo chown user:group fichier`
- **sudo** → Exécute en administrateur.  
  Exemple : `sudo commande`
- **whoami** → Affiche l'utilisateur courant.

### Autres utiles
- **man** → Manuel d'une commande.  
  Exemple : `man ls`
- **clear** → Efface l'écran du terminal.
- **history** → Historique des commandes.
- **shutdown** → Éteint/redémarre.  
  Exemple : `sudo shutdown -h now` (éteindre), `sudo shutdown -r now` (redémarrer).

Ces commandes forment la base pour débuter. Pour plus de détails sur une commande, utilise `man nom_commande` ou `nom_commande --help`.

Si tu as besoin d'exemples plus spécifiques ou d'une catégorie particulière, dis-le-moi ! 😊