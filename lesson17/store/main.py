from Category import Category
from Good import Good
from Catalog import Catalog
from store.Cart import Cart
from store.Users import Users

cat1 = Category(1,"Европейские автомобили")
cat2 = Category(2,"Японские автомобили")

good1 = Good(1,"Skoda",1000,cat1)
good2 = Good(2,"Audi",1000,cat1)
good3 = Good(3,"BMW",1000,cat1)
good4 = Good(4,"Lexus",1000,cat2)
good5 = Good(5,"Toyota",1000,cat2)

goods = [good1,good2,good3,good4,good5]

catalog = Catalog(goods)

users = Users() #получаем объект с юзером, который авторизовался в системе
user = users.start()
if user: #если юзер найден, отображаем товары каталога
    cart = Cart([])
    catalog.show_catalog()
    good_id = int(input("Введите id товара, который желаете добавить в корзину "
                        "или введите -1 для перехода в корзину покупок"))
    while True:
        if good_id > 0:
            good = catalog.get_good_by_id(good_id)
            if good:
                cart.add_good(good,user.id)
        else:
            cart.show_cart()
            break