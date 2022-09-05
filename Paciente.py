from Listas import MatrizDispersa
from Listas import ListaEnlazada
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