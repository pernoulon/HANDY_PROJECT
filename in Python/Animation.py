import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
from HANDY import Model as HANDY
from scipy.integrate import odeint
#%matplotlib inline


fname = "params_stable_equitable_2.txt"
model = HANDY(fname=fname) #fichier trouvé

x = [i for i in range(1000)]
XC = model.run_auto(norm=True)

# plt.plot(x,XC) graphe fixe
# plt.show()

# Création de la figure et de l'axe

fig, ax = plt.subplots()

# Création de la ligne qui sera mise à jour au fur et à mesure
line, = ax.plot([],[], color='blue')
# point, = ax.plot([], [], ls="none", marker="o")

#Gestion des limites de la fenêtre
ax.set_xlim(-10, 1020)
ax.set_ylim(-0.5, 1)


# Création de la function qui sera appelée à "chaque nouvelle image"
def animate(k):
    #i = min(k, len(x))
    line.set_data(x[:k], XC[:k])

    return line,

# Génération de l'animation, frames précise les arguments numérique reçus par func (ici animate), 
# interval est la durée d'une image en ms, blit gère la mise à jour
ani = FuncAnimation(fig=fig, func=animate, frames=range(len(x)), interval=1, repeat = False, blit=True)
plt.show()


# enregistrer la vidéo ?

# from IPython.display import HTML
# plt.rcParams["animation.writer"] = "mencoder"
# HTML(ani.to_html5_video())
