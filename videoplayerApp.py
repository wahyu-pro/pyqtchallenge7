from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5 import uic
from PyQt5.QtGui import QFont, QIcon
import res

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi("videoplayer.ui", self)
        self.setWindowTitle("Video Player")
        self.setWindowIcon(QIcon("icon/icon.png"))
        # self.resize(600,400)
        self.mainUI()

    def mainUI(self):
        self.toolbar = QToolBar()
        self.openTool = QAction(QIcon("icon/openfile.png"), "Open", self)
        self.toolbar.addAction(self.openTool)
        self.addToolBar(self.toolbar)
        self.openTool.triggered.connect(self.openDialog)


        self.player = QMediaPlayer()
        self.video = QVideoWidget()
        self.player.setVideoOutput(self.video)
        self.player.stateChanged.connect(self.mediaStateChanged)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)

        self.statusBar = QStatusBar()
        self.statusBar.setFont(QFont("Arial", 7))
        self.statusBar.setFixedHeight(30)

        self.verticalLayout.addWidget(self.video)
        self.verticalLayout.addWidget(self.statusBar)
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.durationSlider.setRange(0, 0)
        self.durationSlider.sliderMoved.connect(self.setPosition)

        self.volumeSlider.valueChanged.connect(self.player.setVolume)

    def openDialog(self):
        self.dialog = QFileDialog.getOpenFileName(self, "open Video", "c:\\", 'files(*.mp4 *.mkv *.flv *.avi)')
        if self.dialog[0] != '':
            self.player.setMedia(QMediaContent(QUrl(self.dialog[0])))
            self.statusBar.showMessage(self.dialog[0])
            self.playButton.setEnabled(True)
            self.play()

    def play(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def setPosition(self, position):
        self.player.setPosition(position)

    def mediaStateChanged(self, state):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.durationSlider.setValue(position)

    def durationChanged(self, duration):
        self.durationSlider.setRange(0, duration)







if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()