from espaco import Espaco
from process import Processo
from gerenciador_arquivo import *

class Pagina(object):
    def __init__(self, processo, ini):
        self.local = 0 # 0 virtual 1 fisica
        self.processo = processo # processo
        self.ini = ini # o numero inicial, multiplo de p (o numero que o processo enxerga)
        self.R = 0 # contador de referencias
        self.next_ref = 0 # qunado sera a proxima referencia, usado para o Optimal
        self.local_men = None # ende esta na memoria (posicao real de inicio)
        self.contador = 0 # momento em que a pagina foi chamada pela ultima vez

    def __repr__(self):
        res = str(self.local_men)+ " (R:" + str(self.R) + ", C:"+str(self.contador)+")"
        return  res

class Substitui(object):

    def __repr__(self):
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

    # set o bit R para 0 em todas as páginas
    def setR (self):
        for page in self.paginas:
            page.R = 0;
            page.contador = page.contador  >> 1
            page.contador += int('10000000', 2)
            page.contador &= int('11111111', 2) # define contador de 8 bits

    # retorna o elemento que tem que ser retirado
    def page_fault (self, tempo):
        # otimo, procura o elemente que esta mais longe de ser utilizado na memoria fisica
        if self.subs == 1:
            diff_tempo = 0
            pagina_retirada = None
            for page in self.paginas:
                if page.local == 1:
                    for time in page.processo.times:
                        if time > tempo:
                            if time - tempo > diff_tempo:
                                diff_tempo = time - tempo
                                pagina_retirada = page
            return pagina_retirada

        # segund chance
        elif self.subs == 2:
            while(True):
                page = next(page for page in self.paginas if page.local == 1)
                if page.R == 0:
                    return page
                else:
                    page.R = 0
                    self.paginas.remove(page)
                    self.paginas.append(page)

        # Clock
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

        # Least Recently Used (Quarta versao)
        elif self.subs == 4:
            tmp = sorted(self.paginas, key=lambda page: page.contador)
            for page in tmp:
                if page.local == 1:
                    return page

        return -1

    def acesso (self, processo, posicao, tempo):
        # verifica se essa uma pagina para esse acesso
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
                print("FUDEU, não cabe na memória virtual!")
                return -1
            else:
                pagina.local_men = status

        pagina.R = 1

        if pagina.local == 0: # se nao estiver na memoria virtual vamos coloca-la

            status = self.fisica.pegar_livre(mult_ps)
            if status == -1:
                #print("page fault")
                remove = self.page_fault (tempo)
                #print ("retirando ", remove)
                if remove == None:
                    print(self.fisica)

                remove.local = 0
                self.fisica.liberar(remove.local_men, mult_ps)
                remove.local_men = status
                status = self.virtual.pegar_livre(mult_ps)
                marca_vir (pagina.processo.pid, status*4*self.p, mult_ps * self.s)
                remove.local_men = status

                pagina.local = 1
                self.virtual.liberar(pagina.local_men, mult_ps)
                status = self.fisica.pegar_livre(mult_ps)
                marca_men (pagina.processo.pid, status*4*self.p, mult_ps * self.s)
                pagina.local_men = status 

            else:
                pagina.local = 1
                self.virtual.liberar(pagina.local_men, mult_ps)
                marca_men (pagina.processo.pid, status*4*self.p, mult_ps * self.s)
                pagina.local_men = status

        return pagina.local_men
