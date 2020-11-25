import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class gui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.deactivateButton.setEnabled(False)
        self.emergencyStopButton.setEnabled(False)
        self.stateLabel.setText("DESACTIVADO")
        self.activateButton.clicked.connect(self.activate)
        self.deactivateButton.clicked.connect(self.deactivate)
        self.emergencyStopButton.clicked.connect(self.emergencyDeactivate)

    def activate(self):
        self.activateButton.setEnabled(False)
        self.emergencyStopButton.setEnabled(True)
        self.deactivateButton.setEnabled(True)
        self.stateLabel.setText("ACTIVADO")

    def deactivate(self):
        self.activateButton.setEnabled(True)
        self.emergencyStopButton.setEnabled(False)
        self.deactivateButton.setEnabled(False)
        self.stateLabel.setText("DESACTIVADO")

    def emergencyDeactivate(self):
        self.activateButton.setEnabled(False)
        self.deactivateButton.setEnabled(False)
        self.stateLabel.setText("¡DESACTIVADO DE EMERGENCIA!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = gui()
    GUI.show()
    sys.exit(app.exec_())

