"""
Affiche une chaine de caractère avec une certaine identation
"""
def afficher(s,indent=0):
	print(" "*indent+s)
	
class Programme:
	def __init__(self,listeInstructions):
		self.listeInstructions = listeInstructions
	def afficher(self,indent=0):
		afficher("<programme>",indent)
		self.listeInstructions.afficher(indent+1)
		afficher("</programme>",indent)

class ListeInstructions:
	def __init__(self):
		self.instructions = []
	def afficher(self,indent=0):
		afficher("<listeInstructions>",indent)
		for instruction in self.instructions:
			instruction.afficher(indent+1)
		afficher("</listeInstructions>",indent)
			
class Ecrire:
	def __init__(self,exp):
		self.exp = exp
	def afficher(self,indent=0):
		afficher("<ecrire>",indent)
		self.exp.afficher(indent+1)
		afficher("</ecrire>",indent)

class Lire:
	def __init__(self):
		pass
	
	def afficher(self,indent=0):
		afficher("<lire>",indent)
		afficher("</lire>",indent)

class Assignement:
	def __init__(self,nom,valeur):
		self.nom=nom
		self.valeur=valeur
	def afficher(self,indent=0):
		afficher("<variable>",indent)
		self.nom.afficher(indent+1)
		self.valeur.afficher(indent+1)
		afficher("</variable>",indent)

class Recuperation:
	def __init__(self,nom):
		self.nom=nom
	def afficher(self,indent=0):
		afficher("<variable>")


class Operation:
	def __init__(self,op,exp1,exp2):
		self.exp1 = exp1
		self.op = op
		self.exp2 = exp2
	def afficher(self,indent=0):
		afficher("<operation>",indent)
		afficher(self.op,indent+1)
		self.exp1.afficher(indent+1)
		self.exp2.afficher(indent+1)
		afficher("</operation>",indent)


class Entier:
	def __init__(self,valeur):
		self.valeur = valeur
	def afficher(self,indent=0):
		afficher("[Entier:"+str(self.valeur)+"]",indent)

class Booleen:
    def __init__(self,valeur):
        self.valeur = valeur
    def afficher (self, indent=0):
        afficher("[Booleen : "+self.valeur+"]",indent)


class SuperExpression:
	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2

	def afficher(self, indent=0):
		afficher("<super expression>", indent)
		self.expr1.afficher(indent+1)
		self.expr2.afficher(indent+1)
		afficher("<super expression>", indent)


class Fonction:
	def __init__(self, nom, expr):
		self.nom = nom
		self.expr = expr

	def afficher(self,indent=0):
		afficher('<fonction>', indent)
		self.nom.afficher(indent+1)
		self.expr.afficher(indent+1)
		afficher('<fonction>', indent)