################################################################################
#  Nomes: Gabriel Capella                                   Números USP: 8962078 
#         Luís Felipe de Melo Costa Silva                                9297961
#  
#  Arquivo parte do EP3 de MAC0422
################################################################################

# Implementa os algoritmos de gerenciamento de espaço livre.

# Objeto Espaco
class Espaco(object):
    
    # Inicializa
    def __init__(self, tipo, tamanho):
        self.marcador = [False] * int(tamanho) # bit map
        self.tipo = int(tipo)
        self.contador = 0
        self.tamanho = int(tamanho)

    # Devolve o endereço do próximo espaço livre.
    def pegar_livre (self, tamanho):

        tamanho = int (tamanho)

        if tamanho < 1:
            return -1

        # 1) First Fit
        if self.tipo == 1:
            for i in range(self.tamanho - tamanho + 1):
                if sum(self.marcador[i:i+tamanho]) == 0:
                    self.marcador[i:i+tamanho] = [True] * tamanho
                    return i

        # 2) Next Fit
        elif self.tipo == 2:
            for i in range(self.tamanho - tamanho + 1):
                j = (i + self.contador) % (self.tamanho - tamanho + 1)
                if sum(self.marcador[j:j+tamanho]) == 0:
                    self.marcador[j:j+tamanho] = [True] * tamanho
                    self.contador = j+tamanho
                    return j

        # 3) Best Fit
        elif self.tipo == 3:
            zeros_index = []
            zeros_size = []
            count = 0
            index = -1
            for i in range(self.tamanho):
                if self.marcador[i] == True:
                    if index != -1 and count >= tamanho:
                        zeros_index.append(index)
                        zeros_size.append(count)
                    count = 0
                    index = -1
                else:
                    if count == 0:
                        index = i
                    count += 1;
            if index != -1 and count >= tamanho:
                zeros_index.append(index)
                zeros_size.append(count)

            if len(zeros_size) > 0:
                menor = min(zeros_size)
                index = zeros_index[zeros_size.index(menor)]
                self.marcador[index:index+tamanho] = [True] * tamanho
                return index

        # 4) Worst Fit
        elif self.tipo == 4:
            zeros_index = []
            zeros_size = []
            count = 0
            index = -1
            for i in range(self.tamanho):
                if self.marcador[i] == True:
                    if index != -1:
                        zeros_index.append(index)
                        zeros_size.append(count)
                    count = 0
                    index = -1
                else:
                    if count == 0:
                        index = i
                    count += 1;
            if index != -1:
                zeros_index.append(index)
                zeros_size.append(count)

            if len(zeros_size) > 0:
                menor = max(zeros_size)
                index = zeros_index[zeros_size.index(menor)]
                self.marcador[index:index+tamanho] = [True] * tamanho
                return index
     
        # Se não encontrou espaço
        return -1

    # Libera o espaço.
    def liberar (self, posicao, tamanho):
        tamanho = int (tamanho)
        self.marcador[posicao:posicao+tamanho] = [False] * tamanho

    # Representação
    def __repr__(self):
        return str(self.marcador)
