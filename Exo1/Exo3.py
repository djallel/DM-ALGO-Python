print("Exo 3) Ecrire une fonction qui a en paramètre un tableau non vide et qui renvoie la"
"moyenne des éléments d’un tableau")
# https://emilypython.wordpress.com/category/python/
tableau=[1,2,4,5];

def somme(tableau):
    _somme = 0
    for i in tableau:
        _somme = _somme + i
    return _somme

def moyenne(tableau):
    print(somme(tableau)/len(tableau))
    return somme(tableau)/len(tableau)


moyenne(tableau)




