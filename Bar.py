print("Bienvenu")
i = 0
total = 0
print("Avant d\'utiliser l\'application vous devez d\'abord vous connecter!")
tentative = 5
while i < 5: 
    nom_d_utulisateur = input("Entrer le nom d\'utilisateur: ")
    #nom_d_utulisateur.capitalize()
    mot_de_passe = int(input("Entrer le mot de passe: "))
    if nom_d_utulisateur.capitalize() == "Eric" and mot_de_passe == 1234: 
        print("Merci et passe par le choix")
        print("1. Bar \n 2.Hotel \n 3.Cuisine")
        choix = int(input("Entrer le numero de votre choix: "))
        if choix == 1: 
            print("1.Facture \n 2.Dette paye \n 3.Entrees  4.rapport")
            option = int(input("Entrer le numero de votre choix: "))
            if option == 1:
                                  
                date = int(input("Entrer la date du jour: "))
                nom_serveur = input("Entrer le nom du serveur: ")
                produit = input("Entrer le produit: ")
                prix = 0
                if produit == "Primus": 
                    prix = 2000
                elif produit == "Fanta": 
                    prix = 1000 
                quantite = int(input("Entrer la quantite: "))
                total =  prix * quantite 
                print("Total: ",total)             
                with open("facture.txt", "w+") as file: 
                    file.write(date)
                    file.write(nom_serveur)
                    file.write(produit)
                    file.write(quantite)
                    file.write(total)
                    file.close()
            elif option == 2: 
                date = date.date.today()
                    
                
        
        
        
        
        
        
         
        
    else: 
        print("echec et il vous reste que {}".format(tentative-1))
        tentative -=1
        i +=1
        
        #break
