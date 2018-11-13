import Cli
import AppGrafos


class controlCli(object):
	""" controle interface """

	def __init__(self):
		self.cli = Cli.Cli()
		self.grafos = AppGrafos.AppGrafos()

	def menu(self):
		while True:
			op = self.cli.menu()
			if (op == '1'):
				self.grafos.loadGrafo()
			elif (op == '2'):
				self.grafos.caminho()
			elif (op == '3'):
				self.grafos.vooDireto()
			elif (op == '4'):
				self.grafos.menorCusto()
			elif (op == '5'):
				self.grafos.caminho()
			elif (op == '6'):
				self.grafos.caminhoMinimo()
			elif (op == '7'):
				self.grafos.desenharGrafo()
			elif (op == '0'):
				while (True):
					op = self.cli.sair()
					if op.lower() == 'y':
						exit()
					elif op.lower() == 'n':
						break
					else:
						self.cli.opInvalida()

			else:
				self.cli.opInvalida()
