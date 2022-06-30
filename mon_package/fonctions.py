import os
import pickle
from random import choice
from donnees import *

def enregistrer_note():
	if os.path.exists(les_notes):
		elev=open("fichier.txt","wr")
		elev.pickle.Unpickler()
		etu=elev.load()