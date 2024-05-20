def verif_liste_vide(dictionnaire):
        for cle, liste in dictionnaire.items():
            if liste:
                return False
        return True


dico={"a":[],"b":[],"c":[]}
print(verif_liste_vide(dico)) # False