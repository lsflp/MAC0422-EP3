import struct, os
from substitui import Substitui
from process import Processo


total, virtual, s, p = 0, 0, 0, 0
espaco_num = 0
substitui_num = 0
processos = []

def read_file(file):
    pid = 0
    global total, virtual, s, p, processos
    lines = []
    input_file = open(file, 'r')
    with input_file as ins:
        for line in ins:
            lines.append(line)
    total, virtual, s, p = lines[0].split()
    total, virtual, s, p = int(total), int(virtual), int(s), int(p)
    del lines[0]
    for line in lines:
        processos.append(Processo(line, pid))
        pid += 1

def espaco(num):
    global espaco_num
    espaco_num = int(num)

def substitui(num):
    global substitui_num    
    substitui_num = int(num)

def executa(intervalo):
    global total, virtual, s, p, processos

    if virtual == 0 or total == 0:
        print ("Carregar arquivo antes!")
        return

    if espaco_num == 0:
        print ("Escolha um informar algoritimo de gerenciamento de espco livre!")
        return

    if substitui_num == 0:
        print ("Escolha um informar algoritimo de gerenciamento de substituicao!")
        return

    gerenciador_memoria = Substitui(total, virtual, s, p, substitui_num, espaco_num)

    # Entre nesse laço até que todos os processos tenham terminado, executa em 1 em 1 segundo
    time  = 0;
    while len(processos) > 0:
        if (time % 4):
            gerenciador_memoria.setR ()

        retirar = [] # elementos que devem ser retirados da lsita (processos finalizados)
        for p in processos:
            if time in p.times:
                indice = p.times.index(time)
                posicao_memoria = p.positions[indice]
                # acessa
                status = gerenciador_memoria.acesso(p, posicao_memoria, time)
                if status == -1:
                    return;

            if max(p.times) < time:
                gerenciador_memoria.free(p)
                retirar.append(p)

        for i in retirar:
            processos.remove(i)

        if time % int(intervalo) == 0:
            print("\n-> Tempo: ", time)
            print (gerenciador_memoria)
        time += 1
