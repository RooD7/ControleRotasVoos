import Grafo
import GrafoViz
from copy import deepcopy
class ErroFile(Exception):
	"""docstring for ErroSintatico"""
	def __init__(self, fl):
		self.file = fl

	def __str__(self):
		return "ERRO: não foi possivel abrir o arquivo "+str(self.file)+"\n"

class AppGrafos(object):
	def __init__(self):
		self.grafoVoos = Grafo.Grafo()
		self.grafoRotas = Grafo.Grafo(False)

	#Opcao 1
	def loadGrafo(self, fileName = 'mapaGrafo.txt'):
		try:
			with open(fileName,'r') as file:
				for line in file:
					a1, a2, pe = line.split(' ')
					if self.grafoVoos.buscaVertice(a1) is None:
						self.grafoVoos.novoVertice(a1)
						self.grafoRotas.novoVertice(a1)
					if self.grafoVoos.buscaVertice(a2) is None:
						self.grafoVoos.novoVertice(a2)
						self.grafoRotas.novoVertice(a2)
					if self.grafoVoos.buscaAresta(a1,a2) is None:
						self.grafoVoos.novaAresta(a1, a2, pe)
						self.grafoRotas.novaAresta(a1, a2, pe)
		except Exception as e:
			raise

	#Opcao 2
	def caminho(self, v1, v2):
		voos = deepcopy(self.grafoVoos)
		rotas = deepcopy(self.grafoRotas)
		ver1 = voos.getVertice(v1)
		ver2 = voos.getVertice(v2)
		voos.clearCaminho()
		rotas.clearCaminho()
		if ver1 is not None and ver2 is not None:
			print('Voos: ')
			voos.buscaLargura(ver1,ver2)
			voos.printCaminho()
			print('Rotas: ')
			rotas.buscaLargura(ver1,ver2)
			rotas.printCaminho()
		else:
			print('Aeroporto informado desconhecido!')
			# vertice nao existe

	# Opcao 3
	def vooDireto(self, v1):
		voos = deepcopy(self.grafoVoos)
		vert = voos.getVertice(v1)

		caminho = []
		if vert is not None:
			v = voos.verticeAdjacente(vert)
			while v is not None:
				caminho.append(v.getId())
				v = voos.verticeAdjacente(vert)
		else:
			print('Aeroporto informado desconhecido!')
			
		strg = ''
		for i in range(len(caminho)-1):
			strg += '%s -> '%caminho[i]
		strg += '%s.'%caminho[len(caminho)-1]
		print(strg)

	def relaxamento(self, u, v, w):
		if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
			v.setEstimativa(u.getEstimativa() + w.getPeso())
			v.predecessor.append(u.getId()) # guarda apenas o id
	# Dijkstra
	def menorCusto(self, v1, v2):
		pass
		# voos = deepcopy(self.grafoVoos)
		# origem = voos.buscaVertice(v1)
		# destino = voos.buscaVertice(v2)
		# if origem is not None and destino is not None:
		# 	origem.setVisitado(True)
		# 	origem.setEstimativa(0)

		# 	resposta = []  # conjunto resposta
		# 	lista = deepcopy(voos.getVertices())
		# 	# for i in voos.getVertices():
		# 	# 	lista.append(i)
		# 	while len(lista) != 0:
		# 		lista.sort()  # ordeno a lista baseado na estimativa
		# 		u = lista[0]
		# 		v = voos.verticeAdjacente(u)
		# 		if v is None:
		# 			for i in voos.getVertices():  # como o vetice u marcou seus adj como visitado nenhum outro vértice visitara
		# 				i.setVisitado(
		# 					False)  # esse vertice então preciso marcar como não visitado pra bucar os adj de outro vertice
		# 			# self.tempo += 1
		# 			# u.setImput(self.tempo)  # apenas mostra a ordem de visitação do grafo
		# 			resposta.append(lista[0])
		# 			lista.pop(0)  # retiro vertice sem adjacente da lista

		# 		else:
		# 			w = voos.buscaAresta(u, v)
		# 			if w is not None:
		# 				self.relaxamento(u, v, w)

		# 	print("Estimativas: ")
		# 	for i in resposta:
		# 		print(i) # imprimo as respostas
		# else:
		# 	print('Aeroporto informado desconhecido!')

	def caminho2(self):
		pass

	def caminhoMinimo(self):
		pass

	def desenharGrafo(self):
		voos = GrafoViz.GrafoViz('voos.gv')
		rotas = GrafoViz.GrafoViz('rotas.gv',False)
		for v in self.grafoVoos.getVertices():
			voos.novoVertice(v.getId())
			rotas.novoVertice(v.getId())
		for a in self.grafoVoos.getArestas():
			voos.novaAresta(a.getOrigem().getId(), a.getDestino().getId(), a.getDist())
			rotas.novaAresta(a.getOrigem().getId(), a.getDestino().getId(), a.getDist())
		# for a in self.grafoRotas.getArestas():
		# 	rotas.novaAresta(a.getOrigem().getId(), a.getDestino().getId(), a.getDist())
		rotas.view()
		#print(g.source())
		#g.view()
		