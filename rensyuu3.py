# 練習問題3
# アパレルのネット通販のアプリで商品クラスを作るケース

class Syohin:
    def __init__(self, id, name, price, purchase_price):
        self.id = id
        self.name = name
        self.price = price
        self.purchase_price = purchase_price
    
    def genkaritst(self):
        return (self.purchase_price / self.price)

# ① オブジェクトを作成して原価率を表示
t_syatu = Syohin("A0001","半袖クールTシャツ",5000,2250)
print(t_syatu.genkaritst())

# ② 販売原価を6000に変更して原価率を表示
t_syatu.price = 6000
print(t_syatu.genkaritst())


