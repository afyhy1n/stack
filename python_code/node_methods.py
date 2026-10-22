from node import Nodo
class ListNode:
    def __init__(self):
        self.selected = None

    def insertar_fin(self, dato):
        nuevo = Nodo(dato)
        # SI LA LISTA ESTA VACIA SE AGREGA UN NODO (INICIO)
        if self.selected == None:
            self.selected = nuevo
            return

        # RECORRE LA LISTA HASTA EL ULTIMO NODO
        actual = self.selected

        while actual.next != None:
            actual = actual.next

        # AÑADE EL ULTIMO NODO
        actual.next = nuevo

    def regresar_ultimo(self):
        if self.selected == None:
            return None
        actual = self.selected
        while actual.next != None:
            actual = actual.next
        return actual.data

    def esta_vacia(self):
        return self.selected == None

    def sacar_ultimo(self):
        dato = self.regresar_ultimo()
        self.eliminar_ultimo()
        return dato

    # REGRESA EL DATO DEL PENULTIMO (NONE SI HAY MENOS DE 2 NODOS)
    def regresar_penultimo(self):
        if self.contar_nodos() < 2:
            return None
        actual = self.selected
        while actual.next.next != None:
            actual = actual.next
        return actual.data

    def imprimir(self):
        actual = self.selected
        # COMPRUEBA QUE EXISTAN NODOS
        while actual != None:
            print(f"[{actual.data}]", end=" -> ")
            actual = actual.next
        # PRINT AL NODO FINAL = None
        # SI NO HAY NODOS EXISTENTES SOLO IMPRIME EL ··· = None
        print("···")

    # REEMPLAZAR ULTIMO
    def reemplazar_ultimo(self, nuevo_dato):
        if self.selected == None:
            return False
        actual = self.selected
        while actual.next != None:
            actual = actual.next
        actual.data = nuevo_dato
        return True

    # REEMPLAZAR PENULTIMO
    def reemplazar_penultimo(self, nuevo_dato):
        # NECESITA AL MENOS 2 NODOS
        if self.contar_nodos() < 2:
            return False

        actual = self.selected
        # SE DETIENE CUANDO EL SIGUIENTE ES EL ULTIMO
        while actual.next.next != None:
            actual = actual.next

        actual.data = nuevo_dato
        return True

    # REEMPLAZAR ANTEPENULTIMO
    def reemplazar_antepenultimo(self, nuevo_dato):
        # NECESITA AL MENOS 3 NODOS
        if self.contar_nodos() < 3:
            return False

        actual = self.selected
        # SE DETIENE CUANDO EL NODO SIGUIENTE ES EL PENULTIMO
        while actual.next.next.next != None:
            actual = actual.next

        actual.data = nuevo_dato
        return True

    def contar_nodos(self):
        contador = 0
        actual = self.selected
        while actual != None:
            contador += 1
            actual = actual.next
        return contador

        # ELIMINAR ULTIMO
    def eliminar_ultimo(self):
        if self.selected == None:
            return False
        # SOLO HAY UN NODO
        if self.selected.next == None:
            self.selected = None
            return True
        actual = self.selected
        while actual.next.next != None:
            actual = actual.next
        actual.next = None
        return True

    # PERMITE USAR "for token in lista"
    def __iter__(self):
        actual = self.selected
        while actual != None:
            yield actual.data
            actual = actual.next

    def __str__(self):
        return " ".join(self)