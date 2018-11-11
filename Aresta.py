class Aresta(object):
    def __init__(self, origem, destino, dist=0, numP=0, tempo=0):
        self.origem = origem
        self.destino = destino
        self.dist = dist
        self.numP = numP
        self.tempo = tempo

    def getOrigem(self):
        return self.origem

    def setOrigem(self, vertice):
        self.origem = vertice

    def getDestino(self):
        return self.destino

    def setDestino(self, vertice):
        self.destino = vertice

    def getDist(self):
        return self.dist

    def setDist(self, dist):
        self.dist = dist

    def getNumP(self):
        return self.numP

    def setNumP(self, numP):
        self.numP = numP

    def getTempo(self):
        return self.tempo

    def setTempo(self, tempo):
        self.tempo = tempo

    # string
    def __str__(self):
        return ("A(%s --- Dist: %i - numP: %i - tempo: %i ---> %s)" % (self.origem.getId(),
                                                                       self.dist, self.numP, self.tempo,
                                                                       self.destino.getId()))
