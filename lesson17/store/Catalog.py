class Catalog:
    def __init__(self,goods):
        self.goods = goods

    def show_catalog(self):
        for i,item in enumerate(self.goods):
            print(f"{i + 1}) {item.title} стоит {item.price},"
                  f" товар относится к категории {item.category.title},id = {item.id}")

    def add_good_to_cart(self,cart,good,user_id):
        cart.add_good(good,user_id)

    def get_good_by_id(self,id):
        for item in self.goods:
            if item.id == id:
                return item
        return None
