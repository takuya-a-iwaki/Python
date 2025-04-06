from jiwer import wer

# 正解トランスクリプト
with open("transcript.txt","r", encoding="UTF-8") as f:
    reference = f.read()    

# 音声認識結果
with open("base.txt","r", encoding="SJIS") as f:
    hypothesis_base = f.read()

with open("turbo.txt","r", encoding="SJIS") as f:
    hypothesis_turbo = f.read()


# WERの計算
error_rate = wer(reference, hypothesis_base)
print(f"Word Error Rate base: {error_rate}")

error_rate = wer(reference, hypothesis_turbo)
print(f"Word Error Rate turbo: {error_rate}")
