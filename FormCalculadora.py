# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created: Tue Sep 23 18:21:49 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FormCalculadora(object):
    def setupUi(self, FormCalculadora):
        FormCalculadora.setObjectName(_fromUtf8("FormCalculadora"))
        FormCalculadora.resize(328, 219)
        self.centralwidget = QtGui.QWidget(FormCalculadora)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.txtn1 = QtGui.QLineEdit(self.centralwidget)
        self.txtn1.setGeometry(QtCore.QRect(120, 20, 101, 31))
        self.txtn1.setObjectName(_fromUtf8("txtn1"))
        self.txtn2 = QtGui.QLineEdit(self.centralwidget)
        self.txtn2.setGeometry(QtCore.QRect(120, 60, 101, 31))
        self.txtn2.setObjectName(_fromUtf8("txtn2"))
        self.txtresultado = QtGui.QLineEdit(self.centralwidget)
        self.txtresultado.setGeometry(QtCore.QRect(120, 100, 101, 31))
        self.txtresultado.setObjectName(_fromUtf8("txtresultado"))
        self.btnsumar = QtGui.QPushButton(self.centralwidget)
        self.btnsumar.setGeometry(QtCore.QRect(250, 20, 75, 23))
        self.btnsumar.setObjectName(_fromUtf8("btnsumar"))
        self.btnmulti = QtGui.QPushButton(self.centralwidget)
        self.btnmulti.setGeometry(QtCore.QRect(250, 80, 75, 23))
        self.btnmulti.setObjectName(_fromUtf8("btnmulti"))
        self.btnrestar = QtGui.QPushButton(self.centralwidget)
        self.btnrestar.setGeometry(QtCore.QRect(250, 50, 75, 23))
        self.btnrestar.setObjectName(_fromUtf8("btnrestar"))
        self.btndividir = QtGui.QPushButton(self.centralwidget)
        self.btndividir.setGeometry(QtCore.QRect(250, 110, 75, 23))
        self.btndividir.setObjectName(_fromUtf8("btndividir"))
        self.btnsalir = QtGui.QPushButton(self.centralwidget)
        self.btnsalir.setGeometry(QtCore.QRect(110, 142, 111, 31))
        self.btnsalir.setObjectName(_fromUtf8("btnsalir"))
        self.lbln1 = QtGui.QLabel(self.centralwidget)
        self.lbln1.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.lbln1.setObjectName(_fromUtf8("lbln1"))
        self.lbln2 = QtGui.QLabel(self.centralwidget)
        self.lbln2.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.lbln2.setObjectName(_fromUtf8("lbln2"))
        self.lblresultado = QtGui.QLabel(self.centralwidget)
        self.lblresultado.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.lblresultado.setObjectName(_fromUtf8("lblresultado"))
        FormCalculadora.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FormCalculadora)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 328, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        FormCalculadora.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FormCalculadora)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FormCalculadora.setStatusBar(self.statusbar)

        self.retranslateUi(FormCalculadora)
        QtCore.QMetaObject.connectSlotsByName(FormCalculadora)

    def retranslateUi(self, FormCalculadora):
        FormCalculadora.setWindowTitle(_translate("FormCalculadora", "Calculadora en Python", None))
        self.btnsumar.setText(_translate("FormCalculadora", "Sumar", None))
        self.btnmulti.setText(_translate("FormCalculadora", "Multiplicar", None))
        self.btnrestar.setText(_translate("FormCalculadora", "Restar", None))
        self.btndividir.setText(_translate("FormCalculadora", "Dividir", None))
        self.btnsalir.setText(_translate("FormCalculadora", "Salir", None))
        self.lbln1.setText(_translate("FormCalculadora", "Primer Número", None))
        self.lbln2.setText(_translate("FormCalculadora", "Segundo Número", None))
        self.lblresultado.setText(_translate("FormCalculadora", "Resultado", None))

