import os
import math
print("Binvenue ")
print("choisissez l\'operateur:  ")
print("1. Addition")
print("2. Soustraction")
print("3. multiplication")
print("4. Equation du 3eme degre")
print("5. La table de multiprication")
print("6. La puissance")
print("7. La moyenne")
choix =int(input("Entrer le numero de votre choix: "))
if choix == 1: 
    o = 0
    nombre1= int(input("Entrer le premier nommbre que vous : "))
    
    print("la somme est de : ",addition)
elif choix == 2: 
    nombre1= int(input("Entrer le premier nommbre que vous voulez multiplier: "))
    nombre2 = int(input("Entrer deuxieme nombre: "))
    addition = nombre1 - nombre2
    print("le resultat est de : ",addition)
elif choix == 3: 
    nombre1= int(input("Entrer le premier nommbre : "))
    nombre2 = int(input("Entrer deuxieme nombre: "))
    addition = nombre1 * nombre2
    print("le resultat est de : ",addition)
elif choix == 4:
    
    a = int(input("Entrer la valeur de a : "))
    b = int(input("Entrer la valeur de b : "))
    c = int(input("Entrer la valeur de c :"))
    delta = pow(b,2) - 4*a*c
    if delta > 0: 
        print("L'equation est invariable")
    d1 = (-b - delta)/a

    d2 = (b + delta)/a
    print("la valeur  du delta: ",delta)
    print("la valeur de x1:",d1)
    print("la valeur de x2" ,d2)
elif choix == 5:
    i = 0 
    table = int(input("Entrer la table que vous voulez: "))
    while i < 13: 
        print(i ,"*", table ,"=", i*table)
        i +=1
elif choix == 6: 
    nombre = int(input("Entrer le nombre: "))
    puiss = int(input("Entrer la puissance: "))
    puissance = nombre * puiss
    print(f"{nombre} exposa {puiss} = ", puissance)
elif choix == 7: 
    liste=[]
    i=0
    nombre = int(input("Entrer le nombre de chiffres: "))
    while i< nombre: 
        eleve=int(input(f"Entrer le {i+1}er nombre: "))
        i +=1
        liste.append(eleve)
    s = len(liste)
    somme = sum(liste)
    moyenne = somme/s 
    print("la moyenne =: ", moyenne)
elif choix == 8: 
    liste=[]
    i=0
    nombre = int(input("Entrer le nombre de chiffres: "))
    while i< nombre: 
        eleve=int(input(f"Entrer le {i+1}er nombre: "))
        i +=1
        liste.append(eleve)
    s = len(liste)
    somme = sum(liste)
    pourcentage = (somme * 100)/s
    #pourcentage = int(pourcentage)
    print(f"le pourcentage est de {pourcentage}%")
   
    
os.system("pause") 
