from collections import defaultdict
import pandas as pd
import numpy as np
from faker import Faker

class Grafo(object):

    def __init__(self, arestas, direcionado=False):
        tamanho=0
        #inicializa os atributos do grafo
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.tamanho = tamanho
        self.adiciona_arestas(arestas)

    #obtem a lista de vertices do grafo
    def get_vertices(self):
        
        return list(self.adj.keys())

    #obtem a lista de arestas do grafo
    def get_arestas(self):
        
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    #Adciona as arestas no grafo
    def adiciona_arestas(self, arestas):
        
        for i, j in zip(arestas["estilo"], arestas["artista favorito"]):
            self.tamanho += 1
            self.adiciona_arco(i, j)

    def adiciona_estilos(self, arestas):
        
        for u, v in arestas:
            self.tamanho += 1
            self.direcionado = True
            self.adiciona_arco(u, v)

    #adciona um arco entre u e v
    def adiciona_arco(self, u, v):
        
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)

    #verifica a existencia de arestas
    def existe_aresta(self, u, v):
        return u in self.adj and v in self.adj[u]

    def verifica_tamanho(self):
        return self.tamanho

    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]
    
def hash_string(palavra):
    a = np.fromstring(palavra, dtype=np.uint8)
    soma = 0
    for i in a:
        soma += i
    return soma

def verifica_dict(visitado:dict, chave:int, nome:str):
    for i in visitado[str(chave)]:
        if i == nome:
            return True
        
    return False

def bfs(G, inicio: str):

    visitado = {}

    fila = []
    ret = []
    fila.append(inicio)

    chave = hash_string(inicio)

    visitado[str(chave)] = []
    visitado[str(chave)].append(inicio)

    count = 0   #usado para acessar estilo


    while fila:
        pr = fila.pop(0)
        ret.append(pr)
        l = list(G["Estilos"])

        for j in list(G[pr]):
            cha = hash_string(j)
            if str(cha) not in visitado:
                visitado[str(cha)] = []
                visitado[str(cha)].append(j)
                fila.append(j)


            elif verifica_dict(visitado=visitado, chave=cha, nome=j) != True:    
                visitado[cha].append(j)
                fila.append(j)

        if fila == []:
            if count<len(l):
                fila.append(l[count])
                count+=1
    return ret