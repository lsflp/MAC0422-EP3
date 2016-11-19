################################################################################
#  Nomes: Gabriel Capella                                   Números USP: 8962078 
#         Luís Felipe de Melo Costa Silva                                9297961
#  
#  Arquivo parte do EP3 de MAC0422
################################################################################

from espaco import Espaco
from process import Processo
from gerenciador_arquivo import *

# Implementam funções que trabalham com as páginas e os algoritmos de 
# substituição de página. Depende dos arquivos espaco.py, process.py e 
# gerenciador_arquivo.py

# Objeto Página.
class Pagina(object):
    # Inicializando
    def __init__(self, processo, ini):
        # 0 para virtual e 1 para física.
        self.local = 0 
        # Processo.
        self.processo = processo 
        # O número inicial, múltiplo de p (o número que o processo enxerga).
        self.ini = ini 
        # Contador de referências (bit R).
        self.R = 0 
        # Quando será a próxima referência, usado para o Optimal.
        self.next_ref = 0 
        # Onde está na memória (posição real de início).
        self.local_men = None 
        # Momento em que a página foi chamada pela última vez.
        self.contador = 0 

    # Representação
    def __repr__(self):
        res = str(self.local_men)+ " (R:" + str(self.R) + ", C:"+str(self.contador)+")"
        return  res

# Objeto usado para as substituições de páginas.
class Substitui(object):

    # Representação
    def __repr__(self):
        # Para impressão
        res = "Memória Física (bitmap)\n"
        for i in range(len(self.fisica.marcador)):
            if self.fisica.marcador[i]:
                res += "1"
            else:
                res += "0"
            if (i+1) % 32 == 0:
                res += "\n"

        res += "\n\nMemória Virtual (bitmap)\n"
        for i in range(len(self.virtual.marcador)):
            if self.virtual.marcador[i]:
                res += "1"
            else:
                res += "0"
            if (i+1) % 64 == 0:
                res += "\n"

        return  res

    # Inicializando
    def __init__(self, total, virtual, s, p, subs, espaco): 
        self.total = total
        self.virtual = virtual
        self.s = s
        self.p = p
        self.subs = subs

        self.fisica = Espaco(espaco, total/s)
        self.virtual = Espaco(espaco, virtual/s)

        self.paginas = []

        gen_init(virtual, total)

    # Função que libera um processo, o apagando da lista de processos.
    def free (self, processo):
        deletar = []
        mult_ps = self.p/self.s
        for page in self.paginas:
            if page.processo.pid == processo.pid:
                deletar.append(page)

        for d in deletar:
            if d.local == 0:
                self.virtual.liberar(d.local_men, mult_ps)
            elif d.local == 1:
                self.fisica.liberar(d.local_men, mult_ps)
            self.paginas.remove(d)

    # Configura o bit R para 0 em todas as páginas
    def setR (self):
        for page in self.paginas:
            page.R = 0;
            page.contador = page.contador  >> 1
            page.contador += int('10000000', 2)
            page.contador &= int('11111111', 2) # define contador de 8 bits

    # Devolve o elemento que tem que ser retirado (Implementação dos algoritmos
    # de substituição)
    def page_fault (self, tempo):
        
        # 1) Optimal
        if self.subs == 1:
            diff_tempo = 0
            pagina_retirada = None
            for page in self.paginas:
                if page.local == 1:
                    if min(page.processo.times) < tempo:
                        return page
                    for time in page.processo.times:
                        if time > tempo:
                            if time - tempo > diff_tempo:
                                diff_tempo = time - tempo
                                pagina_retirada = page
            return pagina_retirada

        # 2) Second-chance
        elif self.subs == 2:
            while(True):
                page = next(page for page in self.paginas if page.local == 1)
                if page.R == 0:
                    return page
                else:
                    page.R = 0
                    self.paginas.remove(page)
                    self.paginas.append(page)

        # 3) Clock
        elif self.subs == 3:
            size = len(self.paginas)
            i = 0
            while(True):
                page = self.paginas[i]
                if page.local == 1:
                    if page.R == 0:
                        return page
                    else:
                        page.R = 0
                i = (i+1)%size

        # 4) Least Recently Used (Quarta versão)
        elif self.subs == 4:
            tmp = sorted(self.paginas, key=lambda page: page.contador)
            for page in tmp:
                if page.local == 1:
                    return page

        return -1

    # Faz o acesso a uma página.
    def acesso (self, processo, posicao, tempo):
        # Verifica se há uma pagina para esse acesso
        pagina = None
        ini = int(posicao)/int(self.s)
        mult_ps = self.p/self.s

        for page in self.paginas:
            if page.ini == ini and page.processo.pid == processo.pid:
                pagina = page
        if pagina == None:
            pagina = Pagina(processo, ini)
            self.paginas.append(pagina)
            status = self.virtual.pegar_livre(mult_ps)
            marca_vir (pagina.processo.pid, status*4*self.p, mult_ps * self.s)
            if status == -1:
                print("Não há espaço na memória virtual!")
                return -1
            else:
                pagina.local_men = status

        pagina.R = 1

         # Se não estiver na memória virtual vamos coloca-la.
        if pagina.local == 0:

            status = self.fisica.pegar_livre(mult_ps)
            if status == -1:
                remove = self.page_fault (tempo)
                if remove == None:
                    print(self.fisica)

                remove.local = 0

                # libera memorial virtual e fisica para realizar troca
                self.fisica.liberar(remove.local_men, mult_ps)
                self.virtual.liberar(pagina.local_men, mult_ps)

                remove.local_men = status
                status = self.virtual.pegar_livre(mult_ps)
                if status == -1:
                    print("Não há espaço na memória virtual!")
                    return -1

                marca_vir (pagina.processo.pid, status*4*self.p, mult_ps * self.s)
                remove.local_men = status

                pagina.local = 1
                status = self.fisica.pegar_livre(mult_ps)
                marca_men (pagina.processo.pid, status*4*self.p, mult_ps * self.s)
                pagina.local_men = status 

            else:
                pagina.local = 1
                self.virtual.liberar(pagina.local_men, mult_ps)
                marca_men (pagina.processo.pid, status*4*self.p, mult_ps * self.s)
                pagina.local_men = status

        return pagina.local_men
