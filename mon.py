locataires=[]
immpangu = ["twinyoni","mirango", "Heha"]
print("Bienvenue")
print("Avant d\'utiliser l'application veuillez vous connecter!")
user=input("Entrer Votre nom d'utilisateur: ")
mot = int(input("Entrer Votre mot de passe: "))
if user == "Eric" and mot == 1234 : 
    print("Bienvenus vous avez bien saisi votre identification")
    print("Choisissez l\'option: ")
    print("1.Loyer"),print("2.controle")
    choix = int(input("Entrer le numero de votre choix: "))
    if choix == 1: 
        class Personne: 
            def __init__(self): 
                self.nom = ""
                self.prenom = ""
                self.contact = ""
            def donnees_locataires(self): 
                self.nom = input("Entrer Votre nom: ")
                if self.nom == "":
                    print("Le nom est obligatoire!") 
                    self.nom = input("Entrer Votre nom: ")
                self.prenom = input("Entrer Votre prenom: ")
                if self.prenom == "": 
                    print("Le prenom est obligatoire!") 
                    self.prenom = input("Entrer Votre prenom: ")
                    
                self.contact = int(input("Entrer Votre contact: "))
                if self.contact == "": 
                    print("Le contact est obligatoire!") 
                    self.contact = input("Entrer Votre contact: ")
                    
            def enregistrement(self):
                locataires.append(self.nom)
                locataires.append(self.prenom)
                locataires.append(self.contact) 
            def donnees_impangu(self,loyer=0): 
                self.impangu = input("Entrer Urupangu: ")
                if self.impangu not in immpangu: 
                    print("urworupangu ntirubaho")
                    self.impangu = input("Entrer Urupangu: ")
                    
                else:
                    self.numero_maison = int(input("Entrer numero de votre maison: "))
                
                if self.numero_maison == 1 and self.impangu == "twinyoni": 
                    self.loyer = 50000
                elif self.numero_maison == 2 and self.impangu == "twinyoni": 
                    self.loyer = 70000
                elif self.numero_maison == 1 and self.impangu == "mirango": 
                    self.loyer = 100000
                elif self.numero_maison == 2 and self.impangu == "mirango":
                    self.loyer = 60000
                elif self.numero_maison == 1 and self.impangu == "Heha": 
                    self.loyer = 90000
                elif self.numero_maison == 2 and self.impangu == "Heha":
                    self.loyer = 120000
                
            def affichage(self): 
                print("Nom: ", self.nom)
                print("Prenom",self.prenom)
                print("contact: ",self.contact)
                print("Loyer",self.loyer)              
        mo = Personne()
        mo.enregistrement()
        mo.donnees_locataires()
        mo.donnees_impangu()
        mo.affichage()
        print(locataires)
else: 
    print("mot de passe ou nom d\'utilisateur est incorrect !")
