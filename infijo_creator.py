# CREADOR DE INFIJO
class Infijo:
    def __init__(self, texto):
        self.texto = texto
        self.lista_tokens = []
        self.numero_assembly = ""



    def tokenizar(self):

        for caracter in self.texto:  # VA A RECORRER UNO POR UNO  EL TEXTO
            if caracter.isdigit() or caracter == ".":  # ESTO ESPECIFICA QUE SI EL caracter ES UN DIGITO O UN . CONTINUARA
                self.numero_assembly += caracter  # AÑADIMOS EL caracter AL CONSTRUCTOR DE NUMEROS
                # print(numero_assembly)

            else:  # SIGNIFICA QUE SI LLEGA A VER UN OPERADOR, LO QUE ESTE DENTRO DE numero_assembly SE PASARA A LA LISTA: lista_tokens
                if self.numero_assembly:  # SI ES FALSO SIGNIFICA QUE NO HAY NADA
                    self.lista_tokens.append(self.numero_assembly)
                    self.numero_assembly = ""  # REINICIAMOS EL CONSTRUCTOR DESPUES DE AÑADIR A lista_tokens
                if caracter != " ":  # SI TENEMOS 123 + 4 Y SE LEE EL ESPACIO, SE IGNORARA, SI NO ES UN ESPACIO PERO TAMPOCO UN NUMERO ES UN OPERADOR
                    self.lista_tokens.append(caracter)
            # print(self.numero_assembly) # DEBUG
        # AL TERMINAR EL PROCESO SI SE TERMINA CON UN NUMERO, ESTE QUEDA DENTRO DE numero_assembly POR LO QUE SE DEBE AÑADIR A LA LISTA
        # print(self.numero_assembly) # DEBUG
        if self.numero_assembly:
            self.lista_tokens.append(self.numero_assembly)
        return self.lista_tokens