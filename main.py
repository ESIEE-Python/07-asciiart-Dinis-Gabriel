#### Imports et définition des variables globales


#### Fonctions secondaires
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    n=len(s)
    k=0
    caractere=[]
    nombre_occurence=[]
    for k in range(1,n):
        if s[k]==s[k-1]:
            nombre_occurence[-1]+=1
        else :
            caractere.append(s[k])
            nombre_occurence.append(1)        
    return (caractere,nombre_occurence)
def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme récursif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # cas de base
    if len(s)==0:
        return []
    # recherche nombre de caractères identiques au premier
    prem_caractere=s[0]
    n=1
    while n<len(s) and s[n]==prem_caractere:
        n+=1
    # appel récursif
    return [(prem_caractere,n)]+artcode_r(s[n:])
#### Fonction principale
def main():
    """
    Test les fonctions artcode Itéraive et récursive
    Args : None
    Returns : None
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))
if __name__ == "__main__":
    main()
