from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
    url = f'https://x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[0:-4])
    return rate


# slot connected to a signal(clicked) on btn
def convert():
    input_text = float(text.text())
    in_cur = in_combo.currentText()
    tar_cur = tar_combo.currentText()
    rate = get_currency(in_cur, tar_cur)
    print(rate)
    output_text = input_text*rate
    print(output_text)
    output_label.setText(str(output_text))


app = QApplication([])
window = QWidget()
window.setWindowTitle("GUI")

# widgets can be added to a layout
# And again this layout must be connected to our window in order to work
# QH for horizontal
layout = QVBoxLayout()

in_combo = QComboBox()
currencies = ['USD', 'INR', 'EUR']
in_combo.addItems(currencies)
layout.addWidget(in_combo)

tar_combo = QComboBox()
tar_combo.addItems(currencies)
layout.addWidget(tar_combo)

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Convert")
layout.addWidget(btn)
# btn connected to slot(a function or procedure performing something) on clicked signal
btn.clicked.connect(convert)

output_label = QLabel("Currency Converter")
layout.addWidget(output_label)

# Activate Show and then execute the app
window.setLayout(layout)
window.show()
app.exec()
