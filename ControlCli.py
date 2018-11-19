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
				v1 = input('Aeroporto 1: ')
				v2 = input('Aeroporto 2: ')
				self.grafos.caminho(v1, v2)
			elif(op == '3'):
				v = input('Aeroporto: ')
				self.grafos.vooDireto(v)
			elif(op == '4'):
				v1 = input('Aeroporto 1: ')
				v2 = input('Aeroporto 2: ')
				self.grafos.menorCusto(v1, v2)
			elif(op == '5'):
				v = input('Aeroporto de partida: ')
				self.grafos.rotaMinima(v)
				# self.grafos.caminho()
			elif(op == '6'):
				v1 = input('Aeroporto 1: ')
				self.grafos.caminho2(v1)
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