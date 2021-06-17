from nodo import Nodo
class Arbol:
    def __init__(self,dato):
        self.raiz=Nodo(dato)

    def Insertar(self, nodo,dato):
        if dato < nodo.dato:
            if nodo.Hizq== None:
                nodo.Hizq= Nodo(dato)
            else:
                self.Insertar(nodo.Hizq,dato)
        elif dato > nodo.dato:
            if nodo.Hder== None:
                nodo.Hder= Nodo(dato)
            else:
                self.Insertar(nodo.Hder,dato)
        else:
            print("El Nodo ya existe")

    def inOrden(self, nodo):
        if nodo is not None:
            self.inOrden(nodo.Hizq)
            print(nodo.dato,end=" ")
            self.inOrden(nodo.Hder)

    def Agregar(self,dato):
        self.Insertar(self.raiz,dato)
    
    def inorden(self):
        print("Árbol inorden: \n")
        self.inOrden(self.raiz)
        print("")