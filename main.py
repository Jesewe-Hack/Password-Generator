from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from tkinter import messagebox
import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def gen_pass():
	try:
		number = 1
		length = int(form.lineEdit_2.text())
		for n in range(number):
		    password =''
		    for i in range(length):
		        password += random.choice(chars)
		    if length>16:
		    	messagebox.showerror(f"Password Generator", "ERROR: Maximum password length is 16")
		    else:
		    	form.lineEdit.setText(password)
	except Exception as e:
		messagebox.showerror(f"Password Generator", f"FATAL ERROR!")

Form, Window = uic.loadUiType("gui.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.lineEdit.setPlaceholderText('Click Generate')
form.pushButton.clicked.connect(gen_pass)

app.exec()