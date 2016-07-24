import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class Prost(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.x = 0
        self.y = 0
        self.prost = []
        self.bool = True
        self.setGeometry(0, 0, 300, 300)
        self.show()

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.red)
        for e in self.prost:
            qp.drawPoint(e[0], e[1])
        qp.end()

    def keyPressEvent(self, QKeyEvent):
        print(self)
        a = self.size()
        print(a)
        self.prost.append((self.x, self.y))
        self.x += 1
        self.y += 1
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Prost()
    app.exec_()