# CREADOR DE INFIJO
class Infijo:
    def tokenizar(texto):
        lista_tokens = []
        numero_assembly = ""

        for caracter in texto:  # VA A RECORRER UNO POR UNO EL TEXTO
            if caracter.isdigit() or caracter == ".":  # ESTO ESPECIFICA QUE SI EL caracter ES UN DIGITO O UN . CONTINUARA
                numero_assembly += caracter  # AÑADIMOS EL caracter AL CONSTRUCTOR DE NUMEROS
                print(numero_assembly)

            else:  # SIGNIFICA QUE SI LLEGA A VER UN OPERADOR, LO QUE ESTE DENTRO DE numero_assembly SE PASARA A LA LISTA: lista_tokens
                if numero_assembly:  # SI ES FALSO SIGNIFICA QUE NO HAY NADA
                    lista_tokens.append(numero_assembly)
                    numero_assembly = ""  # REINICIAMOS EL CONSTRUCTOR DESPUES DE AÑADIR A lista_tokens
                if caracter != " ":  # SI TENEMOS 123 + 4 Y SE LEE EL ESPACIO, SE IGNORARA, SI NO ES UN ESPACIO PERO TAMPOCO UN NUMERO ES UN OPERADOR
                    lista_tokens.append(caracter)
            # print(numero_assembly) # DEBUG
        # AL TERMINAR EL PROCESO SI SE TERMINA CON UN NUMERO, ESTE QUEDA DENTRO DE numero_assembly POR LO QUE SE DEBE AÑADIR A LA LISTA
        # print(numero_assembly) # DEBUG
        if numero_assembly:
            lista_tokens.append(numero_assembly)
        return lista_tokens