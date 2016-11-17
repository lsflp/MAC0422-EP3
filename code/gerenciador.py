################################################################################
#  Nomes: Gabriel Capella                                   Números USP: 8962078 
#         Luís Felipe de Melo Costa Silva                                9297961
#  
#  Arquivo parte do EP3 de MAC0422
################################################################################

import struct, os
from substitui import Substitui
from process import Processo

# Arquivo com as funções que representam as ações do computador em relação aos 
# comandos fornecidos no console. Depende dos arquivos substitui.py e process.py

# Inicializando as variáveis
total, virtual, s, p = 0, 0, 0, 0
espaco_num = 0
substitui_num = 0
processos = []

# Essa função recebe o nome de um arquivo de trace, lê suas informações e as 
# guarda nas variáveis acima.
def read_file(file):
    pid = 0
    # Váriáveis globais para tamanho da memória física, da memória virtual, do 
    # tamanho da unidade de alocação para os algoritmos para gerência do espaço 
    # livre, para o tamanho da página a ser considerada para a execução dos
    # algoritmos de substituição de página e o vetor de processos, 
    # respectivamente.
    global total, virtual, s, p, processos
    lines = []
    # Abrindo o arquivo
    input_file = open(file, 'r')
    # Lendo as informações
    with input_file as ins:
        for line in ins:
            lines.append(line)
    # Atribuindo-as
    total, virtual, s, p = lines[0].split()
    total, virtual, s, p = int(total), int(virtual), int(s), int(p)
    del lines[0]
    for line in lines:
        processos.append(Processo(line, pid))
        pid += 1

# Define o número do algoritmo de gerência de espaço livre a ser utilizado.
def espaco(num):
    global espaco_num
    espaco_num = int(num)

# Define o número do algoritmo de substituição de página a ser utilizado.
def substitui(num):
    global substitui_num    
    substitui_num = int(num)

# Executa os processos. Recebe o intervalo para mostrar as informações no 
# console. 
def executa(intervalo):
    global total, virtual, s, p, processos

    # Caso alguma das informações necessárias não esteja registrada, a função
    # não trabalha.
    if virtual == 0 or total == 0:
        print ("Carregar arquivo antes!")
        return

    if espaco_num == 0:
        print ("Escolha um algoritmo de gerenciamento de espaço livre!")
        return

    if substitui_num == 0:
        print ("Escolha um algoritmo de substituição de página!")
        return

    # Objeto a ser usado para a execução.
    gerenciador_memoria = Substitui(total, virtual, s, p, substitui_num, espaco_num)

    # Entra nesse laço até que todos os processos tenham terminado, executando
    # a cada "segundo".
    time  = 0;
    while len(processos) > 0:
        if (time % 4):
            gerenciador_memoria.setR ()

        # Elementos que devem ser retirados da lista (processos finalizados)
        retirar = [] 

        for p in processos:
            if time in p.times:
                indice = p.times.index(time)
                posicao_memoria = p.positions[indice]
                # Acessa a memória
                status = gerenciador_memoria.acesso(p, posicao_memoria, time)
                if status == -1:
                    return;

            # Se já passou mais tempo do que o tempo de acesso máximo desse 
            # processo, ele fica marcado para ser removido.s
            if max(p.times) < time:
                gerenciador_memoria.free(p)
                retirar.append(p)

        for i in retirar:
            processos.remove(i)

        # Imprimindo a informação, caso seja o momento.
        if time % int(intervalo) == 0:
            print("\n-> Tempo: ", time)
            print(gerenciador_memoria)
        time += 1
