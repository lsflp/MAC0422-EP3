import os, struct

vir, men = [], []


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

def marca_vir (pid, ini, size):
    global vir, men
    vir.seek(int(ini)) # inteiro de 4 bytes
    data = struct.pack("i", pid) * int(size)
    vir.write(data)
    vir.flush()

def marca_men (pid, ini, size):
    global vir, men
    men.seek(int(ini)) # inteiro de 4 bytes
    data = struct.pack("i", pid) * int(size)
    men.write(data)
    men.flush()
