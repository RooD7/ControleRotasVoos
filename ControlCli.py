import Cli
import AppGrafos

class ControlCli(object):
	""" controle interface """
	def __init__(self):
		self.cli = Cli.Cli()
		self.grafos = AppGrafos.AppGrafos()

	def menu(self):
		while True:
			op = self.cli.menu()
			if(op == '1'):
				# fileName = self.cli.nomeArquivo()
				self.grafos.loadGrafo()
			elif(op == '2'):
				v1 = input('vertice 1: ')
				v2 = input('vertice 2: ')
				self.grafos.caminho(v1, v2)
			elif(op == '3'):
				self.grafos.vooDireto()
			elif(op == '4'):
				self.grafos.menorCusto()
			elif(op == '5'):
				self.grafos.caminho()
			elif(op == '6'):
				self.grafos.caminhoMinimo()
			elif(op == '7'):
				self.grafos.desenharGrafo()
			elif(op == '0'):
				while(True):
					op = self.cli.sair()
					if op.lower() == 'y':
						exit()
					elif op.lower() == 'n':
						break
					else:
						self.cli.opInvalida()
						
			else:
				self.cli.opInvalida()