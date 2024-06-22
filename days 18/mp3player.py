import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent,QMediaPlayer

class MP3PLAYER (QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.playlist = []
        self.position = 0
        self.index = ""

    def init_ui(self):
        vb = QVBoxLayout()
        self.setLayout(vb)
        vb.setAlignment(Qt.AlignCenter)

        hb = QHBoxLayout()
        vb.addLayout(hb)
        font = QFont("calibri",14)
        self.songlist = QListWidget()
        hb.addWidget(self.songlist)

        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)
        vb.addWidget(self.slider)
        

        hb2 = QHBoxLayout()
        vb.addLayout(hb2)

        self.player = QMediaPlayer()
        self.speaker = QPushButton()
        self.speaker.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        hb2.addWidget(self.speaker)
        self.slider_vl = QSlider(Qt.Horizontal)
        hb2.addWidget(self.slider_vl)
        self.label_vl = QLabel()
        self.label_vl.setFont(QFont("Helvetica",10))
        self.label_vl.setMinimumWidth(40)
        hb2.addWidget(self.label_vl)
        self.slider_vl.setRange(0,100)
        volume = self.player.volume()
        self.slider_vl.setValue (volume)

        hb3 = QHBoxLayout()
        vb.addLayout(hb3)
        self.skipbackward = QPushButton()
        self.skipbackward.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        hb3.addWidget(self.skipbackward)
        self.backward = QPushButton()
        self.backward.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward))
        self.backward.setFont(font)
        hb3.addWidget(self.backward)
        self.playbttn = QPushButton()
        self.playbttn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playbttn.setFont(font)
        hb3.addWidget(self.playbttn)
        self.pause = QPushButton()
        self.pause.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.pause.setFont(font)
        hb3.addWidget(self.pause)
        self.next = QPushButton()
        self.next.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
        self.next.setFont(font)
        hb3.addWidget(self.next)
        self.skipforward = QPushButton()
        self.skipforward.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))
        hb3.addWidget(self.skipforward)


        self.openfileleaction = QPushButton()
        self.openfileleaction.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))
        self.openfileleaction.setFont(font)
        hb3.addWidget(self.openfileleaction)


        self.openfileleaction.clicked.connect(self.open_mp3_file)
        self.playbttn.clicked.connect(self.play_mp3)
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.backward.clicked.connect(self.move_backward)
        self.next.clicked.connect(self.move_forward)
        self.skipbackward.clicked.connect(self.skip_backward)
        self.skipforward.clicked.connect(self.skip_forward)
        self.slider_vl.valueChanged.connect(self.set_volume)
        self.pause.clicked.connect(self.mp3_pause)

    def open_mp3_file(self):
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        names = file_name.getOpenFileName(self,"Open Files", os.getenv("HOME"))
        self.song = names[0]
        self.songlist.addItem(self.song)
    
    def play_mp3(self):
        current_item = self.songlist.currentItem()
        if current_item is None:
            QMessageBox.warning(self, "Error", "PILIH LAGU TERLEBIH DULU")
            return

        path = current_item.text()
        self.player.play()
        url = QUrl.fromLocalFile(path)
        Content = QMediaContent(url)
        self.player.setMedia(Content)
        self.index = self.songlist.currentRow().__index__()
        self.player.setPosition(self.position)
        self.playlist.append(path)
        if len(self.playlist) > 2:
            self.playlist.pop(0)
        if current_item.text() != self.playlist[0]:
            self.position = 0
            self.player.setPosition(self.position)
        self.player.play()

        
    def mp3_pause(self):
        self.player.pause()

    def skip_backward(self):
        try:
            self.songlist.setCurrentRow(self.index - 1)
            self.play_mp3()
        except:
            pass
    
    def skip_forward(self):
        try:
            self.songlist.setCurrentRow(self.index + 1)
            self.play_mp3()
        except:
            pass

    def set_position(self,position):
        self.player.setPosition(position)

    def position_changed(self,position):
        self.slider.setValue(position)
        duration = self.player.duration()
        value = self.slider.value()
        value == duration 
    
    def duration_changed(self,duration):
        self.slider.setRange(0,duration)

    def move_forward(self):
        self.player.setPosition(int(self.player.position())+2000)

    def move_backward(self):
        self.player.setPosition(int(self.player.position())-2000)

    def set_volume(self):
        volume = self.slider_vl.value()
        self.player.setVolume(volume)
        self.label_vl.setText(str(volume)+"%")
def main():
    app = QApplication(sys.argv)
    gui = MP3PLAYER()
    gui.setWindowTitle("MP3PLAYER")
    gui.setWindowIcon(QIcon("mp3player.png"))
    gui.setGeometry(600,200,600,700)
    gui.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
