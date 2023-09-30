import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)

        label = QLabel(self)
        button = QPushButton(self)
        pixmap = QPixmap('cat.jpg')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        
        self.resize(pixmap.width(), pixmap.height())


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())