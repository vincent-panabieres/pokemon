class Type(Pokemon):
    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        super().__init__(nom, pv, niveau, attaque, defense)
        
    def modif_pv(self):
        pass
    
    def modif_attaque(self):
        pass 
    
    def modif_defense(self):
        pass 
