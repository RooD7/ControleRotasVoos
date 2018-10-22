import Aresta
import Vertice

class Grafo(object):
	def __init__(self, direcionado=True):
		self.vertices = []
		self.arestas = []
		self.direcionado = direcionado

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
			if ((a.getOrigem().__eq__(Vertice.Vertice(origem))) and 
				(a.getDestino().__eq__(Vertice.Vertice(destino)))):
				return a
		return None

	def verticeAdjacente(self, v):
		for a in self.arestas:
			if ((a.getOrigem().getId() == v.getId()) and 
				(not a.getDestino().getVisitado())):
				# Para nao retornar o mesmo vertice
				a.getDestino().setVisitado(True)
				return a.getDestino()
			else:
				return None
		
	def vazio(self):
		if len(self.vertices) == 0:
			return True
		else:
			return False

	def visita(self, v1, v2):
		print('Partindo do vertice '+str(v1.getId())+', visitamos o vertice '+str(v2.getId())+'.')
		v1.setVisitado(True)
		adj = self.verticeAdjacente(v1)  # retorna apenas não visitado ou nulo
		while adj is not None:
			adj.getPredecessor().append(v1.getId())
			self.visita(adj)
			adj = self.verticeAdjacente(v1)
		print("Voltando para: ", v1.getPredecessor())

	def getVertices(self):
		return self.vertices

	def getArestas(self):
		return self.arestas