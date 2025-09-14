from tkinter import *
import random
import time

class Balle:
    def __init__(self, canvas, raquette, couleur):
        self.canvas = canvas
        self.raquette = raquette
        self.id = canvas.create_oval(10, 10, 25, 25, fill=couleur)
        self.canvas.move(self.id, 245, 100)
        departs = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(departs)
        self.y = -3
        self.hauteur_canvas = self.canvas.winfo_height()
        self.largeur_canvas = self.canvas.winfo_width()

    def new_method(self, canvas):
        self.canvas = canvas
    
    def dessiner(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.largeur_canvas :
            self.x = self.x * -1
        if pos[1] <= 0 or pos[3] >= self.hauteur_canvas :
            self.y = self.y * -1

class Raquette:
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=couleur)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.largeur_canvas = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.vers_gauche)
        self.canvas.bind_all("<KeyPress-Right>", self.vers_droite)
        self.canvas.bind_all("<KeyRelease-Left>", self.arreter)
        self.canvas.bind_all("<KeyRelease-Right>", self.arreter)
    
    def dessiner(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.largeur_canvas:
            self.x = 0
    
    def vers_gauche(self, evt):
        self.x = -2
    
    def vers_droite(self, evt):
        self.x = 2

    def arreter(self, evt):
        self.x = 0

tk = Tk()
tk.title("Essai !")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

raquette = Raquette(canvas, "blue")
balle = Balle(canvas, raquette, "dark orange")

while True:
    balle.dessiner()
    raquette.dessiner()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
