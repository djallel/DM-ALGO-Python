print("Exo 4) Ecrire une fonction qui a en paramètre un tableau non vide et qui renvoie"
"l’indice du plus grand élément d’un tableau")

tableau=[1,2,4,5];

def dernierIndiceMaximum(tableau):
    maxi = tableau[0]
    longueur=len(tableau)
    indice_max = 0
    for i in range(longueur):
        if tableau[i] >= maxi:
            maxi = tableau[i]
            indice_max = i
    print(indice_max)
    return indice_max

dernierIndiceMaximum(tableau)





