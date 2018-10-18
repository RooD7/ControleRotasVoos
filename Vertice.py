class Vertice(object):
	def __init__(self,id):
		self.id = id
		self.estimativa = 99999999
		self.visitado = False
		self.predecessor = []

	def setId(self, id):
		self.id = id

	def getId(self):
		return self.id

	def setVisitado(self, valor):
		self.visitado = valor

	def getVisitado(self):
		return self.visitado

	def setEstimativa(self, estimativa):
		self.estimativa = estimativa

	def getEstimativa(self):
		return self.estimativa

	# string
	def __str__(self):
		return (" Vertice  : %s \n Estimativa: %i \n" % 
			(self.id, self.estimativa))

	# equals
	def __eq__(self, v):
		return self.id == v.id

	def __eq__(self, v):
		return self.estimativa == v.estimativa

	# menor
	def __lt__(self, v):
		return self.estimativa < v.estimativa

	# maior
	def __gt__(self, v):
		return self.estimativa > v.estimativa
