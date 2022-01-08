import sklearn
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import soundfile

FRAME_SIZE = 64
HOP_LENGTH = 24


def get_file_name(file_path):
    # Из пути получает название файла
    way_parts = file_path.split('/')
    filename = way_parts[len(way_parts)-1]
    return filename


# Нормализация для построения спектрального центроида и спектральной ширины
def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)


def make_waveplot(file_path):
    # Построение волнового сигнала:
    x, sr = librosa.load(get_file_name(file_path))
    # Построение графика сигнала:
    plt.figure(figsize=(5, 2))
    librosa.display.waveplot(x, sr=sr)
    plt.savefig(f'processing_results/plots/waveplots/{get_file_name(file_path)[:-3].replace(".", "")}.png')
    plt.show()


def make_amplitude_envelope(file_path):
    # Построение амплитудного конверта сигнала:
    x, sr = librosa.load(file_path)

    def amplitude_envelope(signal, frame_size, hop_length):
        # Вычислить огибающую амплитуды сигнала с заданным размером кадра и длиной скачка.
        amplitude_envelope = []

        # Рассчитать огибающую амплитуды для каждого фрэйма
        for i in range(0, len(signal), hop_length):
            amplitude_envelope_current_frame = max(signal[i:i + frame_size])
            amplitude_envelope.append(amplitude_envelope_current_frame)

        return np.array(amplitude_envelope)

    signal = amplitude_envelope(x, FRAME_SIZE, HOP_LENGTH)
    frames = range(len(signal))
    t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)

    # Построение графика сигнала:
    plt.figure(figsize=(5, 2))

    librosa.display.waveplot(x, alpha=0.5)
    plt.plot(t, signal, color="r")
    plt.ylim((-1, 1))
    plt.savefig(f'processing_results/plots/amplitude_envelope/{get_file_name(file_path)[:-3].replace(".", "")}.png')
    plt.show()


def make_RMSE(file_path):
    # Построение RMSE сигнала:
    x, sr = librosa.load(file_path)

    rms_signal = librosa.feature.rms(x, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
    frames = range(len(rms_signal))
    t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)

    def rmse(signal, frame_size, hop_length):
        rmse = []

        # Посчимать rmse для каждого фрэйма
        for i in range(0, len(signal), hop_length):
            rmse_current_frame = np.sqrt(sum(signal[i:i + frame_size] ** 2) / frame_size)
            rmse.append(rmse_current_frame)
        return np.array(rmse)

    rmse_signal = rmse(x, FRAME_SIZE, HOP_LENGTH)
    plt.figure(figsize=(5, 2))

    librosa.display.waveplot(x, alpha=0.5)
    plt.plot(t, rms_signal, color="r")
    plt.plot(t, rmse_signal, color="b")
    plt.ylim((-1, 1))
    plt.savefig(f'processing_results/plots/RMSE/{get_file_name(file_path)[:-3].replace(".", "")}.png')
    plt.show()


def make_centroid(file_path):
    # Построение спектрального центроида сигнала:
    x, sr = librosa.load(get_file_name(file_path))
    spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]

    # Вычисление временной переменной для визуализации
    plt.figure(figsize=(5, 2))
    frames = range(len(spectral_centroids))
    t = librosa.frames_to_time(frames)
    # Построение спектрального центроида вместе с формой волны
    librosa.display.waveplot(x, sr=sr, alpha=0.4)
    plt.plot(t, normalize(spectral_centroids), color='r')
    plt.savefig(f'processing_results/plots/centroids/{get_file_name(file_path)[:-3].replace(".", "")}.png')
    plt.show()


def make_spectral_bandwidth(file_path):
    # Построение спектральной ширины сигнала:
    x, sr = librosa.load(get_file_name(file_path))
    spectral_bandwidth = librosa.feature.spectral_centroid(x, sr=sr)[0]

    # Вычисление временной переменной для визуализации
    frames = range(len(spectral_bandwidth))
    t = librosa.frames_to_time(frames)

    spectral_bandwidth_2 = librosa.feature.spectral_bandwidth(x + 0.01, sr=sr)[0]
    spectral_bandwidth_3 = librosa.feature.spectral_bandwidth(x + 0.01, sr=sr, p=3)[0]
    spectral_bandwidth_4 = librosa.feature.spectral_bandwidth(x + 0.01, sr=sr, p=4)[0]
    plt.figure(figsize=(5, 2))
    librosa.display.waveplot(x, sr=sr, alpha=0.4)
    plt.plot(t, normalize(spectral_bandwidth_2), color='r')
    plt.plot(t, normalize(spectral_bandwidth_3), color='g')
    plt.plot(t, normalize(spectral_bandwidth_4), color='b')
    plt.legend(('p = 2', 'p = 3', 'p = 4'))
    plt.savefig(f'processing_results/plots/spectral_bandwidth/{get_file_name(file_path)[:-3].replace(".", "")}.png')
    plt.show()


def make_spectral_rolloff(file_path):
    # Построение спектрального спада сигнала:
    x, sr = librosa.load(get_file_name(file_path))
    spectral_rolloffs = librosa.feature.spectral_centroid(x, sr=sr)[0]

    # Вычисление временной переменной для визуализации
    frames = range(len(spectral_rolloffs))
    t = librosa.frames_to_time(frames)
    spectral_rolloff = librosa.feature.spectral_rolloff(x + 0.01, sr=sr)[0]
    plt.figure(figsize=(5, 2))
    librosa.display.waveplot(x, sr=sr, alpha=0.4)
    plt.plot(t, normalize(spectral_rolloff), color='r')
    plt.savefig(f'processing_results/plots/spectral_rolloff/{get_file_name(file_path)[:-3].replace(".", "")}.png')
    plt.show()


def make_zero_crossing_rate(file_path):
    # Построение вычисление числа пересечений нуля сигнала:
    x, sr = librosa.load(file_path)
    n0 = 9000
    n1 = 9100
    plt.figure(figsize=(5, 2))
    plt.plot(x[n0:n1], color="r")
    plt.grid()
    plt.savefig(f'processing_results/plots/zero-crossing_rate/{get_file_name(file_path)[:-3].replace(".", "")}.png')
    plt.show()


def make_MFCC(file_path):
    # Построение MFCC сигнала:
    x, sr = librosa.load(file_path)
    mfccs = librosa.feature.mfcc(x, sr=sr)

    # Отображение MFCC:
    plt.figure(figsize=(5, 2))
    librosa.display.specshow(mfccs, sr=sr, x_axis='time')
    plt.savefig(f'processing_results/plots/MFCCs/{get_file_name(file_path)[:-3].replace(".", "")}.png')
    plt.show()
    ecv_audiofile = librosa.feature.inverse.mfcc_to_audio(mfccs, n_mels=128, dct_type=2, norm='ortho', ref=1.0, lifter=0)
    soundfile.write(file=f'processing_results/soundfiles/MFCCs_ecv/{get_file_name(file_path)[:-3].replace(".", "")}.wav', data=ecv_audiofile, samplerate=sr)


def make_chroma_vector(file_path):
    # Построение хроматического вектора сигнала:
    x, sr = librosa.load(get_file_name(file_path))
    hop_length = 256
    chromagram = librosa.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
    plt.figure(figsize=(5, 2))
    librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=hop_length, cmap='coolwarm')
    plt.savefig(f'processing_results/plots/chroma_vector/{get_file_name(file_path)[:-3].replace(".", "")}.png')
    plt.show()


def make_spectrogram(file_path):
    # Построение спектрограммы сигнала:
    x, sr = librosa.load(get_file_name(file_path), mono=True)
    x_stft = librosa.stft(x)
    xdb = librosa.amplitude_to_db(abs(x_stft))
    plt.figure(figsize=(5, 2))
    librosa.display.specshow(xdb, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar()
    plt.savefig(f'processing_results/plots/spectrograms/{get_file_name(file_path)[:-3].replace(".", "")}.png')
    plt.show()
