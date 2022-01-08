import sys
import os
from pydub import AudioSegment
from PyQt6 import QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from plot_creator import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(1440, 730)
        self.setWindowIcon(QIcon("icon.png"))

        self.label_back = QLabel(self)
        self.label_back.setGeometry(1440, 730, 1440, 730)
        self.label_back.move(0, 0)
        self.label_back.setStyleSheet("QLabel { \n"
                                      "color: white;\n"
                                      "background-color: #6c0503;\n"
                                      "border: 1px solid #000000;\n"
                                      "border-radius: 0;\n"
                                      "}\n"
                                      "\n")

        self.choose_file_button = QPushButton('Choose file', self)
        self.choose_file_button.setGeometry(80, 50, 80, 50)
        self.choose_file_button.move(680, 650)
        self.choose_file_button.clicked.connect(self.choose_file)
        self.choose_file_button.setStyleSheet("QPushButton {\n"
                                              "color: white;\n"
                                              "background-color: #828c84;\n"
                                              "border: 1px solid #000000;\n"
                                              "border-radius: 0;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "background-color: #d02a2a;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    border: 2px solid #ffffff;\n"
                                              "}")

        self.label_waveplot = QLabel("waveplot", self)
        self.label_waveplot.setGeometry(470, 200, 470, 200)
        self.label_waveplot.move(10, 10)
        self.label_waveplot.setStyleSheet("QLabel { \n"
                                          "color: white;\n"
                                          "background-color: #1e2625;\n"
                                          "border: 1px solid #000000;\n"
                                          "}\n"
                                          "\n"
                                          "QLabel:hover {\n"
                                          "border: 2px solid #ffffff;\n"
                                          "}")

        self.label_amplitude_envelope = QLabel("amplitude_envelope", self)
        self.label_amplitude_envelope.setGeometry(470, 200, 470, 200)
        self.label_amplitude_envelope.move(485, 10)
        self.label_amplitude_envelope.setStyleSheet("QLabel { \n"
                                                    "color: white;\n"
                                                    "background-color: #1e2625;\n"
                                                    "border: 1px solid #000000;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QLabel:hover {\n"
                                                    "border: 2px solid #ffffff;\n"
                                                    "}")

        self.label_spectrograms = QLabel("RMSE", self)
        self.label_spectrograms.setGeometry(470, 200, 470, 200)
        self.label_spectrograms.move(960, 10)
        self.label_spectrograms.setStyleSheet("QLabel { \n"
                                      "color: white;\n"
                                      "background-color: #1e2625;\n"
                                      "border: 1px solid #000000;\n"
                                      "}\n"
                                      "\n"
                                      "QLabel:hover {\n"
                                      "border: 2px solid #ffffff;\n"
                                      "}")

        self.label_centroids = QLabel("centroid", self)
        self.label_centroids.setGeometry(470, 200, 470, 200)
        self.label_centroids.move(10, 215)
        self.label_centroids.setStyleSheet("QLabel { \n"
                                           "color: white;\n"
                                           "background-color: #1e2625;\n"
                                           "border: 1px solid #000000;\n"
                                           "}\n"
                                           "\n"
                                           "QLabel:hover {\n"
                                           "border: 2px solid #ffffff;\n"
                                           "}")

        self.label_spectral_bandwidth = QLabel("spectral_bandwidth", self)
        self.label_spectral_bandwidth.setGeometry(470, 200, 470, 200)
        self.label_spectral_bandwidth.move(485, 215)
        self.label_spectral_bandwidth.setStyleSheet("QLabel { \n"
                                                    "color: white;\n"
                                                    "background-color: #1e2625;\n"
                                                    "border: 1px solid #000000;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QLabel:hover {\n"
                                                    "border: 2px solid #ffffff;\n"
                                                    "}")

        self.label_spectral_rolloff = QLabel("spectral_rolloff", self)
        self.label_spectral_rolloff.setGeometry(470, 200, 470, 200)
        self.label_spectral_rolloff.move(960, 215)
        self.label_spectral_rolloff.setStyleSheet("QLabel { \n"
                                                  "color: white;\n"
                                                  "background-color: #1e2625;\n"
                                                  "border: 1px solid #000000;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel:hover {\n"
                                                  "border: 2px solid #ffffff;\n"
                                                  "}")

        self.label_zero_crossing_rate = QLabel("zero_crossing_rate", self)
        self.label_zero_crossing_rate.setGeometry(470, 200, 470, 200)
        self.label_zero_crossing_rate.move(10, 420)
        self.label_zero_crossing_rate.setStyleSheet("QLabel { \n"
                                                    "color: white;\n"
                                                    "background-color: #1e2625;\n"
                                                    "border: 1px solid #000000;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QLabel:hover {\n"
                                                    "border: 2px solid #ffffff;\n"
                                                    "}")

        self.label_MFCCs = QLabel("MFCCs", self)
        self.label_MFCCs.setGeometry(470, 200, 470, 200)
        self.label_MFCCs.move(485, 420)
        self.label_MFCCs.setStyleSheet("QLabel { \n"
                                       "color: white;\n"
                                       "background-color: #1e2625;\n"
                                       "border: 1px solid #000000;\n"
                                       "}\n"
                                       "\n"
                                       "QLabel:hover {\n"
                                       "border: 2px solid #ffffff;\n"
                                       "}")

        self.label_chroma_vector = QLabel("chroma_vector", self)
        self.label_chroma_vector.setGeometry(470, 200, 470, 200)
        self.label_chroma_vector.move(960, 420)
        self.label_chroma_vector.setStyleSheet("QLabel { \n"
                                             "color: white;\n"
                                             "background-color: #1e2625;\n"
                                             "border: 1px solid #000000;\n"
                                             "}\n"
                                             "\n"
                                             "QLabel:hover {\n"
                                             "border: 2px solid #ffffff;\n"
                                             "}")

    def choose_file(self):
        open_file = QFileDialog.getOpenFileName(self, 'Open File', 'E:/Kyrsach', 'MP3 File (*.mp3);;WAV File (*.wav)')

        def get_file_name(file_path):
            way_parts = file_path.split('/')
            filename = way_parts[len(way_parts) - 1]
            return filename

        if open_file[1] == 'MP3 File (*.mp3)':
            Src = f'{get_file_name(open_file[0])}'
            export_way = f'processing_results/soundfiles/{get_file_name(open_file[0])[:-3].replace(".", "")}.wav'
            sound =AudioSegment.from_mp3(Src)
            sound.export(export_way, format='wav')
            print(
                'Используется формат mp3. '
                '\nЕсли при обработке произошла ошибка, выберите копию файла в формате wav\n'
                'по адресу E:/Kyrsach/processing_results/soundfiles/(имя файла)')

        make_waveplot(open_file[0])
        self.label_waveplot.setPixmap(QtGui.QPixmap(
            f'processing_results/plots/waveplots/{get_file_name(open_file[0])[:-3].replace(".", "")}.png'))

        make_amplitude_envelope(open_file[0])
        self.label_amplitude_envelope.setPixmap(QtGui.QPixmap(
            f'processing_results/plots/amplitude_envelope/{get_file_name(open_file[0])[:-3].replace(".", "")}.png'))

        #make_RMSE(open_file[0])
        make_spectrogram(open_file[0])
        self.label_spectrograms.setPixmap(QtGui.QPixmap(
            f'processing_results/plots/spectrograms/{get_file_name(open_file[0])[:-3].replace(".", "")}.png'))

        make_centroid(open_file[0])
        self.label_centroids.setPixmap(QtGui.QPixmap(
            f'processing_results/plots/centroids/{get_file_name(open_file[0])[:-3].replace(".", "")}.png'))

        make_spectral_bandwidth(open_file[0])
        self.label_spectral_bandwidth.setPixmap(QtGui.QPixmap(
            f'processing_results/plots/spectral_bandwidth/{get_file_name(open_file[0])[:-3].replace(".", "")}.png'))

        make_spectral_rolloff(open_file[0])
        self.label_spectral_rolloff.setPixmap(QtGui.QPixmap(
            f'processing_results/plots/spectral_rolloff/{get_file_name(open_file[0])[:-3].replace(".", "")}.png'))

        make_zero_crossing_rate(open_file[0])
        self.label_zero_crossing_rate.setPixmap(QtGui.QPixmap(
            f'processing_results/plots/zero-crossing_rate/{get_file_name(open_file[0])[:-3].replace(".", "")}.png'))

        make_MFCC(open_file[0])
        self.label_MFCCs.setPixmap(QtGui.QPixmap(
            f'processing_results/plots/MFCCs/{get_file_name(open_file[0])[:-3].replace(".", "")}.png'))

        make_chroma_vector(open_file[0])
        self.label_chroma_vector.setPixmap(QtGui.QPixmap(
            f'processing_results/plots/chroma_vector/{get_file_name(open_file[0])[:-3].replace(".", "")}.png'))



def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def build(root, data):
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            create_folder(path)
            build(path, d[1])


if __name__ == "__main__":
    path = r'E:\Kyrsach'
    work_folder = r'processing_results'
    folders = \
    [ ['plots', [
          ['spectrograms', [] ],
          ['waveplots', [] ],
          ['amplitude_envelope', [] ],
          ['RMSE', []],
          ['centroids', [] ],
          ['spectral_bandwidth', [] ],
          ['spectral_rolloff', [] ],
          ['zero-crossing_rate', [] ],
          ['MFCCs', [] ],
          ['chroma_vector', [] ],
          ] ],
      ['soundfiles', [
          ['MFCCs_ecv', [] ],
          ] ],
    ]

    full_path = os.path.join(path, work_folder)
    create_folder(full_path)

    build(full_path, folders)


app_dial = QApplication(sys.argv)
dlgMain = DlgMain()
dlgMain.show()
sys.exit(app_dial.exec())