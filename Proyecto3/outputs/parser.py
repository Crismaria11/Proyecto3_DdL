class Parser:
	def __init__(self, tokens):
		self.tokens = tokens
		self.id_token = 0
		self.actual_token = self.tokens[self.id_token]
		self.last_token = ''
	def advance( self ):
		self.id_token += 1
		if self.id_token < len(self.tokens):
			self.actual_token = self.tokens[self.id_token]
			self.last_token = self.tokens[self.id_token - 1]

	def expect(self, item, arg = None):
		try:
			og = self.id_token
			possible = False
			if item != None:
				try:
					if arg == None:
						ans = item()
					else:
						ans = item(arg)
					if type(ans) == bool:
						possible = ans
					else:
						possible = True
				except:
					possible = False
			self.id_token = og
			self.actual_token = self.tokens[self.id_token]
			self.last_token = self.tokens[self.id_token - 1]
			return possible
		except:
			print('')

	def read(self, item, type = False):
		if type:
			if self.actual_token.type == item:
				self.advance()
				return True
			else:
				return False
		else:
			if self.actual_token.value == item:
				self.advance()
				return True
			else:
				return False
	value, result, value1, value2 = 0,0,0,0

	def EstadoInicial(self):
		while self.expect(self.Instruccion()):
			self.Instruccion()
			self.read(";")
		self.read(".")

	def Instruccion(self):
		resultado = 0
		resultado=self.Expresion(resultado)
		print(str(resultado))

	def Expresion(self,resultado):
		resultado1, resultado2 = 0, 0
		resultado1=self.Termino(resultado1)
		while self.expect(self.read("+")):
			self.read("+")
			resultado2=self.Termino(resultado2)
			resultado1+=resultado2
		resultado=resultado1
		return resultado

	def Termino(self,resultado):
		resultado1, resultado2 =  0,0
		resultado1=self.Factor(resultado1)
		while self.expect(self.read("*")):
			self.read("*")
			resultado2=self.Factor(resultado2)
			resultado1*=resultado2
		resultado=resultado1
		return resultado

	def Factor(self,resultado):
		signo=1
		if self.expect(self.Number(resultado)):
			resultado=self.Number(resultado)
			
		elif self.expect(self.read("(")):
			self.read("(")
			resultado=self.Expresion(resultado)
			self.read(")")
		resultado*=signo
		return resultado

	def Number(self,resultado):
		self.read('numero', True)
		resultado = int(self.last_token.value)
		return resultado

