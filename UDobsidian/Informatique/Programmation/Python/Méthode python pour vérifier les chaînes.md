En Python 3, voici les méthodes disponibles et leurs différences pour vérifier le contenu d'une chaîne de caractères :

## ✅ **La bonne méthode pour vérifier si une chaîne ne contient que des chiffres :**

### `isdigit()`

python

"123".isdigit()      # True
"12.3".isdigit()     # False (contient un point)
"-123".isdigit()     # False (contient un signe)
"123a".isdigit()     # False (contient une lettre)
"１２３".isdigit()    # True (chiffres pleine largeur japonais)

## 📊 **Comparaison des méthodes :**

### 1. **`isdigit()`** ✅

- Vérifie si tous les caractères sont des chiffres
    
- Accepte les chiffres de toutes écritures (arabes, japonais, etc.)
    
- Rejette les signes (+,-), points décimaux, espaces
    

### 2. **`isDecimal()`** (vous avez écrit "isDigit")

python

"123".isdecimal()    # True
"１２３".isdecimal()  # False (chiffres japonais non décimaux)

- Plus restrictif que `isdigit()`
    
- Accepte uniquement les chiffres décimaux (0-9)
    

### 3. **`isnumeric()`** (vous avez écrit "isnum")

python

"123".isnumeric()    # True
"一二三".isnumeric()  # True (caractères numériques chinois)
"½".isnumeric()      # True (fraction)

- Plus large que `isdigit()`
    
- Accepte tous les caractères numériques (fractions, chiffres romains, etc.)
    

### 4. **`isalpha()`**

python

"abc".isalpha()      # True
"abc123".isalpha()   # False
"123".isalpha()      # False

- Vérifie si tous les caractères sont alphabétiques
    
- C'est l'inverse de ce que vous cherchez
    

## 🎯 **Recommandation :**

Pour vérifier qu'une chaîne ne contient **que des nombres** (au sens chiffres 0-9), utilisez **`isdigit()`** ou **`isdecimal()`** selon vos besoins de précision.

python

def est_un_nombre(chaine):
    return chaine.isdigit()
# Méthode python pour vérifier les chaînes
def est_chiffres_decimaux(chaine):
    return chaine.isdecimal()

Regroupe tes réponses dans un seul texte pour que puisse le copier dans Obsidian.

# 🔍 Vérification de chaînes numériques en Python 3

## Méthodes principales

### `isdigit()` ✅

python

"123".isdigit()      # True
"12.3".isdigit()     # False (contient un point)
"-123".isdigit()     # False (contient un signe)
"123a".isdigit()     # False (contient une lettre)
"１２３".isdigit()    # True (chiffres pleine largeur japonais)

**Description** : Vérifie si tous les caractères sont des chiffres (toutes écritures)

### `isdecimal()`

python

"123".isdecimal()    # True
"１２３".isdecimal()  # False (chiffres japonais non décimaux)
"½".isdecimal()      # False

**Description** : Plus restrictif, uniquement chiffres décimaux (0-9)

### `isnumeric()`

python

"123".isnumeric()    # True
"一二三".isnumeric()  # True (caractères numériques chinois)
"½".isnumeric()      # True (fraction)
"Ⅷ".isnumeric()      # True (chiffre romain)

**Description** : Accepte tous les caractères à valeur numérique

### `isalpha()`

python

"abc".isalpha()      # True
"abc123".isalpha()   # False
"123".isalpha()      # False

**Description** : Vérifie si tous les caractères sont alphabétiques

## 📊 Tableau comparatif

|Méthode|"123"|"-123"|"12.3"|"１２３"|"½"|"一二三"|
|---|---|---|---|---|---|---|
|`isdigit()`|✅|❌|❌|✅|❌|❌|
|`isdecimal()`|✅|❌|❌|❌|❌|❌|
|`isnumeric()`|✅|❌|❌|✅|✅|✅|
|`isalpha()`|❌|❌|❌|❌|❌|✅|

## 🎯 Cas d'usage recommandés

python

# Pour vérifier des chiffres "standards" (0-9)
def est_chiffres_standard(chaine):
    return chaine.isdecimal()
# Pour vérifier tout type de chiffres
def est_numerique(chaine):
    return chaine.isdigit()
# Pour vérifier tout caractère à valeur numérique
def est_valeur_numerique(chaine):
    return chaine.isnumeric()

## ⚠️ Limitations importantes

Ces méthodes ne vérifient **pas** :

- Les nombres négatifs (`-123`)
    
- Les nombres décimaux (`12.3`)
    
- Les espaces (`" 123"`)
    
- Les séparateurs de milliers (`"1,234"`)
    

Pour ces cas, utilisez plutôt :

python

def est_nombre_valide(chaine):
    try:
        float(chaine)
        return True
    except ValueError:
        return False