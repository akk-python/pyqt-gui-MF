#!/usr/bin/env python3
from PyQt6.QtWidgets import QApplication, QWidget
import sys

# One and only one QApplication isntance per application
app = QApplication(sys.argv)

# Create a QT Widget, which will be our window
window = QWidget()
window.show()

# start the event loop
app.exec()
