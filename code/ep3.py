################################################################################
#  Nomes: Gabriel Capella                                   Números USP: 8962078 
#         Luis Felipe de Melo Costa Silva                                9297961
#  
#  Arquivo parte do EP3 de MAC0422
################################################################################

import cmd
from gerenciador import *

# Este arquivo implementa o console, usando a biblioteca cmd, do Python e 
# depende do arquivo gerenciador.py

class console(cmd.Cmd):
    # String impressa a cada vez que o usuário deve entrar com comandos.
    prompt = '(ep3): '
    
    # Carrega o arquivo de trace.
    def do_carrega(self, line):
        read_file(line)

    # Recebe o número do gerenciador de espaço livre.
    def do_espaco(self, line):
        espaco(line)

    # Informa o algoritmo de substituição de páginas.
    def do_substitui(self, line):
        substitui(line)

    # Executa os processos definidos no arquivo de trace com o gerenciador de
    # espaço livre e o algoritmo de substituição de páginas escolhidos pelo 
    # usuário.
    def do_executa(self, line):
        executa(line)
    
    # Sai do console e volta pro terminal do shell.
    def do_sai(self, line):
        return True
    do_EOF = do_sai

if __name__ == '__main__':
    console().cmdloop()