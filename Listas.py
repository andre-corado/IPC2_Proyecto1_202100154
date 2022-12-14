class Nodo:
    def __init__(self, dato=None, siguiente=None, id=None, anterior = None):
        self.id = id
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.id = 0

    def insertar(self, dato):
        if self.primero is None:
            self.primero = Nodo(dato=dato, id=self.id)
            self.ultimo = self.primero
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        self.id += 1
        actual.siguiente = Nodo(dato=dato, id=self.id)
        actual.siguiente.anterior = actual
        self.ultimo = actual.siguiente



class NodoEncabezado:
    def __init__(self, id=None):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None


class NodoInterno:
    def __init__(self, fila=None, columna=None, estado=None, contador = 1):
        self.fila = fila
        self.columna = columna
        self.estado = estado
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None
        self.contador = contador

    def sumarContador(self):
        self.contador += 1

class ListaEncabezado:
    def __init__(self, tipo=None):
        self.tipo = tipo
        self.primero = NodoEncabezado = None
        self.ultimo = NodoEncabezado = None

    def insertarEncabezado(self, nuevoEncabezado):
        if self.primero == None:
            self.primero = nuevoEncabezado
            self.ultimo = self.primero
        else:
            if nuevoEncabezado.id < self.primero.id:
                nuevoEncabezado.siguiente = self.primero
                self.primero.anterior = nuevoEncabezado
                self.primero = nuevoEncabezado
            elif nuevoEncabezado.id > self.ultimo.id:
                self.ultimo.siguiente = nuevoEncabezado
                nuevoEncabezado.anterior = self.ultimo
                self.ultimo = nuevoEncabezado
            else:
                aux = self.primero
                while aux != None:
                    if nuevoEncabezado.id < aux.id:
                        nuevoEncabezado.siguiente = aux
                        nuevoEncabezado.anterior = aux.anterior
                        aux.anterior.siguiente = nuevoEncabezado
                        aux.anterior = nuevoEncabezado
                        break
                    elif nuevoEncabezado.id > aux.id:
                        aux = aux.siguiente
                    else:
                        break

    def getEncabezado(self, id):
        aux = self.primero
        while aux != None:
            if id == aux.id:
                return aux
            aux = aux.siguiente
        return None




class MatrizDispersa:
    def __init__(self):
        self.filas = ListaEncabezado(tipo='f')
        self.columnas = ListaEncabezado(tipo='c')

    def insertar(self, nodoInterno: NodoInterno):
        encabezadoFila = self.filas.getEncabezado(nodoInterno.fila)
        encabezadoColumna = self.columnas.getEncabezado(nodoInterno.columna)
        if encabezadoFila == None:
            encabezadoFila = NodoEncabezado(nodoInterno.fila)
            self.filas.insertarEncabezado(encabezadoFila)
        if encabezadoColumna == None:
            encabezadoColumna = NodoEncabezado(nodoInterno.columna)
            self.columnas.insertarEncabezado(encabezadoColumna)
        ## Inserci??n en fila
        if encabezadoFila.acceso == None:
            encabezadoFila.acceso = nodoInterno
        else:
            if int(nodoInterno.columna) < int(encabezadoFila.acceso.columna):
                nodoInterno.derecha = encabezadoFila.acceso
                encabezadoFila.acceso.izquierda = nodoInterno
                encabezadoFila.acceso = nodoInterno
            else:
                aux: NodoInterno = encabezadoFila.acceso
                while aux != None:
                    if int(nodoInterno.columna) == int(aux.columna):
                        aux.sumarContador()
                        break
                    elif int(nodoInterno.columna) < int(aux.columna):
                        nodoInterno.derecha = aux
                        nodoInterno.izquierda = aux.izquierda
                        aux.izquierda.derecha = nodoInterno
                        aux.izquierda = nodoInterno
                        break
                    else:
                        if aux.derecha == None:
                            aux.derecha = nodoInterno
                            nodoInterno.izquierda = aux
                            break
                        else:
                            aux = aux.derecha
        ## Inserci??n en columna
        if encabezadoColumna.acceso == None:
            encabezadoColumna.acceso = nodoInterno
        else:
            if int(nodoInterno.fila) < int(encabezadoColumna.acceso.fila):
                nodoInterno.abajo = encabezadoColumna.acceso
                encabezadoColumna.acceso.arriba = nodoInterno
                encabezadoColumna.acceso = nodoInterno
            else:
                aux2: NodoInterno = encabezadoColumna.acceso
                while aux2 != None:
                    if int(nodoInterno.fila) == int(aux2.fila):
                        break
                    elif int(nodoInterno.fila) < int(aux2.fila):
                        nodoInterno.abajo = aux2
                        nodoInterno.arriba = aux2.arriba
                        aux2.arriba.abajo = nodoInterno
                        aux2.arriba = nodoInterno
                        break
                    else:
                        if aux2.abajo == None:
                            aux2.abajo = nodoInterno
                            nodoInterno.arriba = aux2
                            break
                        else:
                            aux2 = aux2.abajo

    def getCelda(self, fila, columna):
        encabezadoFila = self.filas.getEncabezado(str(fila))
        if encabezadoFila is None:
            return
        else:
            celda = encabezadoFila.acceso
            while celda is not None:
                if celda.columna == str(columna):
                    return celda
                celda = celda.derecha
            return

    def getCeldas(self): # Devuelve una lista enlazada de todas las celdas existentes en la matriz
        listaCeldas = ListaEnlazada()
        encabezadoFila = self.filas.primero
        if encabezadoFila is None:
            return
        while encabezadoFila is not None:
            celda = encabezadoFila.acceso
            while celda is not None:
                listaCeldas.insertar(celda)
                celda = celda.derecha
            encabezadoFila = encabezadoFila.siguiente
        return listaCeldas

    def getCeldasContagiadas(self): # Devuelve una lista enlazada de todas las celdas que fueron contagiadas seg??n la regla 2
        listaCeldas = ListaEnlazada()
        encabezadoFila = self.filas.primero
        if encabezadoFila is None:
            return
        while encabezadoFila is not None:
            celda = encabezadoFila.acceso
            while celda is not None:
                if celda.contador == 3:
                    listaCeldas.insertar(celda)
                celda = celda.derecha
            encabezadoFila = encabezadoFila.siguiente
        return listaCeldas

    def equals(self, segundaRejilla):
        sonIguales = True
        listaCeldas = self.getCeldas()
        nodoCelda = listaCeldas.primero
        while nodoCelda is not None:
            celda = nodoCelda.dato
            if segundaRejilla.getCelda(celda.fila, celda.columna) is None:
                return False
            nodoCelda = nodoCelda.siguiente
        return sonIguales


    def print(self):
        encabezadoFila = self.filas.primero
        while encabezadoFila != None:
            celda = encabezadoFila.acceso
            while celda != None:
                print(celda.fila + celda.columna + ' | ', end='')
                celda = celda.derecha
            print()
            encabezadoFila= encabezadoFila.siguiente