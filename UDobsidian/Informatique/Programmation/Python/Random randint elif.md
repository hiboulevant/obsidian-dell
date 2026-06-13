# Random randint elif

Exercice module random - Solution

**CODE**

1. import random

2. a = random.randint(0, 2)
3. b = random.randint(0, 2)

4. if a > b:
5.     print("Le nombre a est plus grand que le nombre b.")
6. elif a < b:
7.     print("Le nombre b est plus grand que le nombre a.")
8. elif a == b:
9.     print("Le nombre a et le nombre b sont égaux.")

**EXPLICATIONS**

On commence par générer deux nombres aléatoires avec le module `random` et la fonction `randint`.

On utilise ensuite une structure conditionnelle dans laquelle on vérifie si a est plus grand que b avec l'opérateur `>`.

On vérifie ensuite si a est plus petite que b avec l'opérateur `<`.

Et pour finir on vérifie si a est égal à b avec l'opérateur `==`.

**POINTS IMPORTANTS À RETENIR**

- Pour créer un nombre entier aléatoire, on utilise la fonction randint du module random.
    
- Pour comparer des variables, on utilise les opérateurs de comparaison (`>`, `<` et `==`).
    
- Pour vérifier une condition, on utilise des structures conditionnelles avec `if`, `elif` et `else`.
