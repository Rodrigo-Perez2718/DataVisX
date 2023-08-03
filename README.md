# DataVisX

DataVisX contempla la creación de una interfaz gráfica para visualizar problemas relacionados con el tratamiento de datos, lo que es una tarea de gran relevancia en el ámbito de la programación científica.

El objetivo principal de este proyecto es proporcionar a los científicos y analistas de datos una interfaz gráfica amigable, que les permita cargar, visualizar y manipular conjuntos de datos de manera eficiente, reduciendo así las horas de programación requeridas para lograr un análisis completo.

La interfaz gráfica se diseña de manera intuitiva, con una disposición clara de los elementos para garantizar una experiencia de usuario fluida. Se puede cargar conjuntos de datos desde archivos o fuentes externas, y se proporcionarán opciones para el tratamiento de los datos en cuestión. Además, se ofrecerá la posibilidad de generar visualizaciones gráficas interactivas, como gráficos de dispersión, clustering, regresion logística y lineal, que ayuden a comprender rápidamente la estructura y características de los datos.

Asimismo, se implementan funcionalidades para el versionado de los datos, lo que permitirá comparar diferentes versiones de un conjunto de datos y realizar análisis comparativos. Esto resulta especialmente útil en el caso de conjuntos de datos en constante actualización o en situaciones donde se realizan modificaciones en los mismos.

Con esta herramienta, buscamos facilitar el trabajo de los profesionales involucrados en el análisis de datos, ofreciendo una solución efectiva y amigable para el manejo y visualización de información, lo que permitirá tomar decisiones informadas y obtener conocimientos valiosos a partir de los datos.
## Instalación

Para la instalación de nuestra herramienta, se requiere realizar los siguientes pasos:

Descargar y descomprimir el archivo DATAVISX2.ZIP, que contiene todos los archivos necesarios para la instalación.

Una vez descomprimido el archivo, se debe abrir una terminal en el equipo.

En la terminal, se debe ejecutar el siguiente comando: "python -m pip install ."

Es importante tener en cuenta que este proceso está diseñado para funcionar en editores que utilizan la base de datos del computador, como Visual Studio Code, el cual fue el editor implementado y probado para esta herramienta.

Es importante mencionar que en otros editores, como Google Colab, este método de instalación podría no funcionar debido a las limitaciones del entorno. En tales casos, se recomienda seguir las instrucciones específicas proporcionadas por el editor o utilizar un entorno de desarrollo adecuado para la instalación.

## Uso

Para utilizar el paquete de DataVisX, es necesario realizar la instalación previa del mismo. Una vez instalado, se pueden importar los diferentes módulos disponibles para utilizar las funcionalidades relacionadas con la interfaz gráfica, clustering y regresión.

## Interfaz Gráfica:
Para utilizar la interfaz gráfica, es necesario importar el módulo model_graf desde el paquete datavis.Graficinterface. Además, se importa el módulo QApplication de PyQt5 para crear la aplicación gráfica.
from datavis.Graficinterface import model_graf as mg
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mg.MainWindow()
    window.show()
    sys.exit(app.exec_())

En este código, se crea una instancia de QApplication para inicializar la aplicación gráfica. Luego, se crea una instancia de MainWindow desde el módulo model_graf y se muestra la ventana. Finalmente, se inicia el bucle de la aplicación utilizando app.exec_().

## Clustering:
Para utilizar las funcionalidades de clustering, es necesario importar el módulo model_cluster desde el paquete datavis.Clustering.
from datavis.Clustering import model_cluster as mc

Este módulo proporciona la clase Astrodata, que permite realizar agrupaciones espaciales utilizando el algoritmo DBSCAN y K-means. Para más detalles sobre el uso de esta clase y sus métodos, se puede usar help(mc) o revisar los comentarios del código fuente en el módulo model_cluster.

# Regresión:
Para utilizar las funcionalidades de regresión lineal y logística, se debe importar el módulo model_reg desde el paquete datavis.Regresion.

from datavis.Regresion import model_reg as mr

l módulo model_reg proporciona la clase AstroReg, que permite realizar regresiones lineales y de regresión logística. Para más detalles sobre el uso de esta clase y sus métodos, se puede usar help(mr) o revisar los comentarios del código fuente en el módulo model_reg.

En resumen, el paquete DataVisX proporciona una interfaz gráfica y funcionalidades para realizar clustering y regresión. Cada módulo debe ser importado adecuadamente para acceder a sus funcionalidades, y se pueden obtener más detalles de uso utilizando help() o revisando los comentarios del código fuente en cada módulo.

## Dependencias

- Python 3.8 o superior
- numpy 
- matplotlib
- scipy
- scikit-learn
- PyQt5
- Pandas


## Licencia

Este proyecto está bajo la Licencia MIT. Ver [LICENSE](LICENSE) para más información.
