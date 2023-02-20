from GoodCart import GoodCart


class Cart:
    def __init__(self,goods_cart):
        self.goods_cart = goods_cart #корзина покупок

    def show_cart(self):
        print("\nКорзина покупок\n")
        for i,item in enumerate(self.goods_cart):
            print(f"{i + 1}) {item.title} стоит {item.price},"
                  f" общая стоимость товара "
                  f"с учетом количества: {item.price * item.quantity}")

#В методе принимаем товар из каталога для покупки
#good - это товар каталога
    def add_good(self,good,user_id):
        if(len(self.goods_cart) == 0):#если в корзине нет
            self.add_good_first_time(good,user_id)
        else: #если в корзине товары уже были
            is_find = False#пусть товар добавляется впервые
            for item in self.goods_cart: #цикл по существующим в корзине товарам
                if item.id == good.id:#товар найден
                    item.quantity += 1
                    is_find = True
                    break
            if not is_find: #товар добавляется впервые
                self.add_good_first_time(good,user_id)

    def add_good_first_time(self,good,user_id):
        cart_item = GoodCart(good.id, good.title, good.price, good.category, 1,user_id)
        self.goods_cart.append(cart_item)













