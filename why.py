import os
import pickle 
from random import choice 
from essai import *
def recup_scores():
	if os.path.exists(nom_fichier_scores):

	 	fichier_scores = open(nom_fichier_scores, "rb") 
	 	mon_depickler = pickle.Unpickler(fichier_scores)
	 	scores = mon_depickler.load()
	 	fichier_scores.close()
	else:
		scores = {}
	return scores
def enregistrer_scores(scores):
	fichier_scores = open(nom_fichier_scores, "wb")
	mon_pickler = pickle.Pickler(fichier_scores)
	mon_pickler.dump(scores)    
	fichier_scores.close()
def recup_nom_utilisateur():
	nom_utilisateur = input("Tapez votre nom: ")
	nom_utilisateur = nom_utilisateur.capitalize()
	if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
		 print("Ce nom est invalide.")
	return recup_nom_utilisateur()
	else:
	return nom_utilisateur
def recup_lettre():
	lettre = input("Tapez une lettre: ")
	lettre = lettre.lower()
	if len(lettre)>1 or not lettre.isalpha():
		print("Vous n'avez pas saisi une lettre valide.")
	return recup_lettre()
	else:        
	return lettre
def choisir_mot():
	    return choice(liste_mots)
def recup_mot_masque(mot_complet, lettres_trouvees):
	    mot_masque = "" 
	    for lettre in mot_complet:
	    	if lettre in lettres_trouvees:
	    		mot_masque += lettre
	        else:            
	        	mot_masque += "*"    
	        return mot_masque
