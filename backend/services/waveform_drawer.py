import matplotlib.pyplot as plt
import numpy as np


def waveform_drawer(sound, average_amplitude, amplitude_peak_list, syllable_list):
    # 音声のチャンネル数を取得
    channels = sound.channels

    # channelsの検出
    sig = np.array(sound.get_array_of_samples())[::channels]
    dt = 1.0 / sound.frame_rate  # サンプリング時間

    # 時間アレイを作る
    tms = 0.0  # サンプル開始時間を0にセット
    tme = sound.duration_seconds  # サンプル終了時刻
    tm = np.linspace(tms, tme, len(sig), endpoint=False)  # 時間ndarrayを作成

    # DFT
    N = len(sig)
    X = np.fft.fft(sig)
    f = np.fft.fftfreq(N, dt)  # Xのindexに対応する周波数のndarrayを取得

    # データをプロット
    fig, (ax01, ax02) = plt.subplots(nrows=2, figsize=(6, 8))
    plt.subplots_adjust(wspace=0.0, hspace=0.6)

    ax01.set_xlim(tms, tme)
    ax01.set_xlabel("time (s)")
    ax01.set_ylabel("x")
    ax01.plot(tm, sig)  # 入力信号

    ax02.set_xlim(0, 2000)
    ax02.set_xlabel("frequency (Hz)")
    ax02.set_ylabel("|X|/N")
    ax02.plot(f[0 : N // 2], np.abs(X[0 : N // 2]) / N)  # 振幅スペクトル

    # 平均振幅を赤い線で表示
    ax01.axhline(
        y=average_amplitude, color="red", linestyle="--", label="average Amplitude"
    )
    ax01.axhline(y=-average_amplitude, color="red", linestyle="--")
    ax01.legend()

    # ピークを小さな青い点で表示
    # for peak in amplitude_peak_list:
    #    ax01.plot(tm[peak], sig[peak], "bo", markersize=1)

    # sybllable_listを緑の点で表示
    # for syllable in syllable_list:
    #    ax01.plot(tm[syllable], sig[syllable], "go", markersize=2)

    # plt.show()
