class Vertice(object):
    def __init__(self, ide):
        self.id = ide
        self.estimativa = 99999999
        self.visitado = False
        self.predecessor = []

    def setId(self, ide):
        self.id = ide

    def getId(self):
        return self.id

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado

    def setEstimativa(self, estimativa):
        self.estimativa = estimativa

    def getEstimativa(self):
        return self.estimativa

    def getPredecessor(self):
        return self.predecessor

    # string
    def __str__(self):
        return (" Vertice  : %s \t Estimativa: %i \n" %
                (self.id, self.estimativa))

    # equals
    def __eq__(self, v):
        return self.id == v.id

    # def __eq__(self, v):
    # 	return self.estimativa == v.estimativa

    # menor
    def __lt__(self, v):
        return self.estimativa < v.estimativa

    # maior
    def __gt__(self, v):
        return self.estimativa > v.estimativa
