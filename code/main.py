import cmd
from gerenciador import *

class console(cmd.Cmd):
    """Simple command processor example."""
    prompt = '> '
    
    def do_carrega(self, line):
        """carrega  <arquivo> - carrega o arquivo """
        read_file(line)

    def do_espaco(self, line):
        """espaco <num> - informa o gerenciador de estaco live, onde nun: 1 First Fit ;2 Next Fit ;3 Best Fit ;4 Worst Fit"""
        espaco(line)

    def do_substitui(self, line):
        """substitui <num> - algoritmo de substituicao, onde nun: 1 Optimal; 2 Second-Chance; 3 Clock; 4 Least Recently Used"""
        substitui(line)

    def do_executa(self, line):
        """executa <intervalo>"""
        executa(line)
    
    def do_sai(self, line):
        """sai - finaliza o programa"""
        print ()
        return True
    do_EOF = do_sai

if __name__ == '__main__':
    console().cmdloop()