import tkinter
from tkinter import messagebox
import time
canvasWidth = 750
canvasHeight = 500
fenêtre = tkinter.Tk()
fenêtre.title("Pong")
canvas = tkinter.Canvas(fenêtre, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
canvas.pack()
raquette = canvas.create_rectangle(0, 0, 40, 10, fill="dark turquoise")
balle = canvas.create_oval(0, 0, 10, 10, fill="deep pink")
fenêtreOuverte = True
score = 0
compteRebonds = 0
def boucle_principale():
    while fenêtreOuverte == True:
        déplacer_raquette()
        déplacer_balle()
        fenêtre.update()
        time.sleep(0.02)
        if fenêtreOuverte == True:
            vérifier_game_over()
gaucheAppuyé = 0
droiteAppuyé = 0
def quand_touche_appuyée(event):
    global gaucheAppuyé, droiteAppuyé
    if event.keysym == "Left":
        gaucheAppuyé = 1
    elif event.keysym == "Right":
        droiteAppuyé = 1
def quand_touche_relâchée(event):
    global gaucheAppuyé, droiteAppuyé
    if event.keysym == "Left":
        gaucheAppuyé = 0
    elif event.keysym == "Right":
        droiteAppuyé = 0
vitesseRaquette = 6
def déplacer_raquette():
    mouvRaquette = vitesseRaquette*droiteAppuyé - vitesseRaquette*gaucheAppuyé
    (gaucheRaquette, hautRaquette, droiteRaquette, basRaquette) = canvas.coords(raquette)
    if ((gaucheRaquette > 0 or mouvRaquette > 0) and (droiteRaquette < canvasWidth
    or mouvRaquette < 0)):
        canvas.move(raquette, mouvRaquette, 0)
mouvBalleX = 4
mouvBalleY = -4
défHautRaquette = canvasHeight-40
défBasRaquette = canvasHeight-30
def déplacer_balle():
    global mouvBalleY, mouvBalleX, score, compteRebonds, vitesseRaquette
    (gaucheBalle, hautBalle, droiteBalle, basBalle) = canvas.coords(balle)
    if mouvBalleX > 0 and droiteBalle > canvasWidth:
        mouvBalleX = -mouvBalleX
    if mouvBalleX < 0 and gaucheBalle < 0:
        mouvBalleX = -mouvBalleX
    if mouvBalleY < 0 and hautBalle < 0:
        mouvBalleY = -mouvBalleY
    if mouvBalleY > 0 and basBalle > défHautRaquette and basBalle < défBasRaquette:
        (gaucheRaquette, hautRaquette, droiteRaquette, basRaquette) = canvas.coords(raquette)
        if droiteBalle > gaucheRaquette and gaucheBalle < droiteRaquette:
            mouvBalleY = -mouvBalleY
            score = score + 1
            compteRebonds = compteRebonds + 1
            if compteRebonds == 2:
                compteRebonds = 0
                vitesseRaquette = vitesseRaquette + 1
                if mouvBalleX > 0:
                    mouvBalleX = mouvBalleX + 1
                else:
                    mouvBalleX = mouvBalleX - 1
                mouvBalleY = mouvBalleY - 1
    canvas.move(balle, mouvBalleX, mouvBalleY)
def vérifier_game_over():
    (gaucheBalle, hautBalle, droiteBalle, basBalle) = canvas.coords(balle)
    if hautBalle > canvasHeight:
        print("Ton score :" + str(score))
        rejouer = tkinter.messagebox.askyesno(message="Veut-tu rejouer ?")
        if rejouer == True:
            réinitialiser()
        else:
            fermer()
def fermer():
    global fenêtreOuverte
    fenêtreOuverte = False
    fenêtre.destroy()
def réinitialiser():
    global score, compteRebonds, vitesseRaquette
    global gaucheAppuyé, droiteAppuyé
    global mouvBalleX, mouvBalleY
    score = 0
    compteRebonds = 0
    vitesseRaquette = 6
    gaucheAppuyé = 0
    droiteAppuyé = 0
    mouvBalleX = 4
    mouvBalleY = -4
    canvas.coords(raquette, 10, défHautRaquette, 50, défBasRaquette)
    canvas.coords(balle, 20, défHautRaquette-10, 30, défHautRaquette)
fenêtre.protocol("WM_DELETE_WINDOW", fermer)
fenêtre.bind("<KeyPress>", quand_touche_appuyée)
fenêtre.bind("<KeyRelease>", quand_touche_relâchée)
réinitialiser()
boucle_principale()
