# Ajouter un élément à la fin de la liste 1

liste = [1 , 2, 3, 4, 5]
liste.append(6)
print(liste)

# Ajouter un élément à une position spécifique de la liste 2
liste.insert(2, 10)
print(liste)

# Supprimer un élément de la liste 3
liste.remove(2)
print(liste)

# Supprimer un élément à une position spécifique de la liste 4
del liste[3]
print(liste)

# Supprimer le dernier élément de la liste 5
liste.pop()
print(liste)

# Ajouter plusieurs éléments à la fin de la liste 6
liste.extend([7, 8, 9])
print(liste)
