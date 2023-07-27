#!/usr/bin/python3

import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTableView
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        return QVariant()

    def rowCount(self, parent):
        return self._data.shape[0]

    def columnCount(self, parent):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return QVariant()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación con PyQt5")
        self.setMinimumSize(800, 600)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.layout = QGridLayout(self.central_widget)
        
        self.create_toolbar()
        self.create_data_table()
        self.create_plot_area()
        self.create_clustering_regression_area()
    
    def create_toolbar(self):
        toolbar_widget = QWidget(self)
        toolbar_layout = QVBoxLayout(toolbar_widget)
        
        file_button = QPushButton("Archivo", self)
        file_button.clicked.connect(self.open_file_dialog)
        toolbar_layout.addWidget(file_button)
        
        tools_button = QPushButton("Herramientas", self)
        toolbar_layout.addWidget(tools_button)
        
        self.layout.addWidget(toolbar_widget, 0, 0, 1, 3)
    
    def create_data_table(self):
        self.data_table = QTableView(self)
        self.layout.addWidget(self.data_table, 1, 0)
    
    def create_plot_area(self):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas, 1, 1)
    
    def create_clustering_regression_area(self):
        area_widget = QWidget(self)
        area_layout = QVBoxLayout(area_widget)
        
        clustering_button = QPushButton("Clustering (KMeans)", self)
        clustering_button.clicked.connect(self.perform_clustering)
        area_layout.addWidget(clustering_button)
        
        regression_button = QPushButton("Regresión logística", self)
        regression_button.clicked.connect(self.perform_regression)
        area_layout.addWidget(regression_button)
        
        self.layout.addWidget(area_widget, 1, 2)
    
    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "CSV Files (*.csv)", options=options)
        
        if file_path:
            data_frame = pd.read_csv(file_path, skiprows=124)
            self.display_data_frame(data_frame)
    
    def display_data_frame(self, data_frame):
        model = PandasModel(data_frame)
        self.data_table.setModel(model)
    
    def perform_clustering(self):
        # Aquí debes implementar el código para realizar el clustering con KMeans
        pass
    
    def perform_regression(self):
        # Aquí debes implementar el código para realizar la regresión logística
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
