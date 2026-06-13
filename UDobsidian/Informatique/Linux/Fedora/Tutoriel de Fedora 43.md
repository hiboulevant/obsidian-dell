# Tutoriel de Fedora 43

### Tutoriel pour Fedora 43 : Guide du débutant

Bonjour ! Fedora 43 est la version stable de Fedora Linux sortie le 28 octobre 2025. C'est une distribution open source moderne, basée sur GNOME par défaut (pour l'édition Workstation), idéale pour les débutants comme les utilisateurs avancés. Ce tutoriel est un guide complet pour installer, configurer et utiliser Fedora 43. Il s'appuie sur la documentation officielle et des ressources communautaires. Si vous êtes nouveau sous Linux, pas de panique : on va y aller étape par étape.

**Prérequis :**

- Un ordinateur avec au moins 2 Go de RAM (4 Go recommandés), 20 Go d'espace disque, et une connexion internet.
- Fedora est gratuit : téléchargez-le depuis [fedoraproject.org](https://fedoraproject.org/fr/workstation/download/).

#### 1. Installation de Fedora 43

L'installation est simple et graphique via Anaconda (l'installateur de Fedora). Elle prend environ 15-30 minutes.

**Étapes clés :**

1. **Téléchargez l'ISO** : Allez sur [getfedora.org](https://getfedora.org/fr/workstation/download) et choisissez l'édition Workstation (GNOME) pour un usage desktop standard. Vérifiez l'intégrité du fichier avec SHA256 (instructions sur le site).
2. **Créez une clé USB bootable** : Utilisez un outil comme Rufus (Windows), Etcher (multiplateforme) ou dd sous Linux :
    
    text
    
    ```
    sudo dd if=Fedora-Workstation-Live-x86_64-43.iso of=/dev/sdX bs=4M status=progress && sync
    ```
    
    (Remplacez /dev/sdX par votre clé USB ; vérifiez avec lsblk.)
3. **Démarrez sur la clé USB** : Redémarrez votre PC, entrez dans le BIOS (généralement F2, F10 ou Del) et sélectionnez le boot USB. Choisissez "Start Fedora-Workstation-Live 43".
4. **Lancez l'installateur** : Dans l'environnement live, cliquez sur "Install to Hard Drive".
5. **Configuration** :
    - **Langue et clavier** : Sélectionnez français (ou votre préférence).
    - **Réseau** : Connectez-vous au Wi-Fi si besoin.
    - **Destination** : Choisissez votre disque. Pour un dual-boot avec Windows, Fedora détecte automatiquement l'espace libre. Créez des partitions automatiques (/ pour root, swap pour mémoire, /home pour données).
    - **Utilisateur** : Créez un compte non-root (sécurité). Activez l'authentification automatique si vous voulez.
6. **Terminez** : Cliquez sur "Begin Installation". Une fois fini, redémarrez et retirez la clé USB.

**Astuces** : Si vous avez un GPU NVIDIA, activez les pilotes tiers pendant l'installation. Pour un dual-boot, sauvegardez vos données avant.

Pour plus de détails, consultez le [Guide d'installation officiel](https://docs.fedoraproject.org/en-US/fedora/f43/getting-started/).

#### 2. Premiers pas après l'installation (Day 1)

Une fois installé, Fedora est prêt à l'emploi. Le bureau GNOME est intuitif, avec un menu en haut à gauche (clic sur "Activités").

**Étapes essentielles :**

1. **Mise à jour du système** : Ouvrez un terminal (Ctrl + Alt + T) et tapez :
    
    text
    
    ```
    sudo dnf update -y
    ```
    
    Redémarrez si demandé. Cela installe les derniers correctifs (Fedora 43 reçoit des mises à jour fréquentes).
2. **Activer les dépôts tiers (RPM Fusion)** : Pour des codecs multimédia, Steam ou Discord (logiciels non libres) :
    
    text
    
    ```
    sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-43.noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-43.noarch.rpm
    sudo dnf update
    ```
    
    Installez les codecs : sudo dnf groupupdate multimedia --with-optional.
3. **Installer des applications de base** : Utilisez GNOME Software (icône panier) ou le terminal :
    - Navigateur : Firefox est préinstallé ; pour Chrome : sudo dnf install google-chrome-stable.
    - Lecteur multimédia : sudo dnf install vlc.
    - Éditeur : sudo dnf install gimp inkscape.
    - Autres : sudo dnf install flatpak puis flatpak install flathub org.libreoffice.LibreOffice.
4. **Configurer le Wi-Fi et Bluetooth** : Dans les Paramètres (icône en haut à droite) > Réseau/Bluetooth.
5. **Mises à jour firmware** : sudo fwupdmgr refresh && sudo fwupdmgr update.

**Interface GNOME** : Personnalisez avec Extensions (installez via sudo dnf install gnome-tweaks gnome-extensions-app). Ajoutez Dash to Dock pour une barre des tâches.

#### 3. Utilisation basique : Le quotidien

Fedora est convivial, mais voici les bases pour naviguer.

**Bureau et navigation :**

- **Menu** : Clic sur "Activités" pour chercher apps/fichiers.
- **Terminal** : Essentiel pour les pros. Exemples :
    - Lister fichiers : ls -la.
    - Installer logiciel : sudo dnf install paquet.
    - Voir logs : journalctl -f (suivi en temps réel).
- **Gestion des fichiers** : Nautilus (Explorateur) pour copier/déplacer.

**Sécurité et utilisateurs :**

- Utilisez sudo pour les commandes admin (ex. : sudo reboot).
- Le root est désactivé par défaut : bonne pratique !
- Firewall : Activé par défaut ; configurez avec sudo firewall-cmd.

**Ressources apprentissage :**

- [Premier orientation pour débutants](https://docs.fedoraproject.org/en-US/quick-docs/getting-started-guide/) : Vocabulaire Linux de base.
- YouTube : Cherchez "Fedora 43 first look" pour des vidéos visuelles.

#### 4. Configuration avancée (Day 2+)

**Post-install tweaks (inspiré de guides communautaires) :**

1. **Pilotes NVIDIA** (si applicable) :
    
    text
    
    ```
    sudo dnf install akmod-nvidia
    ```
    
    Attendez 5-10 min après redémarrage pour que le module se compile : modinfo -F version nvidia.
2. **Batterie laptop** : Installez TLP si power-profiles-daemon ne suffit pas : sudo dnf install tlp tlp-rdw && sudo tlp start.
3. **Thèmes et extensions** : sudo dnf install gnome-tweaks pour dark mode, etc.
4. **Virtualisation** : sudo dnf install @virtualization pour KVM/VirtualBox.
5. **Sauvegarde** : Utilisez Timeshift : sudo dnf install timeshift.

**Mise à niveau** : Pour passer à Fedora 44 plus tard : sudo dnf install dnf-plugin-system-upgrade && sudo dnf system-upgrade download --releasever=44.

#### 5. Dépannage et aide

- **Erreurs courantes** : Vérifiez les logs avec dmesg ou journalctl -b.
- **Communauté** :
    - [Ask Fedora](https://discussion.fedoraproject.org/c/ask/6) : Forum en français/anglais.
    - Reddit : r/Fedora ou r/linux4noobs.
    - Chat : #fedora sur Matrix.
- **Notes de version** : Lisez-les pour les nouveautés (ex. : améliorations GNOME 47, support hardware récent).

Fedora est stable et innovant – profitez-en pour explorer ! Si vous avez une question spécifique (ex. : gaming, dev), dites-le-moi. Pour contribuer, rejoignez la communauté via [Join Fedora](https://docs.fedoraproject.org/en-US/fedora/f43/project/join/). Bonne découverte ! 🦉