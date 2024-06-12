from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hello(object):
    def setupUi(self, hello):
        hello.setObjectName("hello")
        hello.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(hello)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 286, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(hello)
        QtCore.QMetaObject.connectSlotsByName(hello)

    def retranslateUi(self, hello):
        _translate = QtCore.QCoreApplication.translate
        hello.setWindowTitle(_translate("hello", "Form"))
        self.label_3.setText(_translate("hello", "PENDIDIKAN TEKNNIK INFORMATIKA"))
        self.label_2.setText(_translate("hello", "NAMA : BARIQ OCTAFIANSA PUTRA GANI"))
        self.label.setText(_translate("hello", "NIM : A710230041"))
