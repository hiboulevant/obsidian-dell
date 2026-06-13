### Test de surface plus poussé
Pour effectuer un test de surface plus poussé sur Ubuntu, vous pouvez utiliser les outils **smartmontools** et **badblocks**. Ces outils permettent de scanner physiquement chaque secteur du disque pour identifier ceux qui sont illisibles ou instables. \[1\]

## **1\. Test SMART Étendu (Méthode recommandée)**

C'est le test le plus fiable car il est géré directement par le micrologiciel du disque. \[2\]

* **Installation :** sudo apt install smartmontools  
* **Lancer le test :** sudo smartctl \-t long /dev/sdX (remplacez sdX par le nom de votre disque, ex: sda).  
* **Consulter le résultat :** Une fois terminé (cela peut prendre plusieurs heures), tapez : sudo smartctl \-a /dev/sdX. Cherchez la section "Self-test log" pour voir si le test a échoué. \[3\]

## **2\. Test avec l'utilitaire badblocks (Scan de surface)**

Cet outil lit chaque bloc du disque pour détecter les erreurs d'E/S (Entrée/Sortie). \[4\]

* **Test en lecture seule (Sûr pour vos données) :**  
  `sudo badblocks -sv /dev/sdX`

  * \-s : affiche la progression.  
  * \-v : mode verbeux (affiche les erreurs détectées).  
* **Interprétation :** Si badblocks affiche une liste de chiffres, ce sont les adresses des secteurs défectueux. Plus la liste est longue, plus l'état physique du disque est dégradé. \[5, 6, 7\]

## **3\. Test de lecture/écriture non destructif (Plus précis)**

Ce test écrit des données sur chaque secteur, vérifie qu'elles sont bien écrites, puis restaure vos données d'origine. C'est le test le plus complet sans effacer le disque. \[8, 9\]

* **Commande :**  
  `sudo badblocks -nsv /dev/sdX`  
  *Attention : Bien que "non destructif", une coupure de courant pendant ce test peut causer des pertes de données. Sauvegardez vos fichiers avant.* \[6\]

## **Résumé des commandes utiles**

| Commande | Objectif | Sécurité |
| :---- | :---- | :---- |
| lsblk | Identifier le nom du disque (sda, nvme0n1, etc.) | ✅ Sûr |
| smartctl \-t long | Autodiagnostic matériel complet | ✅ Sûr |
| badblocks \-sv | Scan de surface simple en lecture | ✅ Sûr |
| badblocks \-nsv | Test complet lecture/écriture | ⚠️ Risque faible |

Si l'un de ces tests confirme des erreurs supplémentaires ou si le nombre de secteurs réalloués augmente après le scan, le remplacement du disque est **impératif** pour éviter une perte de données soudaine. \[10\]

Souhaitez-vous de l'aide pour **identifier précisément le nom de votre disque** (/dev/sdX) afin de ne pas vous tromper de cible ?

\[1\] [https://www.tecmint.com](https://www.tecmint.com/check-linux-hard-disk-bad-sectors-bad-blocks/)  
\[2\] [https://www.inspq.qc.ca](https://www.inspq.qc.ca/en/node/4887)  
\[3\] [https://www.hp.com](https://www.hp.com/us-en/shop/tech-takes/how-to-check-hard-drive-health)  
\[4\] [https://lecrabeinfo.net](https://lecrabeinfo.net/tutoriels/verifier-etat-de-sante-tester-secteurs-defectueux-disque-dur-ssd-sur-linux/)  
\[5\] [https://ra1ahq.blog](https://ra1ahq.blog/en/kak-proverit-zhestkii-disk-na-bitye-sektory-ili-bady-plokhie-bloki-v-linux)  
\[6\] [https://mivocloud.com](https://translate.google.com/translate?u=https://mivocloud.com/blog/Check-badblocks&hl=fr&sl=en&tl=fr&client=sge#:~:text=V%C3%A9rification%20du%20disque%20dur%20sous%20Linux%20Vous,de%20secteurs%20d%C3%A9fectueux%20sur%20le%20disque%20dur.)  
\[7\] [https://unix.stackexchange.com](https://unix.stackexchange.com/questions/562890/how-to-check-entire-hard-disk-for-errors-and-bad-sectors)  
\[8\] [https://debian-facile.org](https://debian-facile.org/viewtopic.php?id=9608)  
\[9\] [https://wiki.archlinux.org](https://translate.google.com/translate?u=https://wiki.archlinux.org/title/Badblocks&hl=fr&sl=en&tl=fr&client=sge#:~:text=Test%20en%20mode%20%C3%A9criture.%20Attention%20:%20les,sont%20ex%C3%A9cut%C3%A9s%20et%20ne%20peuvent%20%C3%AAtre%20r%C3%A9cup%C3%A9r%C3%A9es.)  
\[10\] [https://forum.ubuntu-fr.org](https://forum.ubuntu-fr.org/viewtopic.php?id=2080895)