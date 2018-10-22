import Grafo
import GrafoViz

class ErroFile(Exception):
	"""docstring for ErroSintatico"""
	def __init__(self, fl):
		self.file = fl

	def __str__(self):
		return "ERRO: não foi possivel abrir o arquivo "+str(self.file)+"\n"

class AppGrafos(object):
	def __init__(self):
		self.grafo = Grafo.Grafo()

	def caminho(self, v1, v2):
		if self.buscaVertice(v1) is not None:
			if self.buscaVertice(v2) is not None:
				self.grafo.visita(v1,v2)
			else:
				print('v1 nao existe')
		else:
			print('v2 nao existe')

	def loadGrafo(self, fileName = 'mapaGrafo.txt'):
		try:
			with open(fileName,'r') as file:
				for line in file:
					print(line)
					a1, a2, pe = line.split(' ')
					if self.grafo.buscaVertice(a1) is None:
						self.grafo.novoVertice(a1)
					if self.grafo.buscaVertice(a2) is None:
						self.grafo.novoVertice(a2)
					if self.grafo.buscaAresta(a1,a2) is None:
						self.grafo.novaAresta(a1, a2, pe)
		except Exception as e:
			raise

	def caminho(self):
		pass

	def vooDireto(self):
		pass

	def menorCusto(self):
		pass

	def caminho(self):
		pass

	def caminhoMinimo(self):
		pass

	def desenharGrafo(self):
		g = GrafoViz.GrafoViz()
		for v in self.grafo.getVertices():
			g.novoVertice(v.getId())
		for a in self.grafo.getArestas():
			g.novaAresta(a.getOrigem().getId(), a.getDestino().getId(), a.getDist())
		#print(g.source())
		#g.view()
		