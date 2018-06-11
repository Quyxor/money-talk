import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, QGridLayout, QTableWidget, QTableWidgetItem,
                             QWidget, QMessageBox, QApplication)
from PyQt5.QtGui import QIcon


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Money talk')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Сообщение', 'Вы точно хотите выйти?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# class Table(QTableWidget):
#     def __init__(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Window()
    app.exit(app.exec_())