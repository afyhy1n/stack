from node_methods import *
class Postfijo_node:
    def __init__(self, lista_tokenizada):
        self.lista_tokenizada = lista_tokenizada
        self.exitt = ListNode()
        self.stack = ListNode()
        self.operador = {
            'OR': 1,
            'AND': 2,
            'NOT': 3,

            '=': 4,
            '==': 4,
            '!=': 4,

            '<': 5,
            '>': 5,
            '<=': 5,
            '>=': 5,

            '+': 6,
            '-': 6,

            '*': 7,
            'X': 7,
            '/': 7,

            '**': 8,
            '^': 8,

            '(': 0,
            ')': 0
        }
        self.derecha = {'**', '^'}

    def post_creador_node(self):
        for caracter in self.lista_tokenizada:
            if caracter == "(":
                self.stack.insertar_fin(caracter)

            elif caracter == ")":
                while not self.stack.esta_vacia() and self.stack.regresar_ultimo() != "(":
                    self.exitt.insertar_fin(self.stack.sacar_ultimo())
                self.stack.eliminar_ultimo()          # DESCARTA EL "("

            elif caracter in self.operador:
                while not self.stack.esta_vacia():
                    tope = self.operador[self.stack.regresar_ultimo()]
                    actual = self.operador[caracter]
                    if tope > actual or (tope == actual and caracter not in self.derecha):
                        self.exitt.insertar_fin(self.stack.sacar_ultimo())
                    else:
                        break
                self.stack.insertar_fin(caracter)

            else:
                self.exitt.insertar_fin(caracter)

        while not self.stack.esta_vacia():
            self.exitt.insertar_fin(self.stack.sacar_ultimo())
        return self.exitt


    def __str__(self):
        return str(self.exitt)


