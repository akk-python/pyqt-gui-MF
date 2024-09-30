#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QPushButton

# One and only one QApplication isntance per application
app = QApplication(sys.argv)

# Create a QT Widget, which will be our window
window = QPushButton("Push Me")
window.show()

# start the event loop
app.exec()
