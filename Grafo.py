import Aresta
import Vertice

class Grafo(object):
	def __init__(self, direcionado=True):
		self.vertices = []
		self.arestas = []
		self.direcionado = direcionado

	def novoVertice(self, ide):
		self.vertices.append(Vertice(ide))

	def buscaVertice(self, ide):
		for v in self.vertices:
			if v.getId() == ide:
				return v
		else:
			return None

	def novaAresta(self, vOrigem, vDestino, peso):
		orig = self.buscaVertice(vOrigem)
		dest = self.buscaVertice(vDestino)

		# se os vertices da aresta existem
		if (orig is not None) and (dest is not None):
			a = Aresta(orig, dest, peso)
			self.arestas.append(a)

			# grafo nao direcionado
			if not self.direcionado:
				self.arestas.append(Aresta(dest, orig, peso))
			return a
		else:
			return None


	def buscaAresta(self, vOrigem, vDestino):
		for a in self.arestas:
			if ((a.getOrigem().getId() == vOrigem.getId()) and 
				(a.getDestino().getId() == vDestino.getId())):
				return a

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