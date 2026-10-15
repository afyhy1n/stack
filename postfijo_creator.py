# POSTFIJO

def postfijo(listado):
    exitt = []
    stack = []

    operador = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '**': 3,
        '^': 3,
        '(': 0,
        ')': 0
    }
    for caracter in listado:
        # print(caracter)
        if caracter == "(":  # SI ES UN ( AL INICIO ENTRA DIRECTO, LOS MISMO SI NO ESTA AL INICIO
            stack.append(caracter)
        elif caracter == ")":  # SI ES UN ) TODOS LOS OPERADORES HASTA LLEGAR A ( ENTRARAN A exitt
            # print("EXIT: ", exitt)
            # print("STACK: ", stack)
            while stack and stack[-1] != "(":
                exitt.append(stack.pop())
                # print ("EXIT: ", exitt)
                # print ("STACK: ", stack)
            stack.pop()  # ELIMINAMOS EL PARENTESIS ( QUE TENIAMOS GUARDADO EN stack

        elif caracter in operador:  # SI EL CARACTER ES UN OPERADOR SE EVALUARA DENTRO QUE PESO TIENE
            if stack:  # CORROBORAMOS DE QUE TENGAMOS ALGO DENTRO DE STACK [+]=1 *=2 -> [+,*]
                while stack and operador[stack[-1]] >= operador[
                    caracter]:  # AÑADIMOS OTRO COMPROBADOR DE CANTIDAD Y SI SE CUMPLE SIGNIFICA QUE SE DEBE DE SACAR TODOS LOS SIGNOS QUE SEAN >= EL CARCTER ENTRANTE
                    # print("EXIT: ", exitt)
                    # print("STACK: ", stack)
                    exitt.append(stack.pop())  # EL ULTIMO DIGITO SE AÑADIRA A exitt Y ELIMINA EL ULTIMO CARACTER
                    # print("EXIT: ", exitt)
                    # print("STACK: ", stack)
                stack.append(caracter)  # CUANDO YA NO SE CUMPLAN LAS CONDICIONES AÑADIMOS caracter A stack
            else:
                stack.append(caracter)  # SI NO HAY NADA NO SE COMPRUEBA NADA Y PASA DIRECTO
        else:  # SI NO ES UN OPERADOR, SIGNIFICA QUE ES UN NÚMERO Y PASA DIRECTO A exitt
            exitt.append(caracter)
    if stack:  # SI QUEDAN OPERADORES DENTRO DE stack PERO YA NO HAY DIGITOS A LEER, SE METEN DIRECTAMENTE A exitt
        while stack:
            exitt.append(stack.pop())
    # print("EXIT: ",exitt)
    # print("STACK: ",stack)
    return exitt