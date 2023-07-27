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
        self.setGeometry(200, 200, 500, 400)  # Establece la posición y tamaño de la ventana

        archivo_ac = QAction("Abrir archivo", self)
        archivo_ac.triggered.connect(self.abrir_archivo)

    #   tools_bar = self.addToolBar("Barra de tareas")
    #   tools_bar.addAction(archivo_ac)

    #def abrir_archivo(self):
    #	options = QFileDialog.Options()
    #	file, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "CSV Files (*.csv)", options=options)

    #	if file_path:
    #		data_frame = pd.read_csv(file_path)
    
    #		self.display_data_frame(data_frame)


    	#file_dialog = QFileDialog()
    	#file_path, _ = file_dialog.getOpenFileName(self, "Abrir archivo")


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())