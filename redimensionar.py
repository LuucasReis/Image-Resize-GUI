from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from PyQt5.QtGui import QPixmap
import sys
from designr import *

class Redimensionar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        super().setupUi(self)
        self.pushButton.clicked.connect(self.escolher_imagem)
        self.pushButton_2.clicked.connect(self.red)
        self.pushButton_3.clicked.connect(self.salvar)
    
    def escolher_imagem(self):
        imagem, _= QFileDialog.getOpenFileName(
            self.centralwidget,
            "Escolher imagem",
            r'C:\Users\lukes\Pictures',
        )

        self.lineEdit.setText(imagem)
        self.imgoriginal = QPixmap(imagem)
        self.label.setPixmap(self.imgoriginal)

        self.lineEdit_3.setText(str(self.imgoriginal.width()))
        self.lineEdit_2.setText(str(self.imgoriginal.height()))

    def red(self):
        nova_largura= int(self.lineEdit_3.text())
        self.imagem_nova= self.imgoriginal.scaledToWidth(nova_largura)
        self.label.setPixmap(self.imagem_nova)
        self.lineEdit_3.setText(str(self.imagem_nova.width()))
        self.lineEdit_2.setText(str(self.imagem_nova.height()))
    
    def salvar(self):
        imagem, _= QFileDialog.getSaveFileName(
            self.centralwidget,
            "Salvar imagem",
            r'C:\Users\lukes\Pictures',
        )
        self.imagem_nova.save(imagem,"JPEG")
      
    


if __name__== "__main__":
    qt= QApplication(sys.argv)
    red= Redimensionar()
    red.show()
    qt.exec_()
