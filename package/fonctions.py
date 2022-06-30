import os
import pickle
from come import *
def recuperer_les_notes():
    notee=open(les_notes,"rb")
    depick=pickle.Unpickler(notee)
    depicke=depick.load(note)
    notee.close()
def enregistrer_notes():
    
    notee=open(les_notes,'wb')
    und=pickle.Pickler(notee)
    und=notee.dump(note)
    notee.close()

os.system("pause")