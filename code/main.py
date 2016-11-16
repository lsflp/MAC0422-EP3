import cmd
import gerenciador as gen

class console(cmd.Cmd):
    """Simple command processor example."""
    prompt = '> '
    
    def do_carrega(self, line):
        """greet [person] Greet the named person"""
        gen.read_file(line)
    
    def do_exit(self, line):
        """exit - finaliza o programa"""
        print ()
        return True
    do_EOF = do_exit

if __name__ == '__main__':
    console().cmdloop()