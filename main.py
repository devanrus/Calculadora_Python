import sys
from PyQt4 import QtCore, QtGui
from FormCalculadora import Ui_FormCalculadora
from Operaciones import Operaciones


class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # Se crea la instancia de Ui_MainWindow
        self.ventana = Ui_FormCalculadora()
        self.ventana.setupUi(self)
        # Se conectan las senales con los slots
        self.connect(self.ventana.btnsalir, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))
        self.connect(self.ventana.btnsumar, QtCore.SIGNAL('clicked()'), self.sumar)
        self.connect(self.ventana.btnrestar, QtCore.SIGNAL('clicked()'), self.restar)
        self.connect(self.ventana.btnmulti, QtCore.SIGNAL('clicked()'), self.multiplicar)
        self.connect(self.ventana.btndividir, QtCore.SIGNAL('clicked()'), self.dividir)

    def sumar(self):
        objoperaciones = Operaciones(self.ventana.txtn1.text(), self.ventana.txtn2.text())
        self.ventana.txtresultado.setText(str(objoperaciones.sumar()))

    def restar(self):
        objoperaciones = Operaciones(self.ventana.txtn1.text(), self.ventana.txtn2.text())
        self.ventana.txtresultado.setText(str(objoperaciones.restar()))

    def multiplicar(self):
        objoperaciones = Operaciones(self.ventana.txtn1.text(), self.ventana.txtn2.text())
        self.ventana.txtresultado.setText(str(objoperaciones.multiplicar()))

    def dividir(self):
        objoperaciones = Operaciones(self.ventana.txtn1.text(), self.ventana.txtn2.text())
        self.ventana.txtresultado.setText(str(objoperaciones.dividir()))


app = QtGui.QApplication(sys.argv)
mostrar = Main()
mostrar.show()
sys.exit(app.exec_())