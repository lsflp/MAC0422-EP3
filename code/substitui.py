class Pagina(object):
    def __init__(self, pid, size, ini):
        self.local = 0 # 1 virtual 0 fisica
        self.pid = pid # processo
        self.ini = ini # o numero inicial, multiplo de p
        self.size = size # tamanho da pagina, p
        self.R = R # contador de referencias
        self.next_ref = 0 # qunado sera a proxima referencia, usado para o Optimal

class Substitui(object):
    
    def __init__(self, total, virtual, s, p, subs, espaco): 
        self.total = total
        self.virtual = virtual
        self.s = s
        self.p = p
        self.subs = subs
        self.espaco = espaco

    def pegar_pagina (self, processo, posicao):

        if tamanho < 1:
            return -1

        # First Fit
        if self.tipo == 1:
            for i in range(self.tamanho - tamanho + 1):
                if sum(self.marcador[i:i+tamanho]) == 0:
                    self.marcador[i:i+tamanho] = [True] * tamanho
                    return i;
        elif self.tipo == 2:
            for i in range(self.tamanho - tamanho + 1):
                j = (i + self.contador) % (self.tamanho - tamanho)
                if sum(self.marcador[j:j+tamanho]) == 0:
                    self.marcador[j:j+tamanho] = [True] * tamanho
                    self.contador = j+tamanho
                    return j;

                
        # nao encontrou espaco
        return -1

    def liberar (self, posicao, tamanho):
        self.marcador[posicao:posicao+tamanho] = [False] * tamanho