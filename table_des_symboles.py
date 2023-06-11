

class ListSymbole():
    def __init__(self):
        self.listSymboles= []

    class Symbole:
        def __init__(self,nom,type):
            self.nom=nom
            self.type=type
    def addSymbole(self,nom,type):
        self.listSymboles.append( self.Symbole(nom,type))
    def get(self,nom):
        for symbole in ListSymbole:
            if symbole.nom==nom:
                return symbole
        return None

