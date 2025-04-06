# 練習問題2-1
# yearという変数に西暦に数値が代入されています。閏年かどうかを判断して、閏年なら「閏年です」平年なら「平年です」と表示してください。

year = 300

if year % 4 != 0:
    print("平年です")
else:
    if (year % 100 == 0 and year % 400 != 0):
        print("平年です")
        print("yoyo")
    else:
        print("閏年です")



