class Cell:
    def __int__(self,g,x,y,cote):
        self.en_vie=False
        self.graf=g
        self.x=x
        self.y=y
        self.nb_voisin_vivant=0
        self.cote=cote
        self.objet_grafique=g.dessinerRectangle(x,y,cote,cote,"white")

    def est_en_vie(self):
        if self.en_vie:
            self.graf.changerCouleur(self.objet_grafique,"black")
        else:
            self.graf.changerCouleur(self.objet_grafique,"white")

    def changer_etat_vie(self):
        if self.en_vie:
            self.en_vie=False
        else:
            self.en_vie=True


    def actualise_nb_voisins_vivant(self,cellule_tab):
        self.nb_voisin_vivant=0
        for cel in cellule_tab:
            if  (abs(self.y-cel.y)<=20 and abs(self.x-cel.x)<=20) and not (self.x==cel.x and self.y==cel.y):
                if cel.en_vie:
                    self.nb_voisin_vivant+=1

    def tour_suivant(self):
        if self.en_vie:
            if self.nb_voisin_vivant in [2,3]:
                return
            if self.nb_voisin_vivant in [0,1,4,5,6,7,8,9]:
                self.changer_etat_vie()
                self.est_en_vie()
                return
        elif not self.en_vie:
            if self.nb_voisin_vivant ==3:
                self.changer_etat_vie()
                self.est_en_vie()
                return