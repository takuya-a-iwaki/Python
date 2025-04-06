from jiwer import wer

# 正解トランスクリプト
reference = "むかし、むかし、ある所におじいさんとおばあさんが住んでいました。おじいさんは山へしば刈りに、おばあさんは川へ洗濯に行きました。"

# 音声認識結果
hypothesis = "むかあしむかしあるところにおじいさんとおばあさんがすんでいましたおじいさんは山へしばかりに おばあさんはかわえ選択に行きました"

# WERの計算
error_rate = wer(reference, hypothesis)
print(f"Word Error Rate: {error_rate}")