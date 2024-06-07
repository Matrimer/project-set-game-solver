from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

DIALOGWIDTH = 900
DIALOGHEIGHT = 200


class DuplicateDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Duplicate card")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("You are adding a duplicate")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)