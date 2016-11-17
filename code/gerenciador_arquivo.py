################################################################################
#  Nomes: Gabriel Capella                                   Números USP: 8962078 
#         Luís Felipe de Melo Costa Silva                                9297961
#  
#  Arquivo parte do EP3 de MAC0422
################################################################################

# Implementa as funções que escrevem os arquivos binários /tmp/ep3.men e 
# /tmp/ep3.vir 

import os, struct

vir, men = [], []

# Inicializa as variáveis e cria os arquivos.
def gen_init(virtual, total):
    global vir, men
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')

    vir = open('./tmp/ep3.vir', 'wb+')
    men = open('./tmp/ep3.men', 'wb+')

    # Cria arquivos de memória
    data = struct.pack("i", -1) * virtual
    vir.write(data)
    vir.flush()

    data = struct.pack("i", -1) * total
    men.write(data)
    men.flush()

# Escreve em /tmp/ep3.vir
def marca_vir (pid, ini, size):
    global vir, men
    vir.seek(int(ini)) # Inteiro de 4 bytes
    data = struct.pack("i", pid) * int(size)
    vir.write(data)
    vir.flush()

# Escreve em /tmp/ep3.men
def marca_men (pid, ini, size):
    global vir, men
    men.seek(int(ini)) # Inteiro de 4 bytes
    data = struct.pack("i", pid) * int(size)
    men.write(data)
    men.flush()
