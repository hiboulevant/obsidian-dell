# Fedora 43 (commande)

#terminal #commande #Linux #fedora

Princpale commande de terminal de Fedora 43

### Liste des commandes essentielles de terminal pour Fedora 43

Fedora 43 utilise le gestionnaire de paquets **DNF** (successeur de YUM) et des outils standards Linux comme Bash pour le shell. Il n'existe pas de "liste exhaustive" de toutes les commandes, car Linux en compte des milliers, mais voici une sélection des commandes les plus essentielles et couramment utilisées en terminal. Elles sont organisées par catégories pour plus de clarté. Ces commandes sont universelles pour les distributions Linux, mais adaptées au contexte de Fedora (par exemple, pas d'APT comme sur Ubuntu).

Pour ouvrir un terminal sur Fedora : Recherchez "Terminal" dans le menu GNOME (ou utilisez le raccourci **Ctrl + Alt + T**).

**Conseils généraux :**

- Utilisez man commande (ex. : man ls) pour afficher l'aide détaillée d'une commande.
- Pour les opérations système, préfixez avec sudo (ex. : sudo dnf update) et entrez votre mot de passe utilisateur.
- exit ferme la session terminal.

#### 1. Navigation et gestion des fichiers

Ces commandes permettent de se déplacer dans le système de fichiers et de manipuler les dossiers/fichiers.

|Commande|Description|Exemple|
|---|---|---|
|ls|Liste le contenu du répertoire courant. Options : -l (détails), -a (fichiers cachés).|ls -la|
|cd|Change de répertoire. ~ = dossier personnel, .. = parent.|cd Documents ou cd ~|
|pwd|Affiche le chemin du répertoire courant.|pwd|
|mkdir|Crée un nouveau répertoire.|sudo mkdir nouveau_dossier|
|rmdir|Supprime un répertoire vide.|rmdir vide|
|touch|Crée un fichier vide ou met à jour la date d'un fichier.|touch fichier.txt|
|cp|Copie un fichier/répertoire.|cp fichier.txt /tmp/|
|mv|Déplace ou renomme un fichier/répertoire.|mv ancien.txt nouveau.txt|
|rm|Supprime un fichier/répertoire. Attention : irréversible ! Options : -r (récursif).|rm fichier.txt ou rm -r dossier/|
|find|Recherche des fichiers/répertoires.|find /home -name "*.txt"|

#### 2. Affichage et édition de fichiers

Pour visualiser ou modifier du contenu texte.

|Commande|Description|Exemple|
|---|---|---|
|cat|Affiche le contenu d'un fichier.|cat fichier.txt|
|less|Affiche un fichier page par page (utilisez q pour quitter).|less long_fichier.log|
|head|Affiche les premières lignes d'un fichier. Option : -n 10.|head -n 5 fichier.txt|
|tail|Affiche les dernières lignes. Option : -f (suivi en temps réel).|tail -f /var/log/messages|
|nano|Éditeur de texte simple (recommandé pour débutants).|nano config.txt|
|vim|Éditeur avancé (i pour insérer, :wq pour sauvegarder/quitter).|vim fichier.txt|
|grep|Recherche un motif dans un fichier.|grep "erreur" log.txt|

#### 3. Gestion des paquets (DNF sur Fedora)

Fedora utilise DNF pour installer, mettre à jour et supprimer des logiciels.

|Commande|Description|Exemple|
|---|---|---|
|dnf update|Met à jour tous les paquets installés.|sudo dnf update|
|dnf upgrade|Alias de update (met à jour le système).|sudo dnf upgrade|
|dnf install|Installe un paquet.|sudo dnf install vim|
|dnf remove|Supprime un paquet.|sudo dnf remove paquet_inutile|
|dnf search|Recherche un paquet.|dnf search navigateur|
|dnf list installed|Liste les paquets installés.|dnf list installed|
|dnf info|Affiche des infos sur un paquet.|dnf info firefox|
|dnf autoremove|Supprime les paquets inutiles (dépendances orphelines).|sudo dnf autoremove|

#### 4. Gestion du système et des processus

Pour monitorer et contrôler le système.

|Commande|Description|Exemple|
|---|---|---|
|sudo|Exécute une commande en tant qu'administrateur.|sudo systemctl restart service|
|su|Passe en root (utilisez su - pour un environnement complet).|su -|
|top|Affiche les processus en temps réel (q pour quitter).|top|
|htop|Version améliorée de top (installez-le avec sudo dnf install htop).|htop|
|ps|Liste les processus. Option : aux (tous).|ps aux \| grep firefox|
|kill|Termine un processus par PID.|kill 1234|
|systemctl|Gère les services (start, stop, status).|sudo systemctl status httpd|
|df -h|Affiche l'espace disque (humain lisible).|df -h|
|du -sh|Taille d'un répertoire.|du -sh /home|
|free -h|Mémoire RAM disponible.|free -h|
|uptime|Temps de fonctionnement du système.|uptime|

#### 5. Réseau et connexions

Pour diagnostiquer et gérer le réseau.

|Commande|Description|Exemple|
|---|---|---|
|ping|Teste la connectivité.|ping google.com|
|ip addr|Affiche les adresses IP (remplace ifconfig).|ip addr show|
|ss|Liste les connexions réseau (remplace netstat).|ss -tuln|
|curl|Télécharge ou teste une URL.|curl https://example.com|
|wget|Télécharge un fichier.|wget https://exemple.com/fichier.tar.gz|
|ssh|Connexion sécurisée à un serveur distant.|ssh user@ip_serveur|

#### 6. Utilitaires avancés et compression

Pour les tâches courantes comme l'archivage.

|Commande|Description|Exemple|
|---|---|---|
|tar|Archive/comprime des fichiers. Options : -czvf (gzip), -xjvf (bzip2).|tar -czvf archive.tar.gz dossier/|
|history|Liste les commandes précédentes.|history \| grep dnf|
|alias|Crée un raccourci pour une commande (ajoutez dans ~/.bashrc).|alias ll='ls -la'|
|screen|Crée une session terminal persistante.|screen -S session (Ctrl+A D pour détacher)|

Ces commandes couvrent 80 % des besoins quotidiens. Pour Fedora 43 spécifiquement, assurez-vous que votre système est à jour avec sudo dnf update avant d'installer quoi que ce soit. Si vous avez besoin d'exemples plus détaillés ou d'une catégorie spécifique (ex. : scripting), précisez ! Pour une liste plus technique, consultez man ou les docs officielles de Fedora.