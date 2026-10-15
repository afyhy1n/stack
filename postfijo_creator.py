# POSTFIJO
class Postfijo:
    def __init__(self, lista_tokenizada):
        self.lista_tokenizada = lista_tokenizada
        self.exitt = []
        self.stack = []
        self.operador = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '**': 3,
            '^': 3,
            '(': 0,
            ')': 0}

    def post_creador(self):
        for caracter in self.lista_tokenizada:
            # print(caracter)
            if caracter == "(":  # SI ES UN ( AL INICIO ENTRA DIRECTO, LOS MISMO SI NO ESTA AL INICIO
                self.stack.append(caracter)
            elif caracter == ")":  # SI ES UN ) TODOS LOS OPERADORES HASTA LLEGAR A ( ENTRARAN A exitt
                # print("EXIT: ", exitt)
                # print("STACK: ", stack)
                while self.stack and self.stack[-1] != "(":
                    self.exitt.append(self.stack.pop())
                    # print ("EXIT: ", exitt)
                    # print ("STACK: ", stack)
                self.stack.pop()  # ELIMINAMOS EL PARENTESIS ( QUE TENIAMOS GUARDADO EN stack

            elif caracter in self.operador:  # SI EL CARACTER ES UN OPERADOR SE EVALUARA DENTRO QUE PESO TIENE
                if self.stack:  # CORROBORAMOS DE QUE TENGAMOS ALGO DENTRO DE STACK [+]=1 *=2 -> [+,*]
                    while self.stack and self.operador[self.stack[-1]] >= self.operador[caracter]:  # AÑADIMOS OTRO COMPROBADOR DE CANTIDAD Y SI SE CUMPLE SIGNIFICA QUE SE DEBE DE SACAR TODOS LOS SIGNOS QUE SEAN >= EL CARCTER ENTRANTE
                        # print("EXIT: ", exitt)
                        # print("STACK: ", stack)
                        self.exitt.append(self.stack.pop())  # EL ULTIMO DIGITO SE AÑADIRA A exitt Y ELIMINA EL ULTIMO CARACTER
                        # print("EXIT: ", exitt)
                        # print("STACK: ", stack)
                    self.stack.append(caracter)  # CUANDO YA NO SE CUMPLAN LAS CONDICIONES AÑADIMOS caracter A stack
                else:
                    self.stack.append(caracter)  # SI NO HAY NADA NO SE COMPRUEBA NADA Y PASA DIRECTO
            else:  # SI NO ES UN OPERADOR, SIGNIFICA QUE ES UN NÚMERO Y PASA DIRECTO A exitt
                self.exitt.append(caracter)
        if self.stack:  # SI QUEDAN OPERADORES DENTRO DE stack PERO YA NO HAY DIGITOS A LEER, SE METEN DIRECTAMENTE A exitt
            while self.stack:
                self.exitt.append(self.stack.pop())
        # print("EXIT: ",exitt)
        # print("STACK: ",stack)
        return self.exitt