from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AcercaAutores(object):
    def setupUi(self, AcercaAutores):
        AcercaAutores.setObjectName("AcercaAutores")
        AcercaAutores.resize(842, 456)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Qt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AcercaAutores.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(AcercaAutores)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(AcercaAutores)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(AcercaAutores)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(AcercaAutores)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(AcercaAutores)
        self.buttonBox.accepted.connect(AcercaAutores.accept)
        self.buttonBox.rejected.connect(AcercaAutores.reject)
        QtCore.QMetaObject.connectSlotsByName(AcercaAutores)

    def retranslateUi(self, AcercaAutores):
        _translate = QtCore.QCoreApplication.translate
        AcercaAutores.setWindowTitle(_translate("AcercaAutores", "Acerca de los Autores"))
        self.textBrowser.setHtml(_translate("AcercaAutores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#000000;\">Estudiantes :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#000000;\"> Liset Silva Oropesa</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#005500;\">                        </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#000000;\">Ariel Plasencia Díaz</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#005500;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#000000;\">Correos :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#000000;\"> l.silva@estudiantes.matcom.uh.cu</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#005500;\">                </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#000000;\">a.plasencia@estudiantes.matcom.uh.cu</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#005500;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#000000;\">Facultad :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#000000;\"> MatCom</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#005500;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#000000;\">Especialidad :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#000000;\"> Ciencia de la Computación</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#005500;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#000000;\">Asignatura :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#000000;\"> Compilación</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#005500;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#000000;\">Curso :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#005500;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#000000;\">2019 - 2020</span></p></body></html>"))
        self.label.setText(_translate("AcercaAutores", "<html><head/><body><p align=\"center\">Acerca de los Autores</p></body></html>"))
