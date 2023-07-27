#!/usr/bin/python3

import pandas as pd

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QTableWidget, QTableWidgetItem

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): #Primera interfaz
        self.setWindowTitle("VisDxInt v0.1")
        self.setGeometry(100, 100, 400, 300)  # Establece la posición y tamaño de la ventana
        # calling method
        
        
        # Crea las acciones para los botones de la barra de tareas
        archivo_action = QAction("Archivo", self)
        archivo_action.triggered.connect(self.abrir_archivo)

        herramientas_action = QAction("Herramientas", self)
        herramientas_action.triggered.connect(self.mostrar_herramientas)

        # Crea la barra de tareas y agrega los botones
        barra_tareas = self.addToolBar("Barra de tareas")
        barra_tareas.addAction(archivo_action)
        barra_tareas.addAction(herramientas_action)

    def abrir_archivo(self):
        # Lógica para abrir un archivo
        print("Abrir archivo")

    def mostrar_herramientas(self):
        # Lógica para mostrar las herramientas
        print("Mostrar herramientas")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec_())