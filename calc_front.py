import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

from calculadora_mirian import Calculadora

#Criando uma instancia do QAplication
app = QApplication([])

#Criando o GUI
janela = QWidget()
janela.setWindowTitle('Calculadora')
janela.setGeometry(800, 100, 200, 80)

#mostrar app
janela.show()

#Rodar em loop
sys.exit(app.exec())