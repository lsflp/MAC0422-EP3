################################################################################
#  Nomes: Gabriel Capella                                   Números USP: 8962078 
#         Luís Felipe de Melo Costa Silva                                9297961
#  
#  Arquivo parte do EP3 de MAC0422
################################################################################

# Define o objeto Processo

class Processo(object):

    # Recebe uma linha que descreve o processo e o seu pid.
    def __init__(self, info_string, pid):
        data = info_string.split()
        self.pid = pid
        self.name = data[1]
        self.t0 = int(data[0])
        del data[0]
        del data[0]
        self.positions = [int(i) for i in data[1::2]]
        self.times = [int(i) for i in data[0::2]]

    # Representação
    def __repr__(self):
        return self.name + " (" + str(self.pid) + ")"