def sound_display(sound):
    # 音声の長さ（ミリ秒）
    duration_ms = len(sound)
    print(f"音声の長さ: {duration_ms}ms")

    # チャンネル数
    channels = sound.channels
    print(f"チャンネル数: {channels}")

    # サンプルレート（Hz）
    sample_rate = sound.frame_rate
    print(f"サンプルレート: {sample_rate}Hz")

    # ビット深度
    sample_width = sound.sample_width
    print(f"ビット深度: {sample_width * 8}ビット")
