import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter

#Importer tous les fichiers python des résultats, ou juste certains, à voir 

def animate(k):
# k : désigne les frames depuis la fonction funcAnimation 
    ax.plot(t[:k*5], XC[:k*5], color = 'b')
    ax.plot(t[:k*5], XE[:k*5], color = 'r')
    ax.plot(t[:k*5], N[:k*5], color = 'g')
    ax.plot(t[:k*5], W[:k*5], color = 'k')
# ci-dessus : le facteur par lequel on multiplie k permet de faire varier la vitesse de déroul
    plt.title("Stable equitable scenario")
    ax.legend(["Commoner population", "Elite population", "Nature", "Wealth"])
    #rendre legende plus petite



def readFile(fname):

    array = np.genfromtxt(fname, delimiter=', ', dtype='float64')
    XC = array[:,0]
    XE = array[:,1]
    N = array[:,2]
    W = array[:,3]

    return [XC, XE, N ,W]

if __name__=='__main__':

    time = 1000
    fnameM = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_C/results_python.txt"
    fnameP = "/Users/peppa/Desktop/Ba3/CMT/PROJECT/HANDY_PROJECT/in_C/results_python.txt"
    # [XC, XE, N, W] = readFile(fnameP)
    [XC, XE, N, W] = readFile(fnameP)
    t = [i for i in range(time)]

    
# Création de la figure et de l'axe
    interface, ax = plt.subplots()

#Gestion des limites de la fenêtre
    ax.set_xlim(-20, 1020)
    ax.set_ylim(-0.03, 1.03) # marges --> Permet une meilleure clarté du graph 

    ani = FuncAnimation(fig=interface, func = animate, frames = range(time), interval = 1, repeat = False)
    #au lieu de mettre fig=interface, on peut mettre plt.gcf()
    # frames : appelle pour chaque indice de t, les 4 valeurs des variables 
    # interval : 1=plus rapide 

    plt.show()

    # screen_width = fen_princ.winfo_screenwidth()
    # screen_height = fen_princ.winfo_screenheight()

    # print(screen_width, screen_height)

    # window = [curseurxc, curseurxe, curseurn, curseurw, monAffichagexc, monAffichagexe, monAffichagen, monAffichagew, monBoutonxc, monBoutonxe, monBoutonn, monBoutonw, monBoutonfinal]
    # for i in window : i.destroy()
    # monAffichagecalc = Label(fen_princ, text = "Handy is calculating with chosen :\n"+"XC : "+xc+"\nXE : "+xe+"\nN : "+n+"\nW : "+w, width=70)
    # monAffichagecalc.place(x=0, y=0)


    # window = [monAffichageinput, name_file, monBoutoninput]
    # for i in window : i.destroy()
    # monAffichagecalc = Label(fen_princ, text = "Handy is calculating from file", width=70)
    # monAffichagecalc.place(x=10, y=10)

    # ajouter le titre du fichier pour mettre dans le titre

        # name_file = Entry(fen_princ)
    # name_file.pack()