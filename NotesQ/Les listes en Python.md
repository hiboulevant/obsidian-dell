---
tags:
  - python
  - liste/python
  - Informatique
---
# Les listes en Python
Les listes font parties des quatre grandes **structures de données** qui existent en Python en plus des **sets** , des **tuples** et des **dictionnaires**.

C'est un objet très pratique, aussi bien pour les développeurs débutants que pour ceux plus expérimentés.

Une liste est simplement une structure de données [**muable**](https://www.docstring.fr/glossaire/muable/) et **ordonnée** dans laquelle tu peux stocker **n'importe quel type d'objet**.

Chaque objet contenu dans une liste est appelé un **élément**.

Pour créer une liste, tu dois placer ces éléments entre des crochets et les séparer par une virgule.

On accède aux éléments d'une liste grâce à leur **indice** , c'est-à-dire leur position dans la liste.

Enfin, et c'est vraiment le plus intéressant, une liste est une **séquence de données** ! Cela signifie que tu peux **itérer** sur cette séquence, avec une boucle `for` par exemple.

## [Une liste est ordonnée](https://www.docstring.fr/glossaire/liste/?utm_source=udemy&utm_campaign=glossary-listes#une-liste-est-ordonnee)

C'est important que tu retiennes bien qu'une liste est ordonnée car ce n'est pas le cas de toutes les structures de données en Python.

Dans tous les cas, cela signifie simplement que les éléments de ta liste seront toujours dans l'ordre que tu auras défini dans ton code.

Il n'y a pas d'histoire d'ordre alphabétique ou quoi que ce soit, c'est toi qui décides !

# liste vide
villes = [] 

# liste avec trois items de type str
villes = ['Paris', 'Lille', 'Lyon']
print(villes)


