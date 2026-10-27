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
        expr = list(self.postfijo.exitt) # EXPRESIÓN COPIA DE LA LISTA self.postfijo.exitt
        print(*expr) # PRINT DE LA LISTA INICIAL

        while len(expr) > 1: # MIENTRAS QUE EN LA LISTA SE ENCUENTRE ALGUN DIGITO SEGUIRA IMPRIMIENDO
            for i, caracter in enumerate(expr):
                if caracter in ('+', '-', '*', 'x', 'X', '/', '^', '**', '<', '>', '<=', '>=', '=', '!=', 'AND', 'OR'):
                    # SI ENCUENTRA UN OPERADOR SIGNIFICA QUE HAY 2 NUMERADORES ANTES, ENTONCES:
                    a = float(expr[i - 2]) # [10, 20, +, 30, +] -> 1O
                    b = float(expr[i - 1]) # [10, 20, +, 30, +] -> 20
                    if caracter == '+':
                        r = a + b
                    elif caracter == '-':
                        r = a - b
                    elif caracter in ('*', 'x', 'X'):
                        r = a * b
                    elif caracter == '/':
                        r = a / b
                    elif caracter == '^' or caracter == '**':
                        r = a ** b
                    elif caracter == '<':
                        r = a < b
                    elif caracter == '>':
                        r = a > b
                    elif caracter == '<=':
                        r = a <= b
                    elif caracter == '>=':
                        r = a >= b
                    elif caracter == '=':
                        r = a == b
                    elif caracter == '!=':
                        r = a != b
                    elif caracter == 'AND':
                        r = bool(a) and bool(b)
                    elif caracter == 'OR':
                        r = bool(a) or bool(b)
                    expr[i - 2 : i + 1] = [r]
                    print(*expr)
                    break
        return f"\nRESULTADO FINAL: \n{bool(float(expr[0]))} / {float(expr[0])}"


if __name__ == "__main__":

    x=Assembler()
    print(x.calculadora())