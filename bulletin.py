eleve = []
print("bienvenues")
classe = int(input("Saisisssez la classe : "))
i = 0
nombre_eleve = int(input("Entrer le nombre d'eleve de cette classe: "))
while i< nombre_eleve:
    nom_eleve = input(f"Entrer le nom  et le prenom du {i+1}  eleve: ")
    #prenom_eleve = input(f"Entrer le prenom du {i+1} eleve: ")
    u = 0
    cours = int(input("Entrer le nombre de cours: "))
    while u < cours: 
        note = int(input(f"Entrer la note du {u+1} er cours: "))
        u +=1
        
        
    