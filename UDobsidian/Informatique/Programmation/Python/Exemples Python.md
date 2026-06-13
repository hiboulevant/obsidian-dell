# Exemples Python

	1.3.4 Les opérateurs en Python
1.3.4.1 Les différents types d’opérateurs en Python
Les opérateurs sont utilisés en Python pour effectuer des opérations sur les variables et les valeurs associées. Python classifie les opérateurs selon les groupes suivants :
1. Opérateurs arithmétiques
2. Opérateurs d’assignation
3. Opérateurs de comparaison
4. Opérateurs logiques

1.3.4.2 Les opérateurs arithmétiques----
	1.   Adition: 4 + 4 = 8
	2.  Soustraction: 16-8 = 8
	3.  Multiplication: 4 * 5 
	4.  Division: 16 /2 = 8
	17 / 3  # classic division returns a float = 5.666666666666667
	Exposant: 2 ** 3 = 8 
Les opérateurs arithmétiques sont utilisés en Python pour effectuer des opérations de calcul sur les variables comme addition, multiplication, division

<u>Opérateur Description</u>
’+ ’ addition
’-’ soustraction
’*’ multiplication
’/’ division
’%’ modulo ( reste de la division euclidienne) ’**’ Exponentiation
’//’ quotient de la division euclidienne

1.3.4.3 <u>Les opérateurs d’assignation</u>
Les opérateurs d’assignation sont utilisés en Python pour assigner des valeurs aux variables :

Les opérateurs de comparaison

Opérateurs Exemple Explication
Opérateur Exemple Explication
= x = 7 x prends la valeur 7 + = x + = 5 x = x + 5
– = x – = 5 x = x -5
* = x * = 5 x = x *5
/ = x / = 5 x = x / 5
% = x % = 5 reste de la division euclidienne de x par 5 // = x // = 5 quotient de la division euclidienne de x par 5 ** = x ** = 3 x = x **3 ( x^3 ie x*x*x ) & = x & = 5 x = x &5 (& désigne l’opérateur binaire)

1.3.4.4 Opérateurs de comparaison
 >       Plus grand que
<       Plus petit que
>=   Plus grand ou égal à
<=   Plus petit ou égal à
==   Égal [^1]
!=   Différent

Les opérateurs de comparaison sont utilisé en Python pour comparer les variables :
Opérateur Description = = opérateur d’égalité ! = opérateur différent

> opérateur supérieur < opérateur inférieur > = opérateur supérieur ou égale < = opérateur inférieur ou égale

1.3.4.5 Opérateurs logiques Opérateur Description and et logique or ou logique not Négation logique

---
1.4 <u>Les fonctions en Python</u>
Le langage Python possède déjà des fonctions prédéfinies comme print () pour afficher du texte ou une variable, input () pour lire une saisie clavier... Mais il offre à l’utilisateur la possibilité de créer ses propres fonctions :

Exemple. Fonction qui renvoie le double d’un nombre
1 def maFonction ( x ) :
2 return 2∗x
3 print ( " Le double de 5 e s t : " , maFonction ( 5 ) )
4 # a f f i c h e : Le double de 5 est 10
	---
	# Python 3: List comprehensions
 Fruits = ['Banana', 'Apple', 'Lime']
 Loud_fruits = [fruit.Upper () for fruit in fruits] 
 Print (loud_fruits)
['BANANA', 'APPLE', 'LIME']

1.5 **Structures de contrôles**

1.5.1<u> La structure sélective If ... Else</u> ...

La structure sélective if ... Else , permet d’exécuter un ensemble d’instructions lorsqu’une condition est réalisée.
Syntaxe :

1 i f ( c o n d i t i o n ) :
2 i n s t r u c t i o n s . . .
3 else :
4 a u t r e s i n s t r u c t i o n s . . .

Exemple. Structure if ... Else...
1 # cod ing : ut f −8
2 age = 19
3 i f ( age >= 18) :
4 print ( " Vous ê t e s majeur ! " )
5 else :
6 print ( " Vous ê t e s mineur ! " )
7 # a f f i c h e vous ê t e s majeur

_sélective if ... Else , permet d’exécuter un ensemble d’instructions lorsqu’une condition est réalisée.
Syntaxe :

1 i f ( c o n d i t i o n ) :
2 i n s t r u c t i o n s . . .
3 else :
4 a u t r e s i n s t r u c t i o n s . . .

Exemple. Structure if ... Else...
1 # cod ing : ut f −8
2 age = 19
3 i f ( age >= 18) :
4 print ( " Vous ê t e s majeur ! " )
5 else :
6 print ( " Vous ê t e s mineur ! " )
 7  # a f f i c h e vous ê t e s majeur
 
---- # List and the enumerate function
List (enumerate (fruits))
[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]

print('The product is:', product)

# For loop on a list
numbers = [2, 4, 6, 8]
 product = 1
 for number in numbers:
...    product = product * number
... 
print('The product is:', product)
The product is: 384	

---
```python
# Exemple d'utilisation de try-except pour gérer les exceptions
try:
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))
    resultat = a / b
    print(f"Le quotient de {a} par {b} est : {resultat}")
except ZeroDivisionError:
    print("Erreur : Le dénominateur ne peut pas être nul.")
except ValueError:
    print("Erreur : Veuillez entrer des nombres entiers valides.")
```

Code généré par l'IA. Examinez et utilisez soigneusement. .

Dans cet exemple :

- Nous utilisons l’instruction **try** pour entourer le code susceptible de générer des exceptions.
- Si l’utilisateur entre un dénominateur nul, une **ZeroDivisionError** est levée, et le message d’erreur correspondant est affiché.
- Si l’utilisateur entre autre chose qu’un nombre entier, une **ValueError** est levée, et le message d’erreur correspondant est affiché.

[N’hésitez pas à personnaliser cet exemple en ajoutant d’autres types d’exceptions ou en gérant des cas spécifiques selon vos besoins](https://www.pierre-giraud.com/python-apprendre-programmer-cours/gestion-exception-try-except-else/) [1](https://www.pierre-giraud.com/python-apprendre-programmer-cours/gestion-exception-try-except-else/)[2](https://www.tresfacile.net/les-exceptions-en-python-try-except/).

---
<h1 class="text-3xl font-bold underline">
    Hello world!
</h1>
Exemple : affichage total des caractères d’une chaîne à l’aide de la méthode len () )
S = 'Python'
For i in range (0 ,len (s) ):
    Print (s [i])
---

### Les types numériques int, float et complex

Python définit trois types de valeurs numériques supportées :

- Le type `int` qui représente tout entier positif ou négatif ;
- Le type `float` qui représente les nombres décimaux et certaines expressions scientifiques comme le `e` pour désigner une exponentielle par exemple;
- Le type `complex` qui représente les nombres complexes ou nombres imaginaires et qui se sert de la lettre `j` pour représenter la partie imaginaire d’un nombre.
- ci, on commence par effectuer des opérations entre nombres : addition, soustraction, multiplication, division et élévation à la puissance. Notez que pour réaliser une division entière, on utilise l’opérateur `//`.
-  Le type de données “nombre décimal” ou `float` couvre tous les nombres décimaux (c’est-à-dire les nombres à virgule) ainsi que certaines expressions scientifiques comme le `e` qui désigne une exponentielle
- # La différence entre is et == 
  Égalité les variables ont même valeur
a  =  [1, 2, 3]
b  =  [1, 2. 3]
a == b
True
----------- 
Par contre: si l'opératateur est is les objets n'ont pas la même valeur
a is b
False
---
Pour vérifier cela :
Id (a) 
4456584048
Id (b) 
4457604032
Le retour de la fonction id n'est pas la même, 
L'adresse de la mémoire de chaque objet n'est pas la même
--- 
# Particularité
Les nombres de -5 à 256

A = 1000
 B = 2000
 False 
				 Évidement 1000 n'est == à 2000
Par contre
B == 1000
A == b
True 
Ici a et b ont une même valeur
Cependant:
A is b 
False
---
 a = 256
 b = 256 
  a is b
  True
  ---
  a = 257
  b = 257 
  False
  --
            En effet car les valeurs dépasse 256


[^1]: Égalité pour python == en mathématique on n'a pas le concept de variable


