from tkiteasy import ouvrirFenetre
from cellule import Cell

def chercher_cellule(tab_cell,x,y):
    for i in range(len(tab_cell)):
        if tab_cell[i].x == x-x%20 and tab_cell[i].y == y-y%20:
            return i

g=ouvrirFenetre(1195,697)
for i in range(60):
    g.dessinerLigne(i*20-1,0,i*20-1,700,"gray50")
for i in range(35):
    g.dessinerLigne(0,i*20-1,1200,i*20-1,"gray50")
cellule=[]
for i in range(66):
    for j in range(41):
        c = Cell()
        c.__int__(g,i*20-60,j*20-60,19)
        cellule.append(c)

fin = False
while not fin:
    touche = g.recupererTouche()
    if touche=="space":
        fin = True
    clic=g.recupererClic()
    if clic!=None:
        indice = chercher_cellule(cellule,clic.x,clic.y)
        cellule[indice].changer_etat_vie()
        cellule[indice].est_en_vie()

fin_jeux = False
while not fin_jeux:
    touche = g.recupererTouche()
    if touche=="space":
        fin_jeux = True
    for i in range(len(cellule)):
        cellule[i].actualise_nb_voisins_vivant(cellule)



    for i in range(len(cellule)):
        cellule[i].tour_suivant()

    g.actualiser()





g.fermerFenetre()