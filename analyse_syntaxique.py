import sys
from sly import Parser
from analyse_lexicale import FloLexer
import arbre_abstrait

class FloParser(Parser):
	# On récupère la liste des lexèmes de l'analyse lexicale
	tokens = FloLexer.tokens

	# Règles gramaticales et actions associées

	@_('listeInstructions')
	def prog(self, p):
		return arbre_abstrait.Programme(p[0])

	@_('instruction')
	def listeInstructions(self, p):
		l = arbre_abstrait.ListeInstructions()
		l.instructions.append(p[0])
		return l
					
	@_('instruction listeInstructions')
	def listeInstructions(self, p):
		p[1].instructions.insert(0,p[0])
		return p[1]
		
	@_('ecrire')
	def instruction(self, p):
		return p[0]
	
			
	@_('ECRIRE "(" expr ")" ";"')
	def ecrire(self, p):
		return arbre_abstrait.Ecrire(p.expr) #p.expr = p[2]
		
	##@_('expr "+" expr')
	##def expr(self, p):
	##	return arbre_abstrait.Operation('+',p[0],p[2])

	##@_('expr "*" expr')
	##def expr(self, p):
	##	return arbre_abstrait.Operation('*',p[0],p[2])


	@_('"(" expr ")"')
	def fact(self, p):
		return p[1]
		
	@_('ENTIER')
	def fact(self, p):
		return arbre_abstrait.Entier(p.ENTIER) #p.ENTIER = p[0]
	
	@_('fact')
	def produit(self,p):
		return p.fact
	
	@_('expr "+" produit')
	def expr(self,p):
		return arbre_abstrait.Operation('+',p[0],p[2])
	
	@_('produit')
	def expr(self,p):
		return p[0]
	
	@_('expr "-" produit')
	def expr(self,p):
		return arbre_abstrait.Operation('-',p[0],p[2])

	@_('"-" fact')
	def produit(self,p):
		return arbre_abstrait.Operation('*',arbre_abstrait.Entier(-1),p[1])

	@_('produit "*" fact')
	def produit(self,p):
		return arbre_abstrait.Operation('*',p[0],p[2])

	@_('produit "/" fact')
	def produit(self,p):
		return arbre_abstrait.Operation('/',p[0],p[2])

	@_('produit "%" fact')
	def produit(self,p):
		return arbre_abstrait.Operation('%',p[0],p[2])
	
	@_('expr "<" expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('<',p[0],p[2])
	
	@_('expr ">" expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('>',p[0],p[2])
	
	@_('expr EGAL expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('=',p[0],p[2])
	
	@_('expr INFERIEUR_OU_EGAL expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('<=',p[0],p[2])
	
	@_('expr SUPERIEUR_OU_EGAL expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('>=',p[0],p[2])
	
	@_('expr DIFFERENT expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('!=',p[0],p[2])
	
	
	
	@_('LIRE "(" ")"')
	def expr(self,p):
		return arbre_abstrait.Lire()
	
	@_('IDENTIFIANT')
	def variable(self,p):
		return arbre_abstrait.Variable(p[0])
	
	@_('variable')
	def fact(self, p):
		return p[0]

	@_('expr "," expr',
    'superExpression "," expr')
	def superExpression(self, p):
		return arbre_abstrait.SuperExpression(p[0], p[2])

	@_('IDENTIFIANT "(" expr ")"',
    'IDENTIFIANT "(" superExpression ")" ')
	def fact(self,p):
		return arbre_abstrait.Fonction(p[0],p[2])

	@_('VRAI')
	def booleen(self,p):
		return arbre_abstrait.Booleen(True)

	@_('FAUX')
	def booleen(self,p):
		return arbre_abstrait.Booleen(False)
    
	@_("booleen")
	def expr(self,p):
		return p[0]
		
	
	@_("expr ET expr")
	def expr(self,p):
		return arbre_abstrait.LogOp("et",p[0],p[2])	
	
	@_("expr OU booleen")
	def expr(self,p):
		return arbre_abstrait.LogOp("ou",p[0],p[2])
	
	@_("NON booleen")
	def expr(self,p):
		return arbre_abstrait.NegLogOp(p[1])
	
	
	@_('SI "(" expr ")" "{" listeInstructions "}" condSuite')
	def instruction(self, p):
		conditions = [p[2]]
		instructions = [p[5]]

		a,b = p[7]
		conditions.extend(a)
		instructions.extend(b)
		return arbre_abstrait.Conditionnelle(conditions,instructions)
	
	
	@_('SINON_SI "(" expr ")" "{" listeInstructions "}" condSuite')
	def condSuite(self, p):
		a,b = p[7]
		return ([p[2]] + a, [p[5]] + b)
	

	@_('SINON "{" listeInstructions "}" ')
	def condSuite(self, p):
		return ([None], [p[2]])

	@_('')
	def condSuite(self, p):
		return ([], [])
	

	@_('TANT_QUE "(" expr ")" "{" listeInstructions "}"')
	def instruction(self,p):
		return arbre_abstrait.TantQue(p[2], p[5])

	

if __name__ == '__main__':
	lexer = FloLexer()
	parser = FloParser()
	if len(sys.argv) < 2:
		print("usage: python3 analyse_syntaxique.py NOM_FICHIER_SOURCE.flo")
	else:
		with open(sys.argv[1],"r") as f:
			data = f.read()
			try:
				arbre = parser.parse(lexer.tokenize(data))
				arbre.afficher()
			except EOFError:
				exit()