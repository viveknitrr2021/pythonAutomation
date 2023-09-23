from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

# slot connected to a signal(clicked) on btn
def make_sentence():
    input_text = text.text()
    output_label.setText(input_text.capitalize())

app = QApplication([])
window = QWidget()
window.setWindowTitle("GUI")

# widgets can be added to a layout
# And again this layout must be connected to our window in order to work
# QH for horizontal
layout = QVBoxLayout()
text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Make")
layout.addWidget(btn)
# btn connected to slot(a function or procedure performing something) on clicked signal
btn.clicked.connect(make_sentence)

output_label = QLabel("Default Value")
layout.addWidget(output_label)



# Activate Show and then execute the app
window.setLayout(layout)
window.show()
app.exec()