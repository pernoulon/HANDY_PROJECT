import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
from PIL import Image
import os


def readFile(fname):

    array = np.genfromtxt(fname, delimiter=', ', dtype=float)
    XC = array[2:,0]
    XE = array[2:,1]
    N = array[2:,2]
    W = array[2:,3]
    variables = array[0,:]
    parameters = array[1,:]
    return [XC, XE, N ,W, variables, parameters]

def stateText():
    ax[0].axis("off")
    text1 = "Variables : \nXC = "+xc+"\nXE = "+xe+"\nN = "+n+"\nW = "+w+"\n"
    text2 = "Parameters : \nam = "+am+"\naM = "+aM+"\nbc = "+bc+"\nbe = "+be+"\ng = "+g+"\nl = "+l+"\ns = "+s+"\nd = "+d+"\nk = "+k+"\nr = "+r+"\n"
    ax[0].text(0.3,0.5, s=text1+text2)

def finalText():
    ax[2].clear()
    ax[2].axis("off")
    ax[2].text(0.3, 0.5, 'We have reached a collapse', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

# Création de la fonction qui sera appelée à "chaque nouvelle image"
def animate(k):

    s = k*skip

    ax[1].plot(t[:s], XC[:s], color = 'b')
    ax[1].plot(t[:s], XE[:s], color = 'r')
    ax[1].plot(t[:s], N[:s], color = 'g')
    ax[1].plot(t[:s], W[:s], color = 'k')

    ax[1].legend(["Commoner population", "Elite population", "Nature", "Wealth"])
    #rendre legende plus petite

    ax[2].clear() #Permet d'éviter la superposition d'images de tailles diff

    r_xc = XC[s]*0.5 + 0.05 # le "coeff proportionnalité" (=valeur de la col à indice k) * 2 + la valeur min
    # r_xe = XE[s]*0.5 + 0.05
    # r_n = N[s]*0.5 + 0.05
    # r_w = W[s]*0.5 + 0.05

    ax[2].set_xlim([-1,1]) # Définit un cadre pour l'image 
    ax[2].set_ylim([-1,1])
    ax[2].axis("off")
    
    ax[2].imshow(im_xc, extent=[-r_xc-0.5, r_xc-0.5, -r_xc-0.5, r_xc-0.5]) #image en carré ; 0,5 = éloignement par rapport au centre 
    # ax[2].imshow(im_xe, extent=[-r_xe-0.5, r_xe-0.5, -r_xe+0.5, r_xe+0.5])
    # ax[2].imshow(im_n, extent=[-r_n+0.5, r_n+0.5, -r_n+0.5, r_n+0.5])
    # ax[2].imshow(im_w, extent=[-r_w+0.5, r_w+0.5, -r_w-0.5, r_w-0.5])


    if k==time//skip - 1 :
        finalText()

if __name__=='__main__':

    # Importations données graph+im
    print("Entering in interface")
    time = 1000
    skip = 5

    fnameMfile = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_C/results_python_file.txt"
    fnameMcurs = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_C/results_python_cursors.txt"
    fnamePfile = "/Users/peppa/Desktop/Ba3/CMT/PROJECT/HANDY_PROJECT/in_C/results_python_file.txt"
    fnamePcurs = "/Users/peppa/Desktop/Ba3/CMT/PROJECT/HANDY_PROJECT/in_C/results_python_curs.txt"

    [XC, XE, N, W, variables, parameters] = readFile(fnamePfile)
    t = [i for i in range(time)]

    xc = str(variables[1])
    xe = str(variables[2])
    n = str(variables[3])
    w = str(variables[4])
    am = str(parameters[1])
    aM = str(parameters[2])
    bc = str(parameters[3])
    be = str(parameters[4])
    g = str(parameters[5])
    l = str(parameters[6])
    s = str(parameters[7])
    d = str(parameters[8])
    k = str(parameters[9])
    r = str(parameters[10])

    interface, ax = plt.subplots(1, 3, figsize=(13,6.5))

    stateText()

    ax[1].set_xlim(-20, 1020)
    ax[1].set_ylim(-0.03, 1.03)

    #im_xc = Image.open("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/Images/im1.jpg") 
    im_xc = Image.open("Images/im1.jpg") 
    
    # im_xe = Image.open("images/im2.jpg")
    # im_n = Image.open("images/im3.jpg") 
    # im_w = Image.open("images/im4.jpg") 

    ani = FuncAnimation(fig = interface, func = animate, frames = range(time//skip), interval = 1, repeat = False)

    plt.axis("equal")
    plt.show()


# enregistrer la vidéo ?
# courbe inclusive
