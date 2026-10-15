# SOLUCION DE LA TRADUCCIÓN DEL STACK
from main import Main
from infijo_creator import Infijo
from postfijo_creator import Postfijo

class Assembler:
    def __init__(self):
        entrada = Main()
        tokens = Infijo(entrada.texto).tokenizar()
        self.postfijo = Postfijo(tokens)
        self.postfijo.post_creador()

    def calculadora(self):
        pass


x = Assembler()
print(x.postfijo.exitt)