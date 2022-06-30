def facture(total=0): 
    nom = input("Entrer le nom : ")
    produit = input("Entrer le produit: ")
    if produit == "primus": 
        prix = 2000
    elif produit == "Fanta":
        prix = 1000
    quantite = int(input("Entrer la quantite: "))
    total = prix * quantite
    print("total ",total)
facture()