class Cli(object):
	""" interface """
	def __init__(self):
		pass

	def menu(self):
		print('\n\t---\t--- Menu ---\t---\t')
		print('1. Carregar grafo.')
		print('2. Caminho entre 2 aeroportos.')
		print('3. Voos diretos a partir de um aeroporto.')
		print('4. Viagem de menor custo.')
		print('5. Acessar aeroporto.')
		print('6. Caminho minimo entre os aeroportos.')
		print('7. Desenhar grafos.')
		print('0. Sair\n')

		return input('Selecione a opção: ')

	def sair(self):
		return input("Deseja realmente sair? (y/n): ")
	
	def opInvalida(self):
		print("Opção inválida!\n")