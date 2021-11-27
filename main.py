import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen
from PyQt5 import uic
from PyQt5.QtCore import Qt
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("circle.ui", self)
        self.btn.clicked.connect(self.circle)

        self.label = QLabel()
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.btn, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        x, y = [randint(10, 500) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(*[randint(0, 255) for i in range(3)]))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())