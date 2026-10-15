class Postfijo:
    def __init__(self, lista_tokenizada):
        self.lista_tokenizada = lista_tokenizada
        self.exitt = []
        self.stack = []
        self.operador = {
            '+': 1,
            '-': 1,
            '*': 2,
            'x': 2,
            'X': 2,
            '/': 2,
            '**': 3,
            '^': 3,
            '(': 0,
            ')': 0}

    def post_creador(self):
        for caracter in self.lista_tokenizada:
            if caracter == "(":
                self.stack.append(caracter)
            elif caracter == ")":
                while self.stack and self.stack[-1] != "(":
                    self.exitt.append(self.stack.pop())
                self.stack.pop()
            elif caracter in self.operador:
                if self.stack:
                    while self.stack and self.operador[self.stack[-1]] >= self.operador[caracter]:
                        self.exitt.append(self.stack.pop())
                    self.stack.append(caracter)
                else:
                    self.stack.append(caracter)
            else:
                self.exitt.append(caracter)
        if self.stack:
            while self.stack:
                self.exitt.append(self.stack.pop())
        return self.exitt