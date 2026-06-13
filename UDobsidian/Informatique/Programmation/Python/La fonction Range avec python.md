# La fonction Range avec python
Avec Python 3, la fonction range ne retourne pas directement une liste, mais un objet de type range :

1. > interval = range(10)
2. > print(interval)
3. range(0, 10)
4. > print(type(interval))
5. <class 'range'>

Cet objet contient plusieurs attributs qui vous permettent d'obtenir des informations sur ce `range` :

1. > interval.start
2. 0
3. > interval.step
4. 1
5. > interval.stop
6. 10

Si vous souhaitez récupérer cet objet range sous la forme d'une liste, il suffit de le convertir avec la fonction `list` :

1. > interval = list(interval)
2. > print(interval)
3. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
4. > print(type(interval))
5. <class 'list'>

Si vous utilisez Python 2, vous obtenez directement une liste, donc pas besoin de faire la conversion.

1. Python 2.7.15 (default, Jul 23 2018, 21:27:06)
2. [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
3. Type "help", "copyright", "credits" or "license" for more information.
4. > interval = range(10)
5. > print(interval)
6. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
7. > print(type(interval))
8. <type 'list'>

