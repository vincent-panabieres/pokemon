class Pokemon:
    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        self.__nom = nom
        self.__pv = pv
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense
    
    def get_nom(self):
        return self.__nom
    
    def get_pv(self):
        return self.__pv
    
    def set_pv(self, value):
        self.__pv = value
    
    def afficher_infos(self):
        print(f"{self.__nom} ({type(self).__name__}), PV: {self.__pv}, Niveau: {self.niveau}, Attaque: {self.attaque}, Defense: {self.defense}")
