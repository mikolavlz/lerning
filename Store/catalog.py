class Catalog:
    def __init__(self,goods):
        self.goods = goods
    def show_catalog(self):
        for i,item in enumerate(self.goods):
            print(f"{i+1}Товар {item.title} стоит {item.price}"
                  f"товар относиться к категории {item.category.title}")
            