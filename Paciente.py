from Listas import *
import os

class Paciente:
    def __init__(self, nombre, edad, periodos, m, primeraRejilla):
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.m = m
        self.n = None
        self.n1 = None
        self.primeraRejilla = primeraRejilla
        self.rejillas = ListaEnlazada()
        self.rejillas.insertar(primeraRejilla)
        self.diagnostico = 'leve'

    def agregarRejilla(self, rejilla):
        self.rejillas.insertar(rejilla)

    def analizarCaso(self, m, periodos):
        print('________________________________________________\n\n\t\tANÁLISIS DE CASO: ', self.nombre+'\n')
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
            self.agregarRejilla(nuevaRejilla)
            print('\n------------------------------------------------------\n\t\tPeriodo ' + str(periodo))
            nuevaRejilla.print()
            rejilla = nuevaRejilla
        self.diagnosticar()


    def diagnosticar(self):
        diagnosticado = False
        nodo = self.rejillas.primero.siguiente
        # Por cada rejilla
        while nodo is not None:
            rejilla = nodo.dato
            if rejilla.equals(self.primeraRejilla):
                self.n = nodo.id
                if self.n == 1:
                    self.diagnostico = str('mortal')
                elif self.n > 1:
                    self.diagnostico = str('grave')
                diagnosticado = True
                break
            nodo = nodo.siguiente

        if not diagnosticado:
            # Todas las rejillas desde la última hacia la primera
            nodo = self.rejillas.primero.siguiente
            while nodo is not None:
                rejilla = nodo.dato
                # Todas las rejillas desde el periodo 1 hasta el actual
                nodoAux = self.rejillas.ultimo
                while nodoAux is not None:
                    if nodoAux.id == nodo.id:
                        break
                    rejillaAux = nodoAux.dato
                    if rejilla.equals(rejillaAux):
                        self.n = nodo.id
                        self.n1 = (nodoAux.id - nodo.id)
                        if self.n1 == 1:
                            self.diagnostico = str('mortal')
                        elif self.n1 > 1:
                            self.diagnostico = str('grave')
                    nodoAux = nodoAux.anterior
                nodo = nodo.siguiente
        print('----------------------------------------------------------\nEl diagnóstico del paciente es un caso ' + self.diagnostico + '\nCon un periodo de: ' + str(self.n))
        if self.n1 is not None:
            print('Se repite a los ' + str(self.n1) + ' periodos.')

    def hacerPDF(self):
        i = 1
        graphviz = 'digraph Patron{ \n node[shape =box, width = 1, height = 1]; \n edge[style = invis]; \n ranksep = 0 \n subgraph Cluster_A{ \n label = "' + '| Paciente: ' + self.nombre + ' | Edad: ' + str(
            self.edad) + ' | Periodo: ' + str(
            self.periodos) + ' |' + ' "   \n fontcolor ="black" \n fontsize = 41 \n bgcolor ="#F1DFB2" \n'
        nodo = None
        while nodo is not None:
            if nodo.getEstado() == 1:
                graphviz += 'node{}[fontcolor = "#59A94A" fillcolor = "#59A94A" style = filled]; \n'.format(i)
                graphviz += 'node{}[fontcolor = "#EEAEBA" fillcolor = "#EEAEBA" style = filled]; \n'.format(i)
            nodo = nodo.siguiente
            i += 1
        i = 1
        j = 2

        for h in range((int(self.m) * int(self.m)) - 1):
            graphviz += 'node{}->node{} \n'.format(i, j)
            i += 1
            j += 1

        i = 1
        for h in range(int(self.m)):
            graphviz += '{ rank = same'

            for g in range(int(self.m)):
                graphviz += ';node{}'.format(i)
                i += 1
            graphviz += '} \n'

        graphviz += '} \n }'

        documento = 'grafica' + self.nombre + '.txt'
        with open(documento, 'w') as grafica:
            grafica.write(graphviz)
        pdf = 'grafica' + str(self.periodos) + '.jpg'
        os.system("dot.exe -Tjpg " + documento + " -o " + pdf)


    def printRejilla(self, rejilla):
        encabezadoFila = rejilla.filas.primero
        while encabezadoFila != None:
            celda = encabezadoFila.acceso
            while celda != None:
                print(celda.fila + celda.columna + ' | ', end='')
                celda = celda.derecha
            print()
            encabezadoFila = encabezadoFila.siguiente
