import xml.etree.ElementTree as ET
from Paciente import Paciente
from tkinter import filedialog
from Listas import *
import os


def AbrirFileExplorer():
    ruta = filedialog.askopenfilename(initialdir="C:/Users/SergioLima/Downloads", title="Elige un archivo XML",
                                      filetypes=(("XML files", "*.xml*"),("All files", "*.xml*")))
    return ruta

def lectura(ruta, ListaPacientes):
    tree = ET.parse(ruta)
    print('________________________________________________\n\t\tSTATUS DE LECTURA:\n\n')
    for paciente in tree.findall('paciente'):
        nombre = paciente.find('.//nombre').text
        edad = paciente.find('.//edad').text
        periodos = paciente.find('.//periodos').text
        m = paciente.find('.//m').text

        if int(m) <= 10000 and int(periodos) <= 10000 and (int(m) % 10) == 0:
            rejilla = MatrizDispersa()
            for celda in paciente.iter('celda'):
                coordenadas = celda.attrib
                celda = NodoInterno(coordenadas.get('f'), coordenadas.get('c'), estado='1')
                rejilla.insertar(celda)
            nuevoPaciente = Paciente(nombre, edad, periodos, m, rejilla)
            ListaPacientes.insertar(nuevoPaciente)
            print('Paciente: ', nombre,' creado.\n')
        else:
          print('ERROR. Variables no válidas en paciente: ', nombre)

if __name__ == '__main__':
    while True:
        os.system('cls')
        print('1.\tIngresar archivo')
        print('2.\tSalir')
        menu = input()
        if menu == '1':
            ruta = AbrirFileExplorer()
            print('\nLa ruta elegida es:\t', ruta)
            print()
            print('Ingrese Y o y para confirmar la ruta.\n')
            menu = input()
            if menu == 'Y' or menu == 'y':
                listaPacientes = ListaEnlazada()
                lectura(ruta, listaPacientes)
                nodo = listaPacientes.primero
                while nodo is not None:
                    nodo.dato.analizarCaso(int(nodo.dato.m), int(nodo.dato.periodos))
                    nodo = nodo.siguiente
                input()
            else:
                print('Instrucción no válida')
                input()
        elif menu == '2':
            break