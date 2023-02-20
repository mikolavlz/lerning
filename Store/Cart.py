class Cart:
    def __init__(self, goods_cart):
        self.goods = goods_cart

    def show_cart(self):
        print("Корзина покупок")
        for i, item in enumerate(self.goods_cart):
            print(f"{i + 1}Товар {item.title} стоит {item.price}"
                  f"Общая стоимость с учетом количества{item.price * item.quantity}")

    def add_good(self,good):
        if(len(self.goods_cart) == 0 ):
            cart_item