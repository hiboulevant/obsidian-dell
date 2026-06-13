---
feature: thumbnails/external/e6ce08f0ba657f7f47e8a789c3aec65e.png
thumbnail: thumbnails/resized/573ea1aa02d3ac07007d28f23ff5a83b_86cf658e.webp
---
# Libéber disque dur principale
#sata #ssd #HDD

### Pourquoi vos solutions actuelles ne fonctionnent pas pour les applications :

- **Disques SATA externes :** Vous avez une grande capacité de stockage, mais les applications ne peuvent généralement pas être installées sur un disque externe de manière fiable. Le système d'exploitation, les dépendances des applications et les chemins d'accès au registre sont optimisés pour une installation locale. De plus, les performances des disques externes sont limitées par l'interface de connexion (souvent USB), ce qui les rendrait trop lents pour faire fonctionner des programmes correctement.
    
- **Google Drive :** Le cloud est un excellent endroit pour stocker des documents, des photos et des vidéos, mais il n'est pas conçu pour l'installation d'applications. Les programmes ont besoin d'un accès constant et très rapide à leurs fichiers exécutables et de données, ce qui est impossible avec le stockage en ligne, qui dépend de votre connexion Internet et de la latence.
    

### Solutions gratuites pour optimiser l'espace de votre SSD :

Puisque vous ne pouvez pas acheter de nouveau SSD, l'objectif est de maximiser l'espace libre sur votre disque principal.

1. **Identifier les plus gros fichiers :**
    
    - Utilisez des logiciels d'analyse de disque gratuits comme **WinDirStat** ou **WizTree**. Ces outils scannent votre disque et affichent une carte graphique de votre utilisation de l'espace, vous permettant de voir en un coup d'œil quels fichiers et dossiers sont les plus volumineux. C'est souvent là que se cachent les fichiers temporaires, les anciennes sauvegardes ou les téléchargements oubliés.
        
2. **Transférer les données personnelles :**
    
    - Déplacez tous vos fichiers personnels (documents, photos, vidéos, musique) qui ne sont pas essentiels au fonctionnement du système vers vos disques durs externes ou votre Google Drive. Assurez-vous que les paramètres de vos applications (par exemple, le dossier de sauvegarde de votre logiciel de montage vidéo) dirigent directement vers un disque externe.
        
3. **Nettoyer les fichiers temporaires et système :**
    
    - Utilisez l'outil de **Nettoyage de disque** de Windows. Tapez simplement "Nettoyage de disque" dans la barre de recherche du menu Démarrer, sélectionnez votre SSD, puis cliquez sur "Nettoyer les fichiers système" pour libérer de l'espace en supprimant les mises à jour Windows obsolètes, les fichiers temporaires et autres données inutiles.
        
4. **Désinstaller les logiciels inutiles :**
    
    - Passez en revue la liste des applications installées via les "Paramètres" de Windows 11 (Applications > Applications installées). Désinstallez tous les logiciels que vous n'utilisez plus.
        
5. **Modifier les emplacements d'installation par défaut :**
    
    - Pour les futures installations, certaines applications vous permettent de choisir l'emplacement. Dirigez-les vers un disque dur externe si possible. Cependant, soyez conscient que les performances seront dégradées.
        
6. **Gérer l'hibernation et la mémoire virtuelle :**
    
    - Le fichier d'hibernation (`hiberfil.sys`) et le fichier de mémoire virtuelle (`pagefile.sys`) peuvent occuper plusieurs gigaoctets. Vous pouvez les désactiver si vous n'utilisez pas l'hibernation, mais faites attention, car cela pourrait affecter la stabilité du système si votre RAM est limitée. La désactivation de l'hibernation se fait via l'Invite de commandes en mode administrateur avec la commande `powercfg.exe /hibernate off`.
        

### Une solution hybride pour vos applications : le lien symbolique

C'est une solution avancée, mais elle peut être très utile. Windows 11 permet de créer des **liens symboliques** (ou "symlinks"). C'est une méthode qui fait croire au système qu'un dossier se trouve à un endroit alors qu'il est physiquement stocké ailleurs.

- **Comment ça marche :** Vous installez votre logiciel sur le SSD, puis vous déplacez le dossier d'installation le plus volumineux (souvent "bin" ou "Data") vers un de vos disques durs externes. Ensuite, vous créez un lien symbolique qui pointe vers ce dossier sur le disque externe. Le système et le logiciel voient le dossier comme s'il était toujours sur le SSD, mais les données sont stockées sur le disque externe.
    
- **Attention :** Cette méthode est complexe, peut causer des problèmes si elle est mal exécutée et ne résoudra pas les problèmes de performance. Le logiciel fonctionnera, mais il sera aussi lent que le disque externe. Elle est mieux adaptée pour les logiciels qui n'exigent pas des temps de chargement instantanés.
    

En conclusion, la solution réside dans la gestion minutieuse de ce qui est stocké sur votre SSD. Libérez de l'espace en déplaçant tout ce qui n'est pas une application essentielle ou un fichier système vers vos disques externes, et envisagez des solutions de contournement comme les liens symboliques pour les logiciels qui consomment trop d'espace.

--- 

![Disque dur](https://web.maths.unsw.edu.au/~lafaye/CCM/pc/images/disque-dur.png)

![Définition HDD : Disque Dur Mécanique](https://d2u1z1lopyfwlx.cloudfront.net/thumbnails/187d3cfa-8323-58bd-98cc-bd4c5db79ff8/2d206665-a6e2-539f-8ef2-12841699111d.jpg)

![Disque dur hybride — Wikipédia](https://d2u1z1lopyfwlx.cloudfront.net/thumbnails/7a0de673-25ea-53c6-8873-5b4c41b104df/01a84265-e09c-5682-92ce-681c89a1afe2.jpg)

![SSD vs HDD – MicroAge Québec](https://microage.ca/quebec/wp-content/uploads/sites/56/bb-plugin/cache/hard-drive-ssd-1-landscape-358dc8fde33045be5c50638ca5660584-603ffbdade5fe.jpg)

![Disque dur HDD : tout connaître de ce support de stockage ...](https://www.macway.com/blog/wp-content/uploads/2022/03/disque-dur-hdd-composants-1024x683.jpg)

Un disque dur HDD (pour _Hard Disk Drive_) est un dispositif de stockage de données utilisant des plateaux magnétiques tournants pour lire et écrire l’information. Les HDD sont couramment utilisés dans les ordinateurs de bureau, portables, serveurs et de nombreux autres appareils nécessitant un stockage de masse non-volatile. Ils permettent de stocker des fichiers, des programmes, des systèmes d’exploitation et peuvent servir aux sauvegardes.[wikipedia+1](https://fr.wikipedia.org/wiki/Disque_dur)

## Fonctionnement

Un disque dur se compose généralement :

- D’un ou plusieurs plateaux métalliques recouverts d’une matière magnétique.
    
- D’une tête de lecture/écriture pour chaque surface de plateau.
    
- D’un moteur faisant tourner les plateaux à une vitesse constante (typiquement entre 5,400 et 7,200 tours/minute, parfois plus pour des usages professionnels).
    
- D’un bras mobile positionnant les têtes au bon endroit sur les plateaux.
    

Les données sont organisées en pistes et secteurs. L’électronique embarquée gère l’écriture, la lecture et l’interface avec l’ordinateur.[wikipedia](https://fr.wikipedia.org/wiki/Disque_dur)

## Avantages et inconvénients

- **Avantages** : Prix au gigaoctet très bas, grandes capacités (de 500Go à 20To et plus).
    
- **Inconvénients** : Plus lenteur d’accès par rapport aux SSD, bruit de fonctionnement, fragilité mécanique (chocs).
    

## Interfaces modernes

Les HDD utilisent principalement l’interface SATA (Serial ATA) sur les modèles récents, mais des interfaces plus anciennes comme IDE/PATA ou SCSI existent encore sur des matériels anciens ou spécialisés.[bestbuy+1](https://www.bestbuy.ca/fr-ca/categorie/disques-durs-internes/20239)

## Alternatives

Les SSD (Solid State Drive) fournissent de meilleures performances, sans pièce mobile, mais restent plus chers pour de grandes capacités. Il existe aussi des disques hybrides (HDD+SSD) qui associent stockage magnétique et mémoire flash pour plus de rapidité sur les fichiers souvent utilisés.[touchedeclavier](https://blog.touchedeclavier.com/differences-entre-disque-dur-hdd-ssd/)

En résumé, le disque dur HDD reste une solution de stockage économique et courante, surtout intéressante pour l’archivage ou les besoins très volumineux.[bestbuy+2](https://www.bestbuy.ca/fr-ca/categorie/disques-durs-internes/20239)

1. [https://www.bureauengros.com/collections/fr-disques-durs-internes-7246](https://www.bureauengros.com/collections/fr-disques-durs-internes-7246)
2. [https://www.bestbuy.ca/fr-ca/categorie/disques-durs-internes/20239](https://www.bestbuy.ca/fr-ca/categorie/disques-durs-internes/20239)
3. [https://www.electro-shop.ca/fr/products/disque-desktop-3-5-1-to-hdd](https://www.electro-shop.ca/fr/products/disque-desktop-3-5-1-to-hdd)
4. [https://fr.wikipedia.org/wiki/Disque_dur](https://fr.wikipedia.org/wiki/Disque_dur)
5. [https://blog.touchedeclavier.com/differences-entre-disque-dur-hdd-ssd/](https://blog.touchedeclavier.com/differences-entre-disque-dur-hdd-ssd/)
6. [https://addison-electronique.com/fr/ordinateurs-et-reseau/media-de-stockage/disques-dur.html](https://addison-electronique.com/fr/ordinateurs-et-reseau/media-de-stockage/disques-dur.html)
7. [https://www.westerndigital.com/fr-ca/products/hdd](https://www.westerndigital.com/fr-ca/products/hdd)
8. [https://www.hamster.ca/disques-durs](https://www.hamster.ca/disques-durs)
9. [https://www.coopzone.ca/produits/informatique/disques-durs-et-stockage/disques-durs-externes](https://www.coopzone.ca/produits/informatique/disques-durs-et-stockage/disques-durs-externes)