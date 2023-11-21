import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow



class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setupUi(self)
        self.do_paint = False
        self.button.clicked.connect(self.updating)
    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False
    def updating(self):
        self.do_paint = True
        self.update()
    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))

        for i in range(randint(70, 800)):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            r = randint(0, 150)
            qp.drawEllipse(randint(0, 800), randint(0, 600), r, r)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
