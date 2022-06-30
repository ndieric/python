import os
prix_unitaire=0
affiche=("Bienvenus dans l'utilisation de notr application")
print(affiche)
print("Comme introduction cette application vient a temps pour vous aider a  faire services qui sont un peu rapide, diminuer des erreurs aussi ")
print("Vous devez d'abord vous connectez merci")
nom_Utilisateur=input("Entrer le nom d\'Utilisateur: ")
mot_de_pass=int(input("Entrer le mot de passe: "))
if(nom_Utilisateur=="Eric" and mot_de_pass==1234):
	print("Bienvenus et passez au choix de ce que vous voulez faire")
	print("1.Bar"),print("2.Hotel"),print("3.Autre")
	
	try:
		choix=input("Entrer le chiffre de votre choix: ")
		choix=int(choix)
		
	except NameError:
		print("SVP saisi un entier")
		choix=int(input("Entrer le chiffre de votre choix: "))
	if(choix==1):
		print("1.Facture"),print("2.Entrees")
		choixx=int(input("Entrer le choix: "))
		if(choixx==1):
			Facture=("Facture")
			prix_unitaire=0
			def facture_bar():
       
				#global prix_unitaire
				nom_serveur=input("Entrer le nom du serveur: ")
				numero_facture=int(input("Entrer le numero: "))
				produit=input("Entrer le produit: ")
    
				if produit=="Primus":
					prix_unitaire=2000
				elif produit=="fanta":
					prix_unitaire=1000
				quantite=int(input("Entrer la quantite: "))
				total=prix_unitaire*quantite
				print("Total est : ",total)
			facture_bar()
	elif choix==2:

		facture_bar()
			#print()
		
else:
	print("Le mot de passe ou le nom d\' Utilisateur incorrect")
#break


os.system("pause")