import Grafo
import GrafoViz
from copy import deepcopy
from heapq import heappop, heappush


class ErroFile(Exception):
	"""docstring for ErroSintatico"""

	def __init__(self, fl):
		self.file = fl

	def __str__(self):
		return "ERRO: não foi possivel abrir o arquivo " + str(self.file) + "\n"


class AppGrafos(object):
	def __init__(self):
		self.grafoVoos = Grafo.Grafo() 
		self.grafoRotas = Grafo.Grafo(False)
		self.graph = []

	# Opcao 1
	def loadGrafo(self, fileName='mapaGrafo.txt'):
		try:
			with open(fileName, 'r') as file:
				for line in file:
					a1, a2, pe = line.split(' ')
					if self.grafoVoos.buscaVertice(a1) is None:
						self.grafoVoos.novoVertice(a1)
						self.grafoRotas.novoVertice(a1)
					if self.grafoVoos.buscaVertice(a2) is None:
						self.grafoVoos.novoVertice(a2)
						self.grafoRotas.novoVertice(a2)
					if self.grafoVoos.buscaAresta(a1, a2) is None:
						self.grafoVoos.novaAresta(a1, a2, pe)
						self.grafoRotas.novaAresta(a1, a2, pe)
		except Exception as e:
			raise
		# self.graph = [ [] for i in range(0,len(self.grafoRotas.getArestas()))]

	# Opcao 2
	def caminho(self, v1, v2):
		voos = deepcopy(self.grafoVoos)
		rotas = deepcopy(self.grafoRotas)
		ver1 = voos.getVertice(v1)
		ver2 = voos.getVertice(v2)
		voos.clearCaminho()
		rotas.clearCaminho()
		if ver1 is not None and ver2 is not None:
			print('Voos: ')
			voos.buscaLargura(ver1, ver2)
			voos.printCaminho()
			print('Rotas: ')
			rotas.buscaLargura(ver1, ver2)
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
		for i in range(len(caminho) - 1):
			strg += '%s -> ' % caminho[i]
		strg += '%s.' % caminho[len(caminho) - 1]
		print(strg)

	def relaxamento(self, u, v, w):
		print('v.estimativa: '+str(v.getEstimativa()))
		print('u.estimativa: '+str(u.getEstimativa()))
		print('w.distancia : '+str(w.getDist()))
		if v.getEstimativa() > (u.getEstimativa() + int(w.getDist())):
			return u.getEstimativa() + int(w.getDist())
			# v.predecessor.append(u.getId())  # guarda apenas o id
		# print('v.estimativa: '+str(v.getEstimativa()))
		return 999999

	# Dijkstra
	def menorCusto(self, v1, v2):

		voos = deepcopy(self.grafoVoos)
		listaVert = deepcopy(voos.getVertices())

		origem = voos.buscaVertice(v1)
		destino = voos.buscaVertice(v2)
		if origem is not None and destino is not None:
			origem.setVisitado(True)
			origem.setEstimativa(0)

			listaVert.remove(origem)
			listaVert.append(origem)

			custo = 999999
			resposta = []  # conjunto resposta
			resposta.append(origem)
			encontrou = False
			while len(listaVert) != 0:
				listaVert.sort()  # ordeno a lista baseado na estimativa
				
				u = listaVert[0]
				v = voos.verticeAdjacente(u)
				print('u: '+str(u.getId()))
				if v is not None:
					print('v: '+str(v.getId()))
				else:
					print('v: None')

				for i in listaVert:
					if i.getEstimativa() != 999999:
						print('ID: '+str(i.getId())+'\tEST: '+str(i.getEstimativa()))
				if v is None:
					print('Não encontrou mais...')
					# self.tempo += 1
					resposta.append(listaVert.pop(0))
					# listaVert.pop(0)  # retiro vertice sem adjacente da lista
				else:
					w = voos.buscaAresta(u.getId(), v.getId())
					if w is not None:
						estimativa = self.relaxamento(u, v, w)
						v.setEstimativa(estimativa)
						v.addPredecessor(u)
						resposta.append(v)
						listaVert.remove(v)
						listaVert.append(v)
					if v.getId() == destino.getId():
						custo = v.getEstimativa()
						encontrou = True
						break

			if encontrou:
				print("Camminho mínimo: ")
				# for i in resposta:
				# 	print(i) # imprimo as respostas
				# for i in listaVert:
				# 	if i.getPredecessor() != []:
				# 		for j in i.getPredecessor():
				# 			print('VT: '+str(i.getId())+'\tPDT: '+str(j.getId()))

				# extrai os predecessor do vetor resposta
				r = []
				r.insert(0, destino.getId())
				ok = False
				while not ok:
					for k in resposta:
						if k.getId() == destino.getId():
							pre = k.getPredecessor()
							p = pre.pop()
							r.insert(0,p.getId())
							destino = p
							if p.getId() == origem.getId():
								ok = True
								break
				# imprime resposta
				strg = ''
				for i in range(len(r) - 1):
					strg += '%s -> ' % r[i]
				strg += '%s.' % r[len(r) - 1]
				print(strg)
				print('Custo: '+str(custo))
			else:
				print('Não foi possivel a partir do aeroporto 1, atingir o aeroporto 2')
		else:
			print('Aeroporto informado desconhecido!')

	def caminho2(self, v1):

		voos = deepcopy(self.grafoVoos)
		listaVert = deepcopy(voos.getVertices())

		origem = voos.buscaVertice(v1)
		if origem is not None:
			origem.setVisitado(True)
			origem.setEstimativa(0)

			listaVert.remove(origem)
			listaVert.append(origem)

			custo = 999999
			resposta = []  # conjunto resposta
			resposta.append(origem)
			encontrou = False
			while len(listaVert) != 0:
				listaVert.sort()  # ordeno a lista baseado na estimativa
				
				u = listaVert[0]
				v = voos.verticeAdjacente(u)
				print('u: '+str(u.getId()))
				if v is not None:
					print('v: '+str(v.getId()))
				else:
					print('v: None')

				for i in listaVert:
					if i.getEstimativa() != 999999:
						print('ID: '+str(i.getId())+'\tEST: '+str(i.getEstimativa()))
				if v is None:
					print('Não encontrou mais...')
					# self.tempo += 1
					resposta.append(listaVert.pop(0))
					# listaVert.pop(0)  # retiro vertice sem adjacente da lista
				else:
					w = voos.buscaAresta(u.getId(), v.getId())
					if w is not None:
						estimativa = self.relaxamento(u, v, w)
						v.setEstimativa(estimativa)
						v.addPredecessor(u)
						resposta.append(v)
						if v in listaVert:
							listaVert.remove(v)
							listaVert.append(v)
						else:
							encontrou = True
							break
					# if v.getId() == destino.getId():
					# 	custo = v.getEstimativa()
					# 	encontrou = True
					# 	break

			if encontrou:
				print("Camminho mínimo: ")
				for i in resposta:
					print(i) # imprimo as respostas
				for i in listaVert:
					if i.getPredecessor() != []:
						for j in i.getPredecessor():
							print('VT: '+str(i.getId())+'\tPDT: '+str(j.getId()))

				# extrai os predecessor do vetor resposta
				# r = []
				# ultimo = resposta[len(resposta)-1]
				# r.insert(0, ultimo.getId())
				# ok = False
				# while not ok:
				# 	for k in resposta:
				# 		if k.getId() == ultimo.getId():
				# 			pre = k.getPredecessor()
				# 			p = pre.pop()
				# 			r.insert(0,p.getId())
				# 			ultimo = p
				# 			if p.getId() == origem.getId():
				# 				ok = True
				# 				break
				# # imprime resposta
				# strg = ''
				# for i in range(len(r) - 1):
				# 	strg += '%s -> ' % r[i]
				# strg += '%s.' % r[len(r) - 1]
				# print(strg)
				# print('Custo: '+str(custo))
			else:
				print('Não foi possivel a partir do aeroporto 1, atingir o aeroporto 2')
		else:
			print('Aeroporto informado desconhecido!')

	# Algoritmo de Prim
	def rotaMinima(self, vi=1):
		rotas = deepcopy(self.grafoRotas)
		vertices = deepcopy(rotas.getVertices())
		# vertice inicial
		v = rotas.buscaVertice(vi)
		if v is not None:
			v.setVisitado(True)
			v.setEstimativa(0)

		vertices.remove(v)
		vertices.append(v)
		
		sub = []
		# menor = rotas.menorArestaAdjacente(v)
		ok = False
		while not ok:
			vertices.sort() # ordeno a lista baseado na estimativa
			u = vertices[0]
			v = rotas.verticeAdjacente(u)

			# verifica se todos os vertices foram visitados
			for t in vertices:
				if not t.getVisitado():
					ok = False
					break
				else:
					ok = True

			if v is not None:
				w = rotas.buscaAresta(u.getId(), v.getId())
				v.setVisitado(True)
				v.setEstimativa(w.getDist())
				vertices.remove(v)
				vertices.append(v)
				sub.append(v)

		for s in sub:
			print(s)


	def montar_grafo(self):
		for i in self.grafoRotas.getArestas():
			print(i)
			(u, v) = (int(i.getDestino().getId()), int(i.getDist()))
			self.graph.append((u,v))

# Utiliza heap para encontrar a árvore geradora mínima, se o grafo for desconexo, apenas os vertices conectados
# ao vertice inicial será incluído na árvore geradora mínima.
	def prim(self, Vi=1):

		# print(self.graph[3])
		# print(len(self.graph))
		self.graph[Vi] = (0,-1)
		heap = [(0,Vi)]

		
		vis = [False]*len(self.graph)
		while True:
			v = -1
			while len(heap) > 0 and (v < 0 or vis[v]):
				v = heappop(heap)[1]

			if v < 0 or self.graph[v][0] < 0:
				break
			vis[v] = True

			print(v)
			print(self.graph[v])
			# for (u, w) in self.graph[v]:
			for i in self.graph:
				(u, w) = i
				if self.graph[u][0] < 0 or self.graph[u][0] > w:
					self.graph[u] = (w, v)
					heappush(heap, (self.graph[u][0],u))
		return self.graph


	def desenharGrafo(self):
		voos = GrafoViz.GrafoViz('voos.gv')
		rotas = GrafoViz.GrafoViz('rotas.gv', False)
		for v in self.grafoVoos.getVertices():
			voos.novoVertice(v.getId())
			rotas.novoVertice(v.getId())
		for a in self.grafoVoos.getArestas():
			voos.novaAresta(a.getOrigem().getId(), a.getDestino().getId(), a.getDist())
			rotas.novaAresta(a.getOrigem().getId(), a.getDestino().getId(), a.getDist())
		# for a in self.grafoRotas.getArestas():
		# 	rotas.novaAresta(a.getOrigem().getId(), a.getDestino().getId(), a.getDist())
		rotas.view()
	# print(g.source())
	# g.view()
