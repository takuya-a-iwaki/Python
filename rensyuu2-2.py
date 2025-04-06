# 練習問題2-2
# FizzBuzz問題。 1から100までの数位を出力してください。
# ただし、3の倍数の時は数字の代わりにFizz
# 5の倍数の場合は数字の代わりにBuzz
# 15の倍数の時は数字の代わりにFizzBuzz を表示させてください。

for num in range(1,101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


