import whisper

# model = whisper.load_model("turbo")
model = whisper.load_model("turbo")
result = model.transcribe("5momotarou.mp3", language="ja", task="transcribe", verbose=False, word_timestamps=True)

# with open("base3.txt","w") as f:
#     f.write(result["segments"])

with open("turbo.txt","w",encoding="utf-8") as f:
    # 変換結果の表示
    for segment in result["segments"]:
        start = segment['start']
        end = segment['end']
        text = segment['text']
        
        # 秒を分:秒形式に変換
        start_min = int(start // 60)
        start_sec = start % 60
        end_min = int(end // 60)
        end_sec = end % 60
        
        # 分:秒形式で出力
        f.writelines(f"[{start_min:02}:{start_sec:06.3f} --> {end_min:02}:{end_sec:06.3f}] {text}\n")