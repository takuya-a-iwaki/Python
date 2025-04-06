import whisper
from jiwer import wer

# model = whisper.load_model("turbo")
model = whisper.load_model("base")
result = model.transcribe("5momotarou.mp3")

with open("large.txt","w") as f:
    f.write(result["text"])

