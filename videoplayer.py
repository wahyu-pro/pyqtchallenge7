from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.resize(600,400)
        self.mainUI()
        self.setCentralWidget(self.widget)

    def mainUI(self):
        self.toolbar = QToolBar()
        self.openTool = QAction("open", self)
        self.toolbar.addAction(self.openTool)
        self.addToolBar(self.toolbar)
        self.openTool.triggered.connect(self.openDialog)
        self.player = QMediaPlayer()
        self.player.setVolume(70)
        self.video = QVideoWidget()
        self.player.setVideoOutput(self.video)
        self.btnPlay = QPushButton("play")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.video)
        self.layout.addWidget(self.btnPlay)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.btnPlay.clicked.connect(self.pause)

    def openDialog(self):
        self.dialog = QFileDialog.getOpenFileName(self, "open Video", "c:\\", 'files(*.mp4)')
        if self.dialog[0] != '':
            self.player.setMedia(QMediaContent(QUrl(self.dialog[0])))
            self.player.play()

    def pause(self):
        pass






if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()