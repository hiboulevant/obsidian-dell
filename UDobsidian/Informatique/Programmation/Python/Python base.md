---
tags:
  - pythonbase
  - typenatif
---
# Python base


# Les différents types natifs

Ce qu'on appelle les types natifs, ce sont des types de données préexistants qui vous permettent en programmation de représenter tout ce dont vous avez besoin.

Il existe plusieurs types natifs comme les chaînes de caractères (qui sont en fait tout simplement du texte), les nombres et les booléens (qui vont nous permettre de travailler par la suite avec des conditions).

Il existe d'autres types natifs qui peuvent être construits à partir de ces trois types de base.

👉 On retrouve par exemple les _listes_ et les _tuples_ qui nous permettent de représenter une séquence de différents éléments (`[1, 2, 3, 4]`).

👉 Les types d'ensembles comme les _sets_ et _frozen set_, qui permettent de réaliser des opérations d'union, de différences ou encore d'intersection

👉 Les types de correspondances avec les _dictionnaires_, qui sont un autre moyen d'organiser des données avec un système de clés et de valeurs.

Dans les prochaines parties, on va s'intéresser aux types natifs de base que sont _les chaînes de caractères_, _les nombres_ et _les booléens_.

Les autres types natifs que je viens d'énoncer sont un peu plus complexes et disposent de formations qui leur sont entièrement dédiés et ce ne sont finalement que des façons d'organiser et d'agencer dans d'autres structures ces trois types natifs de base que l'on va voir dans les prochaines parties.

# Les nombres entiers:
1.  -5 , 230
2. Depuis la version 3.6 on peut mettre des tirets sans problèmes. 
   1000000
   1_000_000
# Les nombres décimaux (flottants) [^1]
1.45, 150,87 10,0
   

[^1]: Dès qu'il y a un point.  Le nombre même s'il est entier est considéré comme décimal.

# Les booléans
Un booléan est un objet que ne peut prendre que deux valeurs: Frue ou False [^2]
Issubclass (bool, int)
True
Ainsi on obtient:
True + 1 = 2
False + 5 = 5
Tous les objects peuvent être vrai (Truely) ou faux (Falsy)
bool("Bonjour") [^3]

Cependant tous les nombres sont considérés comme True à l'exception du 0 qui est considéré comme fausse.

Les caractères comme [] si vide seront considéré comme faux.  S'il contienne une valeur chiffré, elle est vrai


[^2]: True et False sont une sous-classe des nombres entiers. 1 et 0


[^3]: Il va répondre True car la chaîne comprend au moins un caractère.


