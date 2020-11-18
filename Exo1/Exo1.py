print("Exo 1 Ecrire une fonction qui a en paramètre un tableau non vide et qui renvoie le"
      "plus petit élément d’un tableau non vide")

tableau=[1,2,4,5];

def plusPetitElementDunTableau(tableau):
    # if tableau non vide renvoyer le min
    mini = tableau[0]
    for i in tableau:
        if i <= mini:
            mini = i
    print("Le plus petit élément du tableau est :")
    print(mini)
    return mini

plusPetitElementDunTableau(tableau)






