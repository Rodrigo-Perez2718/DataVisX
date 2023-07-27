#!/usr/bin/python3

import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # Primera interfaz
        self.setWindowTitle("VisDxInt v0.1")
        self.setGeometry(100, 100, 400, 300)  # Establece la posición y tamaño de la ventana

        # Crea las acciones para los botones de la barra de tareas
        archivo_action = QAction("Abrir archivo", self)
        archivo_action.triggered.connect(self.abrir_archivo)

        herramientas_action = QAction("Herramientas", self)
        herramientas_action.triggered.connect(self.mostrar_herramientas)

        # Crea la barra de tareas y agrega los botones
        barra_tareas = self.addToolBar("Barra de tareas")
        barra_tareas.addAction(archivo_action)
        barra_tareas.addAction(herramientas_action)

        # Crea una tabla
        self.table = QTableWidget(self)
        self.table.setColumnCount(0)
        self.table.setRowCount(0)

        # Crea un layout vertical y un widget para contener la tabla
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        # Crea un widget principal y establece el layout vertical
        widget = QWidget(self)
        widget.setLayout(layout)

        # Establece el widget principal como el widget central de la ventana
        self.setCentralWidget(widget)

    def abrir_archivo(self):
        # Abre el cuadro de diálogo para seleccionar un archivo
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Abrir archivo", "", "CSV Files (*.csv)")

        # Verifica si se seleccionó un archivo
        if file_path:
            # Lee el archivo CSV y crea un dataframe de pandas
            df = pd.read_csv(file_path, skiprows=124)

            # Obtén el número de filas y columnas
            num_rows, num_cols = df.shape

                # Establece el número de filas y columnas en la tabla
            self.table.setRowCount(num_rows)
            self.table.setColumnCount(num_cols)

            # Agrega los datos del dataframe a la tabla
            for i, row in enumerate(df.values):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(i, j, item)

    def mostrar_herramientas(self):
        # Lógica para mostrar las herramientas
        print("Mostrar herramientas")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())