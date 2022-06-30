liste=[]
i=0
nombre = int(input("Entrer le nombre d'eleve: "))
while i< nombre: 
    eleve=input(f"Entrer le {i+1}er eleve: ")
    i +=1
    liste.append(eleve)
s = len(liste)
print(s)
    
      
