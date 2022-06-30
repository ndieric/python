import os
import pickle
os.chdir("D:/yes")
eleve="notes"
def Enregistrer_notes():
	notes=int(input("Entrer la note: "))
	if os.path.exists(eleve):

		mine=open(eleve,"rb")
		mon_depickle=pickle.Unpickler(mine)
		notes=mon_depickle.load()
		mine.close()
	else:
		notes={}
	return notes

