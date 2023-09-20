from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path


def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select files')
    message.setText('\n'.join(filenames))
    print(filenames)


def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText('files destroyed')

app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")
layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy. The Files will be <font color="red">permanently</font> '
                     'deleted')
layout.addWidget(description)

open_ptn = QPushButton('Open Files')
open_ptn.setToolTip('Open Files')
open_ptn.setFixedWidth(100)
layout.addWidget(open_ptn, alignment=Qt.AlignmentFlag.AlignCenter)
open_ptn.clicked.connect(open_files)

destroy_btn = QPushButton('Destroy Files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()
