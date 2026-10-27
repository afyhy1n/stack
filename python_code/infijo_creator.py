class Infijo:
    def __init__(self, texto):
        self.texto = texto.upper()
        self.lista_tokens = []
        self.numero_assembly = ""

    def tokenizar(self):
        for caracter in self.texto:
            if caracter.isdigit() or caracter == ".":
                self.numero_assembly += caracter
            else:
                if self.numero_assembly:
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
                    elif caracter == "R" and self.lista_tokens and self.lista_tokens[-1] == "O":
                        self.lista_tokens[-1] = "OR"
                    elif caracter == "D" and len(self.lista_tokens) >= 2 and self.lista_tokens[-1] == "N" and self.lista_tokens[-2] == "A":
                        self.lista_tokens[-2:] = ["AND"]
                    else:
                        self.lista_tokens.append(caracter)
        if self.numero_assembly:
            self.lista_tokens.append(self.numero_assembly)
        return self.lista_tokens
