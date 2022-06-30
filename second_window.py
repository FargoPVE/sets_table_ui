from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClickedData(object):
    def setupUi(self, ClickedData):
        ClickedData.setObjectName("ClickedData")
        ClickedData.resize(340, 200)
        ClickedData.setTabletTracking(True)
        ClickedData.setFocusPolicy(QtCore.Qt.ClickFocus)
        ClickedData.setStyleSheet("background-color: rgb(255, 87, 87);")
        self.centralwidget = QtWidgets.QWidget(ClickedData)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 280, 50))
        self.lineEdit.setStyleSheet("background-color: rgba(233, 233, 233, 243);\n"
                                      "color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 120, 280, 50))
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_2.setStyleSheet("background-color: rgba(243, 243, 243, 243);\n"
                                      "color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        ClickedData.setCentralWidget(self.centralwidget)

        self.retranslateUi(ClickedData)
        QtCore.QMetaObject.connectSlotsByName(ClickedData)

    def retranslateUi(self, ClickedData):
        _translate = QtCore.QCoreApplication.translate
        ClickedData.setWindowTitle(_translate("ClickedData", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClickedData = QtWidgets.QMainWindow()
    ui = Ui_ClickedData()
    ui.setupUi(ClickedData)
    ClickedData.show()
    sys.exit(app.exec_())

