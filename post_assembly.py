# SOLUCION DE LA TRADUCCIÓN DEL STACK
from text import Main
from infijo_creator import Infijo
from postfijo_creator import Postfijo

class Assembler:
    def __init__(self):
        entrada = Main()
        tokens = Infijo(entrada.texto).tokenizar()
        self.postfijo = Postfijo(tokens)
        self.postfijo.post_creador()

    def calculadora(self):
        pila=[]
        for caracter in self.postfijo.exitt:
            if caracter in ('+', '-', '*', 'x', 'X', '/', '^', '**'):
                b = pila.pop()
                a = pila.pop()
                if caracter == '+':
                    pila.append(a+b)
                elif caracter == '-':
                    pila.append(a-b)
                elif caracter == '*' or caracter == 'x' or caracter == 'X':
                    pila.append(a*b)
                elif caracter == '/':
                    pila.append(a/b)
                elif caracter == '^' or caracter == '**':
                    pila.append(a**b)
            else:
                pila.append(float(caracter))
        return pila[0]


if __name__ == "__main__":

    x=Assembler()
    print(x.calculadora())