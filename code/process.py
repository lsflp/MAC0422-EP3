class Processo(object):

    # recebe uma linha que descreve o processo e o pid
    def __init__(self, info_string, pid):
        data = info_string.split()
        self.pid = pid
        self.name = data[1]
        self.t0 = int(data[0])
        del data[0]
        del data[0]
        self.positions = [int(i) for i in data[1::2]]
        self.times = [int(i) for i in data[0::2]]

    def __repr__(self):
        return self.name + " (" + str(self.pid) + ")"