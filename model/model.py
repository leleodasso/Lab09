import networkx as nx

from database.DAO import DAO


class Model:


    def __init__(self):
        self._aeroporto = DAO.getAllAirport()
        self._grafo = nx.Graph()
        self._idMapAeroporto = {}
        for v in self._aeroporto:
            self._idMapAeroporto[v.ID] = v


    def buildGraph(self, dist):
        #Aggiungo i nodi
        self._grafo.add_nodes_from(self._aeroporto) #aggiungo un nodo per ogni fermata
        self._grafo.clear_edges()
        self.addEdges(dist)

    def addEdges(self, dist):
        """
        Faccio una query che prende tutti gli arghi
        e poi mi arrangio su python
        """
        allEdges = DAO.getAllEdges()
        for edge in allEdges:
            u = self._idMapAeroporto[edge.ORIGIN_AIRPORT_ID]
            v = self._idMapAeroporto[edge.DESTINATION_AIRPORT_ID]
            print(edge.DISTANCE)
            if edge.DISTANCE < int(dist):
                print("distanza troppo piccola")
                continue
            print(edge)
            self._grafo.add_edge(u, v)


    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)
