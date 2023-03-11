import random

class Combat:
    def __init__(self, joueur, adversaire):
        self.joueur = joueur
        self.adversaire = adversaire
        self.tour = 1
        
    def est_termine(self):
        return self.joueur.est_ko() or self.adversaire.est_ko()
    
    def get_vainqueur(self):
        if self.joueur.est_ko() and self.adversaire.est_ko():
            return "Match nul"
        elif self.joueur.est_ko():
            return self.adversaire.nom
        else:
            return self.joueur.nom
    
    def attaque_reussie(self):
        return random.randint(0, 1) == 1
    
    def degats_infliges(self, attaquant, defenseur):
        multiplicateur = attaquant.get_multiplicateur_type(defenseur.type)
        degats = attaquant.attaque * multiplicateur - defenseur.defense
        return max(0, degats)
    
    def tour_suivant(self):
        print(f"Tour {self.tour}")
        attaquant, defenseur = self.joueur, self.adversaire
        if self.tour % 2 == 0:
            attaquant, defenseur = self.adversaire, self.joueur
            
        if not attaquant.est_ko():
            if self.attaque_reussie():
                degats = self.degats_infliges(attaquant, defenseur)
                defenseur.subir_degats(degats)
                print(f"{attaquant.nom} inflige {degats} dégâts à {defenseur.nom}")
            else:
                print(f"{attaquant.nom} rate son attaque")
        
        self.tour += 1
