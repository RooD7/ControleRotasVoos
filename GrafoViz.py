from graphviz import Digraph

# g = Digraph('G', filename='hello.gv')
# g.node('Hello')
# g.edge('Hello', 'World')
# g.view()

class GrafoViz(object):
	""" Visualizacao Grafica de um Grafo """
	def __init__(self, fileName = 'grafo.gv'):
		self.fileName = fileName
		self.g = Digraph('G', filename= fileName)

	def novoVertice(self,vertice):
		self.g.node(vertice)

	def novaAresta(self,v1, v2, lab= '/**/', cor = 'black'):
		self.g.edge(v1, v2, label= lab, color= cor)

	def view(self):
		self.g.view()

	def source(self):
		return self.g.source

		