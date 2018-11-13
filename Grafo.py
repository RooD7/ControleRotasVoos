import Aresta
import Vertice


class Grafo(object):
	def __init__(self, direcionado=True):
		self.vertices = []
		self.arestas = []
		self.direcionado = direcionado
		self.caminho = []

	def novoVertice(self, ide):
		self.vertices.append(Vertice.Vertice(ide))

	def buscaVertice(self, ide):
		for v in self.vertices:
			if v.getId() == ide:
				return v
		else:
			return None

	def novaAresta(self, vOrigem, vDestino, dist):
		orig = self.buscaVertice(vOrigem)
		dest = self.buscaVertice(vDestino)

		# se os vertices da aresta existem
		if (orig is not None) and (dest is not None):
			a = Aresta.Aresta(orig, dest, dist)
			self.arestas.append(a)

			# grafo nao direcionado
			if not self.direcionado:
				self.arestas.append(Aresta.Aresta(dest, orig, dist))
			return a
		else:
			return None

	def buscaAresta(self, origem, destino):
		# origem e destino sao strings
		for a in self.arestas:
			if ((a.getOrigem().getId() == origem) and
					(a.getDestino().getId() == destino)):
				return a
		return None

	def verticeAdjacente(self, v):
		for a in self.arestas:
			if ((a.getOrigem().getId() == v.getId()) and
					(not a.getDestino().getVisitado())):
				# Para nao retornar o mesmo vertice
				a.getDestino().setVisitado(True)
				return a.getDestino()
		return None

	def menorVerticeAdjacente(self, v):
		menorDist = 999999
		menor = None
		for a in self.arestas:
			if ((a.getOrigem().getId() == v.getId()) and
					(not a.getDestino().getVisitado())):
				# Para nao retornar o mesmo vertice
				a.getDestino().setVisitado(True)
				if menorDist > int(v.getEstimativa()) + int(a.getDist()):
					menorDist = int(v.getEstimativa()) + int(a.getDist())
					menor = a.getDestino()
		return menor

	def vazio(self):
		if len(self.vertices) == 0:
			return True
		else:
			return False

	def buscaLargura(self, v1, v2):
		self.visitarVertice(v1)
		adj = self.verticeAdjacente(v1)  # retorna apenas não visitado ou nulo
		while adj is not None:
			adj.getPredecessor().append(v1.getId())
			self.caminho.append(v1.getId())
			if adj.__eq__(v2):
				self.caminho.append(v2.getId())
				self.caminho.append('FIM')
				return None
			else:
				self.buscaLargura(adj, v2)
				adj = self.verticeAdjacente(v1)
		if len(self.caminho) != 0 and self.caminho[len(self.caminho) - 1] != 'FIM':
			self.caminho.pop()

	def visitarVertice(self, vert):
		for v in self.vertices:
			if (v.getId() == vert.getId()):
				v.setVisitado(True)
				break

	def getVertice(self, vert):
		for v in self.vertices:
			if v.getId() == vert:
				return v
		return None

	def getVertices(self):
		return self.vertices

	def getArestas(self):
		return self.arestas

	def getCaminho(self):
		if len(self.caminho) != 0 and self.caminho[len(self.caminho) - 1] == 'FIM':
			self.caminho.pop()
		return self.caminho

	def clearCaminho(self):
		self.caminho = []

	def printCaminho(self):
		if len(self.caminho) == 0:
			print('Não existe caminho possível!')
		else:
			strg = ''
			for i in range(len(self.caminho) - 1):
				strg += '%s -> ' % self.caminho[i]
			strg += '%s.' % self.caminho[len(self.caminho) - 1]
			print(strg)
