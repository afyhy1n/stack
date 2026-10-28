class Infijo:
    def __init__(self, texto):
        self.texto = texto.upper()
        self.lista_tokens = []
        self.numero_assembly = ""

    def limpiar_vacios(self):
        t = self.lista_tokens
        i = 0
        while i < len(t) - 1:
            if t[i] == "(" and t[i + 1] == ")":
                del t[i:i + 2]
                if i > 0 and t[i - 1] == "*":  # el * implícito sobrante
                    del t[i - 1]
                    i -= 1
                i = max(i - 1, 0)  # reevaluar, pueden anidarse
            else:
                i += 1
    def tokenizar(self):
        for caracter in self.texto:
            if caracter.isdigit() or caracter == ".":
                self.numero_assembly += caracter
            else:
                if self.numero_assembly:
                    if self.lista_tokens and self.lista_tokens[-1] == ")": # CIERRE DE OPERADOR
                        self.lista_tokens.append("*")
                    self.lista_tokens.append(self.numero_assembly)
                    self.numero_assembly = ""
                if caracter != " ":
                    if caracter == "*" and self.lista_tokens and self.lista_tokens[-1] == "*":
                        self.lista_tokens[-1] = "**"
                    elif caracter == "=" and self.lista_tokens and self.lista_tokens[-1] == "<":
                        self.lista_tokens[-1] = "<="
                    elif caracter == "=" and self.lista_tokens and self.lista_tokens[-1] == ">":
                        self.lista_tokens[-1] = ">="
                    elif caracter == "=" and self.lista_tokens and self.lista_tokens[-1] == "!":
                        self.lista_tokens[-1] = "!="
                    elif caracter == "=" and self.lista_tokens and self.lista_tokens[-1] == "=":
                        self.lista_tokens[-1] = "=="
                    elif caracter == "(" and self.lista_tokens and (self.lista_tokens[-1].isdigit() or self.lista_tokens[-1] == ")"):
                        self.lista_tokens.append("*")
                        self.lista_tokens.append("(")
                    elif caracter == "R" and self.lista_tokens and self.lista_tokens[-1] == "O":
                        self.lista_tokens[-1] = "OR"
                    elif caracter == "D" and len(self.lista_tokens) >= 2 and self.lista_tokens[-1] == "N" and self.lista_tokens[-2] == "A":
                        self.lista_tokens[-2:] = ["AND"]
                    elif caracter == "T" and len(self.lista_tokens) >= 2 and self.lista_tokens[-1] == "O" and self.lista_tokens[-2] == "N":
                        self.lista_tokens[-2:] = ["NOT"]
                    else:
                        self.lista_tokens.append(caracter)
        if self.numero_assembly:
            if self.lista_tokens and self.lista_tokens[-1] == ")": # CIERRE DE NUMERADOR
                self.lista_tokens.append("*")
            self.lista_tokens.append(self.numero_assembly)
        if self.lista_tokens.count("(") != self.lista_tokens.count(")"):
            for i in range(self.lista_tokens.count("(")-1):
                self.lista_tokens.append(")")
        self.limpiar_vacios()
        return self.lista_tokens



x = Infijo("3(1+3)(2(1(((((").tokenizar()
print(x)