import Cli
import Grafo

class Cli(object):
	""" controle interface """
	def __init__(self):
		pass

	def ctrlMenu(self):
		while True:
			if(op == 1):
				Grafo.loadGrafo()
			elif(op == 2):
				Grafo.caminho()
			elif(op == 3):
				Grafo.vooDireto()
			elif(op == 4):
				Grafo.menorCusto()
			elif(op == 5):
				Grafo.caminho()
			elif(op == 6):
				Grafo.caminhoMinimo()
			elif(op == 7):
				Grafo.desenharGrafo()
			elif(op == 0):
				while(True):
					op = Cli.sair()
					if op.lower() == 'y':
						exit()
					elif op.lower() == 'n':
						break
			else:
				pass