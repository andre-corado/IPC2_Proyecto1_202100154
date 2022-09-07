from Listas import *


class Paciente:
    def __init__(self, nombre, edad, periodos, m, primeraRejilla):
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.m = m
        self.primeraRejilla = primeraRejilla
        self.rejillas = ListaEnlazada()
        self.rejillas.insertar(primeraRejilla)
        self.resultado = None

    def agregarRejilla(self, rejilla):
        self.rejillas.insertar(rejilla)

    def analizarCaso(self, m, periodos):
        print('________________________________________________\n\n\t\tANÁLISIS DE CASO: ', self.nombre,'\n\n\tPrimera Rejilla:\n')
        self.printRejilla(self.primeraRejilla)
        rejilla = self.primeraRejilla

        for periodo in range(1, periodos + 1):
            # Por cada celda contagiada
            nuevaRejilla = MatrizDispersa()
            rejillaAuxiliar = MatrizDispersa()
            celdasContagiadas = rejilla.getCeldas()
            nodoCeldaContagiada = celdasContagiadas.primero
            while nodoCeldaContagiada is not None:
                fila = int(nodoCeldaContagiada.dato.fila)
                columna = int(nodoCeldaContagiada.dato.columna)

                # Se busca si tiene exactamente 2 o 3 células vecinas contagiadas.
                # Se contagian las células sanas vecinas a las contagiadas y se añaden a una matriz auxiliar

                celda1 = celda2 = celda3 = celda4 = celda6 = celda7 = celda8 = celda9 = None
                contador = 0
                if (fila - 1) != 0:  # Fila superior
                    if (columna - 1) != 0:
                        celda1 = rejilla.getCelda(fila - 1, columna - 1)    # Se busca si hay otra célula vecina contagiada
                        if celda1:
                            contador += 1
                        else:
                            rejillaAuxiliar.insertar(NodoInterno(str(fila - 1), str(columna - 1))) # Contagiamos la célula sana en la rejilla auxiliar
                    if (columna + 1) <= m:
                        celda3 = rejilla.getCelda(fila - 1, columna + 1)
                        if celda3:
                            contador += 1
                        else:
                            rejillaAuxiliar.insertar(NodoInterno(str(fila - 1), str(columna + 1)))
                    celda2 = rejilla.getCelda(fila - 1, columna)
                    if celda2:
                        contador += 1
                    else:
                        rejillaAuxiliar.insertar(NodoInterno(str(fila - 1), str(columna)))
                if (fila + 1) <= m:  # Fila inferior
                    if (columna - 1) != 0:
                        celda7 = rejilla.getCelda(fila + 1, columna - 1)
                        if celda7:
                            contador += 1
                        else:
                            rejillaAuxiliar.insertar(NodoInterno(str(fila + 1), str(columna - 1)))
                    if (columna + 1) <= m:
                        celda9 = rejilla.getCelda(fila + 1, columna + 1)
                        if celda9:
                            contador += 1
                        else:
                            rejillaAuxiliar.insertar(NodoInterno(str(fila + 1), str(columna + 1)))
                    celda8 = rejilla.getCelda(fila + 1, columna)
                    if celda8:
                        contador += 1
                    else:
                        rejillaAuxiliar.insertar(NodoInterno(str(fila + 1), str(columna)))
                # Misma fila
                if (columna - 1) != 0:
                    celda4 = rejilla.getCelda(fila, columna - 1)
                    if celda4:
                        contador += 1
                    else:
                        rejillaAuxiliar.insertar(NodoInterno(str(fila), str(columna - 1)))
                if (columna + 1) <= m:
                    celda6 = rejilla.getCelda(fila, columna + 1)
                    if celda6:
                        contador += 1
                    else:
                        rejillaAuxiliar.insertar(NodoInterno(str(fila), str(columna + 1)))
                if contador == 2 or contador == 3:
                    nuevaRejilla.insertar(NodoInterno(nodoCeldaContagiada.dato.fila, nodoCeldaContagiada.dato.columna))

                nodoCeldaContagiada = nodoCeldaContagiada.siguiente

            nuevasCeldasContagiadas = rejillaAuxiliar.getCeldasContagiadas()
            # Cada nueva celda contagiada se añade a la nueva rejilla
            nodoCeldaContagiada = nuevasCeldasContagiadas.primero
            while nodoCeldaContagiada is not None:
                nuevaRejilla.insertar(NodoInterno(nodoCeldaContagiada.dato.fila, nodoCeldaContagiada.dato.columna))
                nodoCeldaContagiada = nodoCeldaContagiada.siguiente

            print('________________________________________________\n\n\tRejilla Periodo: '+ str(periodo)+'\n')
            nuevaRejilla.print()
            rejilla = nuevaRejilla

    def printRejilla(self, rejilla):
        encabezadoFila = rejilla.filas.primero
        while encabezadoFila != None:
            celda = encabezadoFila.acceso
            while celda != None:
                print(celda.fila + celda.columna + ' | ', end='')
                celda = celda.derecha
            print()
            encabezadoFila = encabezadoFila.siguiente
