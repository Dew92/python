# coding:utf-8
from tkinter import *  # import les menu et autres widgets
from tkinter import messagebox  # sous module pour les message
import tkinter  # créer directement la fenetre
import json


class emptyFields(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def valid(user, pasw):
    contenu = None
    try:
        with open("connect.json", "r") as fich:
            contenu = fich.read()  # lecture du contenu du fichier
            contenu = json.loads(contenu)  # transform le string en dict
        # contenu trouvé et vérifiable
    except FileNotFoundError:
        print("Fichier introuvable")
        messagebox.showerror("Fichier d'indentification manquant", "Contacter le créateur de l'application")
    if contenu["id_user"] == user and contenu["passw"] == pasw:
        messagebox.showinfo("Connexion réussi", "Bievenue " + contenu["id_user"].capitalize() + "")
        return True
    else:
        messagebox.showerror("Erreur de connexion", "Combinaison < Utilisateur - Mot de passe > incorrect")


def rien():
    pass


def forgot():  # pass oublier
    pass


def press(event):
    #messagebox.showinfo("Cliquer", "Bien reçu")#lier à l'appli
    check()


def check():
    # valeur saisi
    tuser = zs_user.get()
    tpass = zs_pass.get()
    try:
        if tuser == "" or tpass == "":  # si vide
            raise emptyFields("Champs vides")  # excption vide
        if valid(tuser, tpass):
            print("next frame =>")  # chargement du profil
    except emptyFields:
        messagebox.showerror("Erreur de saisie", "Un des champs n'est pas rempli : connexion impossible")


app = tkinter.Tk()
app.title("Gestionnaire d'utilisateur")
# trouver les dimensions de l'ecran
screen_x = int(app.winfo_screenwidth())
screen_y = int(app.winfo_screenheight())
window_x = 640
window_y = 480
# centrage
pos_X = (screen_x // 2) - (window_x // 2)
pos_Y = (screen_y // 2) - (window_y // 2)

# affichage
geo = "{}x{}+{}+{}".format(window_x, window_y, pos_X, pos_Y)
# fixer la taille (max=min)
app.maxsize(window_x, window_y)
app.minsize(window_x, window_y)
# appliquer
app.geometry(geo)
# test
cf = tkinter.LabelFrame(app, text="Connexion", width=400, height=300, bd=2, padx=20, pady=40)
# widgets du menubar (statique)
menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nouveau", command=rien, state="disabled")
filemenu.add_command(label="Charger", command=rien, state="disabled")
filemenu.add_command(label="Sauvegarde", command=rien, state="disabled")
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=app.quit)
menubar.add_cascade(label="Fichier", menu=filemenu)
app.config(menu=menubar)
# widgets de connexion
lb_user = tkinter.Label(cf, text="Identifiant :", justify="left", anchor="w")
zs_user = tkinter.Entry(cf)
lb_pass = tkinter.Label(cf, text="Mot de passe :", justify="left")
zs_pass = tkinter.Entry(cf, show="*")
bt_cnx = tkinter.Button(cf, text="Connexion", command=check)
# event widgets
app.bind("<KeyPress-Return>", press)#
# centrage LF connexion
cfc_X = (window_x // 2) - (cf.winfo_width() // 2) - 10
cfc_Y = (window_y // 2) - (cf.winfo_height() // 2) - 30
# rattacher a la fenetre
cf.place(x=cfc_X, y=cfc_Y, anchor=CENTER)
lb_user.grid(row=0, column=0)
zs_user.grid(row=0, column=1)
lb_pass.grid(row=1, column=0)
zs_pass.grid(row=1, column=1)
bt_cnx.grid(row=2, column=1, padx=30, pady=15)
# maintenir la fenetre ouverte
app.mainloop()
