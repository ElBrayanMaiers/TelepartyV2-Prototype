from PySide2 import QtCore, QtGui, QtWidgets
import server
import client

class startMenu_Ui(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CreateButton = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateButton.sizePolicy().hasHeightForWidth())
        self.CreateButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CreateButton.setFont(font)
        self.CreateButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CreateButton.setObjectName("CreateButton")
        self.CreateButton.clicked.connect(self.createButtonAction)
        self.verticalLayout.addWidget(self.CreateButton)
        self.JoinButton = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JoinButton.sizePolicy().hasHeightForWidth())
        self.JoinButton.setSizePolicy(sizePolicy)
        self.JoinButton.clicked.connect(self.joinButtonAction)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.JoinButton.setFont(font)
        self.JoinButton.setObjectName("JoinButton")
        self.verticalLayout.addWidget(self.JoinButton)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def createButtonAction(self):
        self.MenuWidget = QtWidgets.QWidget()
        self.ui = server.createMenu_IU()
        self.ui.setupUi(self.MenuWidget)
        self.MenuWidget.show()

    def joinButtonAction(self):
        self.MenuWidget = QtWidgets.QWidget()
        self.ui = client.JoinMenu_Ui()
        self.ui.setupUi(self.MenuWidget)
        self.MenuWidget.show()

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CreateButton.setText(_translate("Dialog", "Create"))
        self.JoinButton.setText(_translate("Dialog", "Join"))

if(__name__ == "__main__"):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuWidget = QtWidgets.QWidget()
    ui = startMenu_Ui()
    ui.setupUi(MenuWidget)
    MenuWidget.show()
    sys.exit(app.exec_())