from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os


def afficherValeur_xc() :
    valeur = curseurxc.get()
    text1 = "XC : " + str(valeur)
    monAffichagexc.configure(text = text1)
def afficherValeur_xe() :
    valeur = curseurxe.get()
    text1 = "XE : " + str(valeur)
    monAffichagexe.configure(text = text1)
def afficherValeur_n() :
    valeur = curseurn.get()
    text1 = "N : " + str(valeur)
    monAffichagen.configure(text = text1)
def afficherValeur_w() :
    valeur = curseurw.get()
    text1 = "W : " + str(valeur)
    monAffichagew.configure(text = text1)

def sendCursors():
    xc = str(curseurxc.get())
    xe = str(curseurxe.get())
    n = str(curseurn.get())
    w = str(curseurw.get())

    variables = ['c', xc, xe, n, w]
    os.chdir("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_Python")
    os.chdir("../in_C") #sortir de celui d'avant
    # os.system("python emilien.py")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + variables[0] + " " + variables[1] + " " + variables[2] + " " + variables[3] + " " + variables[4])

    fen_princ.destroy()

def sendPath():
    path = ['f', name_file.get()]
    os.chdir("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_Python")
    os.chdir("../in_C") #sortir de celui d'avant
    # os.system("python emilien.py")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + path[0] + " " + path[1])

    fen_princ.destroy()

def uploadFile():
    global monAffichageinput
    global name_file
    global monBoutoninput

    window = [monAffichagep, monBoutonfile, monBoutoncurs]
    for i in window : i.destroy()

    monAffichageinput = Label(fen_princ, text = "Enter the path of your file", width=70)
    monAffichageinput.pack()

    name_file = Entry(fen_princ)
    name_file.pack()

    monBoutoninput = Button(fen_princ, text = "Validate the path", command = sendPath)
    monBoutoninput.pack()

def launchCursors():
    global curseurxc
    global monAffichagexc
    global monBoutonxc
    global curseurxe
    global monAffichagexe
    global monBoutonxe
    global curseurn
    global monAffichagen
    global monBoutonn
    global curseurw
    global monAffichagew
    global monBoutonw
    global monBoutonfinal

    window = [monAffichagep, monBoutonfile, monBoutoncurs]
    for i in window : i.destroy()

    # XC
    curseurxc = Scale(fen_princ, orient='horizontal', from_ = 0, to = 10)
    curseurxc.pack()

    monAffichagexc = Label(fen_princ, text = "Value wanted for XC", width=70)
    monAffichagexc.pack()

    monBoutonxc = Button(fen_princ, text = "Get value for XC", command = afficherValeur_xc)
    monBoutonxc.pack()
    
    # XE
    curseurxe = Scale(fen_princ, orient='horizontal', from_ = 0, to = 20)
    curseurxe.pack()

    monAffichagexe = Label(fen_princ, text = "Value wanted for XE", width=70)
    monAffichagexe.pack()

    monBoutonxe = Button(fen_princ, text = "Get value for XE", command = afficherValeur_xe)
    monBoutonxe.pack()

    #N
    curseurn = Scale(fen_princ, orient='horizontal', from_ = 0, to = 5)
    curseurn.pack()

    monAffichagen = Label(fen_princ, text = "Value wanted for N", width=70)
    monAffichagen.pack()

    monBoutonn = Button(fen_princ, text = "Get value for N", command = afficherValeur_n)
    monBoutonn.pack()

    # W
    curseurw = Scale(fen_princ, orient='horizontal', from_ = 0, to = 15)
    curseurw.pack()

    monAffichagew = Label(fen_princ, text = "Value wanted for W", width=70)
    monAffichagew.pack()

    monBoutonw = Button(fen_princ, text = "Get value for W", command = afficherValeur_w)
    monBoutonw.pack()

    #Validate values
    monBoutonfinal = Button(fen_princ, text = "GOOOO", command = sendCursors)
    monBoutonfinal.pack()

def questions():
    global monAffichagep
    global monBoutonfile
    global monBoutoncurs

    # First choices
    monAffichagep = Label(fen_princ, text = "What do you prefer?", width=70)
    monAffichagep.pack()

    monBoutonfile = Button(fen_princ, text = "I want to use my file", command = uploadFile)
    monBoutonfile.pack()

    monBoutoncurs = Button(fen_princ, text = "I want to chose now", command = launchCursors)
    monBoutoncurs.pack()


if __name__=='__main__':
    fen_princ = Tk()

    fen_princ.attributes('-fullscreen', True)
    questions()
    fen_princ.mainloop()



#ajouter résumé à la fin
#préciser quels sont les paramètres par défaut

# expliquer les variables 
# et la normalisation 