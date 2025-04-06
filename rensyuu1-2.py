# 練習問題2
# 平均点を求めてください。「○点」という文字で出力してください。

scores = {"数学":82, "国語":74, "英語":60, "理科":92, "社会":70}

avg_score = sum(list(scores.values())) / len(scores)

print(f"{avg_score}点")
