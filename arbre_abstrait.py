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
		self.listeInstructions.afficher(indent+2)
		afficher("</programme>",indent)

class ListeInstructions:
	def __init__(self):
		self.instructions = []
	def afficher(self,indent=0):
		afficher("<listeInstructions>",indent)
		for instruction in self.instructions:
			instruction.afficher(indent+2)
		afficher("</listeInstructions>",indent)
			
class Ecrire:
	def __init__(self,exp):
		self.exp = exp
	def afficher(self,indent=0):
		afficher("<ecrire>",indent)
		self.exp.afficher(indent+2)
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
		self.nom.afficher(indent+2)
		self.valeur.afficher(indent+2)
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
		afficher(self.op,indent+2)
		self.exp1.afficher(indent+2)
		self.exp2.afficher(indent+2)
		afficher("</operation>",indent)

class Comparaison:
	def __init__(self,op,exp1,exp2):
		self.exp1 = exp1
		self.op = op
		self.exp2 = exp2

	def afficher(self,indent=0):
		afficher("<Comparaison>",indent)
		afficher("[Comparateur : " + self.op + "]",indent+2)
		self.exp1.afficher(indent+2)
		self.exp2.afficher(indent+2)
		afficher("</Comparaison>",indent)

class Entier:
	def __init__(self,valeur):
		self.valeur = valeur
	def afficher(self,indent=0):
		afficher("[Entier : " + str(self.valeur) + "]", indent)

class Booleen:
    def __init__(self,valeur):
        self.valeur = valeur
    def afficher (self, indent=0):
        afficher("[Booleen : " + str(self.valeur) + "]", indent)

class LogOp:
	def __init__(self,op,exp1,exp2):
		self.exp1 = exp1
		self.op = op
		self.exp2 = exp2

	def afficher(self,indent=0):
		afficher("<LogOp>",indent)
		afficher("[LogOp : " + self.op + "]",indent+2)
		self.exp1.afficher(indent+2)
		self.exp2.afficher(indent+2)
		afficher("</LogOp>",indent)

class NegLogOp:
	def __init__(self,exp):
		self.exp = exp

	def afficher(self,indent=0):
		afficher("<NegLogOp>",indent)
		afficher("[NegLogOp : non]",indent+2)
		self.exp.afficher(indent+2)
		afficher("</NegLogOp>",indent)

class SuperExpression:
	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2

	def afficher(self, indent=0):
		afficher("<super expression>", indent)
		self.expr1.afficher(indent+2)
		self.expr2.afficher(indent+2)
		afficher("</super expression>", indent)

class Fonction:
	def __init__(self, nom, expr):
		self.nom = nom
		self.expr = expr

	def afficher(self,indent=0):
		afficher('<fonction>', indent)
		self.nom.afficher(indent+2)
		self.expr.afficher(indent+2)
		afficher('</fonction>', indent)

class Variable:
	def __init__(self, nom):
		self.nom = nom
	
	def afficher(self, indent):
		afficher("<variable>", indent)
		afficher(self.nom, indent+2)
		afficher("</variable>", indent)

class Conditionnelle:
	def __init__(self,expressions: list, instructions: list):
		self.expressions = expressions
		self.instructions = instructions
	def afficher(self,indent=0):
		afficher("<Conditionnelle>",indent)
		afficher("<Si>",indent+2)
		self.expressions[0].afficher(indent+2)
		afficher("</Si>",indent)
		afficher("<Alors>",indent)
		self.instructions[0].afficher(indent+2)
		afficher("</Alors>",indent)
		for i in range(1,len(self.expressions)):
			if self.expressions[i] != None:
				afficher("<SinonSi>",indent)
				self.expressions[i].afficher(indent+2)
				afficher("</SinonSi>",indent)
				afficher("<Alors>",indent)
				self.instructions[i].afficher(indent+2)
				afficher("</Alors>",indent)
			else:
				afficher("<Sinon>",indent+2)
				self.instructions[i].afficher(indent+2)
				afficher("</Sinon>",indent+2)
		afficher("</Conditionnelle>",indent)

class TantQue:
	def __init__(self,condition,faire):
		self.condition = condition
		self.faire = faire
	def afficher(self,indent=0):
		afficher("<tantQue>",indent)
		self.condition.afficher(indent+1)
		self.faire.afficher(indent+1)
		afficher("</tantQue>",indent)

class Retourner:
	def __init__(self, expr):
		self.expr = expr
	def afficher(self, indent = 0):
		afficher("<retourner>", indent)
		self.expr.afficher(indent+1)
		afficher("</retourner>", indent)

class Declaration:
	def __init__(self, type, nom):
		self.type = type
		self.nom = nom
	def afficher(self, indent = 0):
		afficher("<declaration>", indent)
		afficher("[type = " + self.type + "]", indent + 1)
		afficher("[nom = " + self.nom + "]", indent + 1)
		afficher("</declaration>", indent)

class Affectation:
	def __init__(self, nom, expression):
		self.nom = nom
		self.expression = expression
	def afficher(self, indent = 0):
		afficher("<affectation>",indent)
		afficher("[nom = " + self.nom + "]", indent + 1)
		self.expression.afficher(indent + 1)
		afficher("</affectation>",indent)

class DeclarationAffectation:
	def __init__(self, type, nom, expression):
		self.type = type
		self.nom = nom
		self.expression = expression
	def afficher(self, indent = 0):
		afficher ("<declaration>", indent)
		afficher("[type = " + self.type + "]", indent + 1)
		afficher("[nom = " + self.nom + "]", indent + 1)
		afficher("<affectation>",indent + 1)
		afficher("[nom = " + self.nom + "]", indent + 2)
		self.expression.afficher(indent + 2)
		afficher("</affectation>",indent + 1)
		afficher ("<declaration>", indent)