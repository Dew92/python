# Menu de chargement de sauvegardes

import os 			# lib pour effacer dans la console
import pickle 		# lib pour les fichier
import time			# lib pour les dates
import re 			# lib d expression reg

"""
Une partie est défini par un nom de personnage, le nombre de sauvegarde et la date de creation
"""

SiG = True

def newGame():
	os.system("cls")
	character=input("Veuillez indiquer le nom du personnage :\t")
	czas=time.strftime("%Y-%m-%d_%H-%M-%S") #date et heure courant
	partie = {"nom":character,"nbSave":1,"creatData":czas}
	printGame(partie)
	saveData(partie)

def loadGame(party):
	with open(party,"rb") as file:
		mp = pickle.Unpickler(file)
		cp = mp.load() #paramatre de partie chargé
		partie=cp
	printGame(partie)
	sa=input("Revenir au menu en sauvegardant ? (O/N)")
	if sa == "O" or sa == "o":
		partie["nbSave"]+=1
		saveData(partie)
	else:
		print("Retour au menu sans sauvegader. Appuyer sur Entrée ...")
		tempo()

def delData(party):
	os.remove(party) #suppression du fichier physique
	print("Sauvegade supprimer. Appuyer sur Entrée pour revenir au menu ...")
	tempo()

def manageDate(integ):
	os.system("cls")
	Partie=None
	adapt="toto"
	print("Fichiers sauvegardés :\n")
	files=listFiles()
	if integ == 2: #chargement
		adapt="charger"
	if integ == 3:
		adapt="supprimer"
	try:
		files[0] # premiere sauvegarde trouvé sinon error
		i=menuList(files)
		lp=input("\nVeuillez choisir la partie à {} : \t".format(adapt))
		try:
			lp = int(lp)
			if lp>0 and lp<=i+1 :
				lp-=1 # numero - 1 = index
				if integ==2: # chargement party
					loadGame(files[lp])
				if integ ==3: #suppression
					delData(files[lp])
		except ValueError:
			print("Saisie incorrect : cette sauvegarde n'existe pas.")
			tempo()
	except IndexError:
		print("Aucune sauvegarde trouvée : impossible de charger")
		tempo()

def tempo():
	i=input()#Faire artificiellement la pause pour confirmer la sauvegarde à l'utilisateur
	pass

def menuList(files):
	i=0
	for sv in files:
		perso=re.findall("^[A-Za-z0-9]*",sv)
		st=re.findall("[0-9]{4}[-]+[0-9]{2}[-]+[0-9]{2}[_]+[0-9]{2}[-]+[0-9]{2}[-]+[0-9]{2}",sv)
		st="-".join(st)	#transforme la liste en un string
		i+=1
		print("#{} Partie de {} : \t {}.".format(i,perso[0],st))
	return i

def saveData(partie):# sauvegarde des données en binaire
	mot=str(partie['nom'])+"_"+str(partie["creatData"])
	with open(mot,"wb") as file:
		mp = pickle.Pickler(file) 	# creer le fichier binaire
		mp.dump(partie)
	if file.closed:
		print("Sauvegarde réussi. Appuyer sur une touche Entrée.")
		tempo()

def listFiles():
	files=[]
	regex=r"[A-Za-z0-9]*[_]+[0-9]{4}[-]+[0-9]{2}[-]+[0-9]{2}[_]+[0-9]{2}[-]+[0-9]{2}[-]+[0-9]{2}"	# expression du fichier nom_date
	repertory=os.listdir(".")	# liste des fichier du répertoire courrant
	for i in repertory:
		if re.findall(regex,i):
			files.append(i)
	return files

def printGame(partie):
	if partie["nbSave"]==1:
		print("La partie du joueur {} sera enregistrer pour la première fois à {}".format(partie["nom"],partie["creatData"]))
	else:
		print("La partie du joueur {} sera enregistrer pour la {}ème fois à {}".format(partie["nom"],partie["nbSave"],partie["creatData"]))

if __name__ == "__main__":
	while SiG:
		os.system("cls") # efface ecran console
		print("Menu Principal :\n\n1# Nouvelle Partie\n2# Charger Partie\n3# Supprimer Partie\n4# Quitter\n")
		choix = input() #peut etre tout sauf un int
		try:
			choix = int(choix)
			if choix == 1:
				newGame()
			if choix == 2:
				manageDate(2)
			if choix == 3:
				manageDate(3)
			if choix == 4:
				SiG = False
			if choix > 4:
				raise ValueError()
		except ValueError:
			print("saisie incorrect")
	exit()# on quitte proprement
