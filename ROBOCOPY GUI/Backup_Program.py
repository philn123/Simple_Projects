#Phillip Nguyen
import sys
import os
import subprocess
from PyQt5 import QtGui
from PyQt5.QtGui import QPalette, QMovie, QPainter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

"""
PURPOSE:
This program allows the user to select a source and
a destination, and the files and subfolders of the source
are copied to the destination file, ignoring the files that
belong in both

RESOURCES:
https://stackoverflow.com/questions/41709464/python-pyqt-add-background-gif
https://build-system.fman.io/pyqt5-tutorial
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy
"""
class App(QWidget):
    #variables to store folders to backup
    source_folder = None
    destination_folder = None

    def __init__(self):
        super().__init__()
        self.title = 'ROBOCOPY Backup GUI'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 500
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.movie = QMovie('cool.gif')
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

        #Colors
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.darkCyan)
        palette.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(palette)


        #buttons
        source_button = QPushButton('Source Folder', self)
        destination_button = QPushButton('Destination Folder', self)
        source_button.move(20, 20)
        destination_button.move(140, 20)
        copy_button = QPushButton('Start Copying', self)
        copy_button.move(260, 20)
        done_button = QPushButton('Click to Close', self)
        done_button.move(380, 20)

        source_button.resize(100,40)
        destination_button.resize(100,40)
        copy_button.resize(100,40)
        done_button.resize(100,40)

        #clicked buttons
        source_button.clicked.connect(self.select_source_folder)
        destination_button.clicked.connect(self.select_destination_folder)
        copy_button.clicked.connect(self.copying)
        done_button.clicked.connect(self.done)

        self.show()

    def select_source_folder(self):
        App.source_folder = QFileDialog.getExistingDirectory(self, 'SELECT DIRECTORY').strip()

    def select_destination_folder(self):
        App.destination_folder = QFileDialog.getExistingDirectory(self, 'SELECT DIRECTORY').strip()

    def copying(self):
        subprocess.run(["robocopy", App.source_folder, App.destination_folder, "/S"])

    def done(self):
        sys.exit(1)

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

