from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5 import uic
import res, time, os

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi("camera.ui", self)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.showCamera()
        self.verticalLayout.addWidget(self.finder)
        self.verticalLayout.addWidget(self.btnCamera)
        self.btnCamera.clicked.connect(self.savePictures)

    def showCamera(self):
        self.finder = QCameraViewfinder()
        self.finder.show()
        self.camera = QCamera()
        self.camera.setViewfinder(self.finder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        # self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
        self.camera.start()

        self.capture = QCameraImageCapture(self.camera)
        # self.capture.error.connect(lambda i, e, s: self.alert(s))
        self.capture.imageCaptured.connect(lambda d, i: self.status.showMessage("Image %04d captured" % self.save_seq))

        self.save_seq = 0

    def savePictures(self):
        timestamp = time.strftime("%b-%Y-%H_%M_%S")
        self.capture.capture(os.path.join("d:\\", "%s-%s.jpg" % (
            self.save_seq,
            timestamp
        )))
        self.save_seq += 1




if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()