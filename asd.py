class Hola:
    def __init__(self, numero=None):
        if numero is None:
            self.numero=0
        else:
            self.numero=numero

    def dame_un_tres(self):
        return 3


one = Hola().dame_un_tres()

print(one)
