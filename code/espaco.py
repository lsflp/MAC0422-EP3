class Espaco(object):
    # tipo: 1 First Fit ;2 Next Fit ;3 Best Fit ;4 Worst Fit e o temanho size
    def __init__(self, tipo, tamanho):
        self.marcador = [False] * int(tamanho)
        self.tipo = int(tipo)
        self.contador = 0
        self.tamanho = int(tamanho)

    def pegar_livre (self, tamanho):

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