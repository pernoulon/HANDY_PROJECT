from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import os
import argparse

parser = argparse.ArgumentParser(description="File sent from C")
parser.add_argument("--fileName", type=str, help="fichier C", default="../in_C/results_python_file.txt")
parser.add_argument("--scenario", type=str, help="type of scenario chosen", default="egalitarian")



def sendCursors():
    scenario_cursors = []
    k = []
    if args.scenario == "egalitarian" :
        scenario_cursors.append("eg_c")
        k.append("no change")
    if args.scenario == "equitable" :
        scenario_cursors.append("eq_c")
        k.append("no change")
    if args.scenario == "unequal" :
        scenario_cursors.append("un_c")
        k.append(str(curseurk.get()))

    d = str(curseurd.get())

    variables = [scenario_cursors[0], k[0], d]
    # os.chdir("in_C")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + variables[0] + " " + variables[1] + " " + variables[2])

    fen_princ.destroy()

def print_k() :
    text_k = "k : " + str(curseurk.get())
    k_label.configure(text= text_k)
def print_d() :
    text_d = "d : " + str(curseurd.get())
    d_label.configure(text= text_d)

def cursors():
    global curseurk
    global k_label
    global curseurd
    global d_label

    if args.scenario == "egalitarian" or args.scenario == "equitable" :
        next_graph_label= Label(fen_princ, text = "You can now chose a new parameter : d.", width=70).grid(row= 0,column=1)

        curseurd = Scale(fen_princ, orient='horizontal', from_ = 1.25, to = 10)
        curseurd.grid(row=4, column=1)
        d_label = Label(fen_princ, text = "Value for d", width=70)
        d_label.grid(row=5, column=1)
        monBoutond = Button(fen_princ, text = "Validate value for D", command = print_d).grid(row=6, column=1)
        
        monBoutongo = Button(fen_princ, text = "Launch scenario", command = sendCursors).grid(row=7, column=1)

        
    if args.scenario == "unequal" :
        next_graph_label= Label(fen_princ, text = "You can now chose two starting parameters : k and d.", width=70).grid(row= 0,column=1)

        curseurk = Scale(fen_princ, orient='horizontal', from_ = 0, to = 100)
        curseurk.grid(row=1, column=1)
        k_label = Label(fen_princ, text = "Value for k", width=70)
        k_label.grid(row=2, column=1)
        monBoutonk = Button(fen_princ, text = "Validate value for K", command = print_k).grid(row=3, column=1)

        curseurd = Scale(fen_princ, orient='horizontal', from_ = 1.25, to = 10)
        curseurd.grid(row=4, column=1)
        d_label = Label(fen_princ, text = "Value for d", width=70)
        d_label.grid(row=5, column=1)
        monBoutond = Button(fen_princ, text = "Validate value for D", command = print_d).grid(row=6, column=1)
        
        monBoutongo = Button(fen_princ, text = "Launch scenario", command = sendCursors).grid(row=7, column=1)



def readFile(fname):

    array = np.genfromtxt(fname, delimiter=', ', skip_header=3, dtype=float)
    XC = array[:,0]
    XE = array[:,1]
    N = array[:,2]
    W = array[:,3]
    f = open(fname, "r")
    variables = [f.readline()]
    variables = variables[0].split(", ")
    parameters = [f.readline()]
    parameters = parameters[0].split(", ")
    
    return [XC, XE, N ,W, variables, parameters]

def animate(k, XC, XE, N, W):

    s = k*skip
    
    if k==0:
        ax.legend(loc='upper left', bbox_to_anchor=(-0.1, -0.06),
        fancybox=True, shadow=True, ncol=4, fontsize='xx-small')

    ax.plot(t[:s], XC[:s], color = 'b', label = "Commoner population")
    ax.plot(t[:s], XE[:s], color = 'r', label = "Elite population")
    ax.plot(t[:s], N[:s], color = 'g', label = "Nature")
    ax.plot(t[:s], W[:s], color = 'k', label = "Wealth")

    if k==(time//skip)-1:
        cursors()


def backFen1():
    os.system("python ../in_Python/fen1.py")
    fen_princ.destroy()
def quit():
    fen_princ.destroy()

# développer textes
def welcomeEg():
    text_welcome = """WELCOME TO YOUR EGALITARIAN MODELISATION\n
                    No elite."""
    return text_welcome
def welcomeEq():
    text_welcome = """WELCOME TO YOUR EQUITABLE MODELISATION\n
                    Elites with same salaries as Commoners."""
    return text_welcome
def welcomeUn():
    text_welcome = """WELCOME TO YOUR UNEQUAL MODELISATION\n
                    Elites with inequalities in salaries."""
    return text_welcome



if __name__=='__main__':

    args = parser.parse_args()
    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)

    text_welcome = []
    if args.scenario == "egalitarian" :
        text_welcome.append(welcomeEg())
    if args.scenario == "equitable" :
        text_welcome.append(welcomeEq())
    if args.scenario == "unequal" :
        text_welcome.append(welcomeUn())

    welcome_label = Label(fen_princ, text = text_welcome[0], width=70).grid(row= 0,column=0)
    home_button = Button(fen_princ, text = "Back to Home", command = backFen1).grid(row=1, column=0)
    end_button = Button(fen_princ, text = "Quit Model", command = quit).grid(row=2, column=0)

    time = 1000
    skip = 20
    
    [XC, XE, N, W, variables, parameters] = readFile(args.fileName)
    t = [i for i in range(time)]

    interface, ax = plt.subplots(figsize=(4,3))

    ax.set_xlim(-20, 1020)
    ax.set_ylim(-0.03, 1.03)
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)

    canvas = FigureCanvasTkAgg(interface, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=190)

    ani = FuncAnimation(fig = interface, func = animate, fargs = (XC,XE,N,W), frames = range(time//skip), interval = 1, repeat = False)

    fen_princ.mainloop()

