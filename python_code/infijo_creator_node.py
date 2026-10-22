from node_methods import ListNode
class Infijo_node:
    def __init__(self, texto):
        self.texto = texto.upper()
        self.lista_tokens = ListNode()
        self.numero_assembly = ""

    # INSERTAR AL FINAL

    def tokenizar_node(self):
        for caracter in self.texto:
            if caracter.isdigit() or caracter == ".":
                self.numero_assembly += caracter
            else:
                if self.numero_assembly:
                    self.lista_tokens.insertar_fin(self.numero_assembly)
                    self.numero_assembly = ""
                if caracter != " ":
                    ultimo = self.lista_tokens.regresar_ultimo()
                    penultimo = self.lista_tokens.regresar_penultimo()

                    if caracter == "*" and ultimo == "*":
                        self.lista_tokens.reemplazar_ultimo("**")
                    elif caracter == "=" and ultimo == "<":
                        self.lista_tokens.reemplazar_ultimo("<=")
                    elif caracter == "=" and ultimo == ">":
                        self.lista_tokens.reemplazar_ultimo(">=")
                    elif caracter == "=" and ultimo == "!":
                        self.lista_tokens.reemplazar_ultimo("!=")
                    elif caracter == "R" and ultimo == "O":
                        self.lista_tokens.reemplazar_ultimo("OR")
                    elif caracter == "D" and ultimo == "N" and penultimo == "A":
                        # A, N + D -> AND (UN SOLO NODO)
                        self.lista_tokens.reemplazar_penultimo("AND")
                        self.lista_tokens.eliminar_ultimo()
                    else:
                        self.lista_tokens.insertar_fin(caracter)

        if self.numero_assembly:
            self.lista_tokens.insertar_fin(self.numero_assembly)
        return self.lista_tokens

