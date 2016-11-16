vir, men = [], []

def gen_init(virtual, total):
    global vir, men
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')

    vir = open('./tmp/ep3.vir', 'wb+')
    men = open('./tmp/ep3.men', 'wb+')

    # Cria arquivos de memória
    with vir as vir_file:
        data = struct.pack("i", -1) * virtual
        vir_file.write(data)
        vir_file.flush()

    with men as men_file:
        data = struct.pack("i", -1) * total
        men_file.write(data)
        men_file.flush()

def marca(pid, file, bloco, quantidade_blocos)