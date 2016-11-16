from espaco import Espaco
from process import Processo

class Pagina(object):
    def __init__(self, processo, ini):
        self.local = 0 # 0 virtual 1 fisica
        self.processo = processo # processo
        self.ini = ini # o numero inicial, multiplo de p (o numero que o processo enxerga)
        self.R = 0 # contador de referencias
        self.next_ref = 0 # qunado sera a proxima referencia, usado para o Optimal
        self.local_men = None # ende esta na memoria (posicao real de inicio)

class Substitui(object):

    def __init__(self, total, virtual, s, p, subs, espaco): 
        self.total = total
        self.virtual = virtual
        self.s = s
        self.p = p
        self.subs = subs

        self.fisica = Espaco(espaco, total/s)
        self.virtual = Espaco(espaco, virtual/s)

        self.paginas = []

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
            if status == -1:
                print("FUDEU, não cabe na memória virtual!")
                return -1
            else:
                pagina.local_men = status

        if pagina.local == 0: # se nao estiver na memoria virtual vamos coloca-la

            status = self.fisica.pegar_livre(mult_ps)
            if status == -1:
                print("page fault")
                
                return 0;
            else:
                pagina.local = 1
                self.virtual.liberar(pagina.local_men, mult_ps)
                pagina.local_men = status
        return status

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
