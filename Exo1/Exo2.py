print("Exo 2 Ecrire une fonction qui a en paramètre un tableau non vide, un entier v,et qui"
"renvoie l’indice de la première occurrence de v dans le tableau -1 si v n’est pas"
"présent dans le tableau")

tableau=[1,2,4,5];

def indicePremiereOccurence(tableau, v):
    longueur = len(tableau)
    indice_valeur = 0
    for i in range(longueur):
        if tableau[i] == v:
            indice_valeur = i

    print(indice_valeur)
    return indice_valeur

indicePremiereOccurence(tableau, 5)
indicePremiereOccurence(tableau, 9)







