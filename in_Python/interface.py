import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
from PIL import Image


# Création de la fonction qui sera appelée à "chaque nouvelle image"
def animate(k):

    ax[1].plot(t[:k*5], XC[:k*5], color = 'b')
    ax[1].plot(t[:k*5], XE[:k*5], color = 'r')
    ax[1].plot(t[:k*5], N[:k*5], color = 'g')
    ax[1].plot(t[:k*5], W[:k*5], color = 'k')

    ax[1].legend(["Commoner population", "Elite population", "Nature", "Wealth"])
    #rendre legende plus petite

    im_xc = Image.open("in_Python/im1.jpg") 
    im_xe = Image.open("in_Python/im2.jpg")
    im_n = Image.open("in_Python/im3.jpg") 
    im_w = Image.open("in_Python/im4.jpg")  

    ax[2].clear() #Permet d'éviter la superposition d'images de tailles diff

    ax[2].set_xlim([-1,1]) # Définit un cadre pour l'image 
    ax[2].set_ylim([-1,1])

    r_xc = XC[k*5]*0.5 + 0.05 # le "coeff proportionnalité" (=valeur de la col à indice k) * 2 + la valeur min
    r_xe = XE[k*5]*0.5 + 0.05
    r_n =   N[k*5]*0.5 + 0.05
    r_w =   W[k*5]*0.5 + 0.05

    
    ax[2].imshow(im_xc, extent=[-r_xc-0.5, r_xc-0.5, -r_xc-0.5, r_xc-0.5]) #image en carré ; 0,5 = éloignement par rapport au centre 
    ax[2].imshow(im_xe, extent=[-r_xe-0.5, r_xe-0.5, -r_xe+0.5, r_xe+0.5])
    ax[2].imshow(im_n, extent=[-r_n+0.5, r_n+0.5, -r_n+0.5, r_n+0.5])
    ax[2].imshow(im_w, extent=[-r_w+0.5, r_w+0.5, -r_w-0.5, r_w-0.5])

    ax[2].axis("off")



def readFile(fname):

    array = np.genfromtxt(fname, delimiter=', ', dtype='float64')
    XC = array[:,0]
    XE = array[:,1]
    N = array[:,2]
    W = array[:,3]

    return [XC, XE, N ,W]

if __name__=='__main__':

    time = 5000 # Quelle valeur du temps ? 
    fnameM = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_Python/results_python.txt"
    fnameP = "/Users/peppa/Desktop/Ba3/CMT/PROJECT/HANDY_PROJECT/in_C/results_python.txt"
    [XC, XE, N, W] = readFile(fnameP)
    t = [i for i in range(time)]
    
# Création de la figure et de l'axe
    interface, ax = plt.subplots(1, 3, figsize=(14,7))
    # Comment réduire la taille de la première colonne ?


#Gestion des limites de la fenêtre
    ax[1].set_xlim(-20, 1020)
    ax[1].set_ylim(-0.03, 1.03)
    

    ani = FuncAnimation(fig = interface, func = animate, frames = range(time), interval = 1, repeat = False)

    plt.axis("equal")
    plt.show()


# enregistrer la vidéo ?
# courbe inclusive