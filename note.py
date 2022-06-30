compteur_eleve = 0
nombre_eleve = int(input("Entrer le nombre d\'eleve: "))
while compteur_eleve < nombre_eleve: 
    eleve = input(f"Entrer le {compteur_eleve + 1} er eleve: ")
    compteur_cour = 0
    nombre_cours = int(input("Entrer le nombre de cours: "))
    while compteur_cour < nombre_eleve: 
        cours = input(f"Entrer le nom du {compteur_cour + 1} cours :  ")
        compteur_note = 0
        while compteur_note < nombre_cours: 
            note = int(input(f"Entrer la {compteur_note +1}er note:  "))
            compteur_note +=1
        compteur_cour += 1 
    compteur_eleve += 1

