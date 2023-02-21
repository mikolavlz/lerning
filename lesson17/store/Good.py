class Good:
    def __init__(self,id,title,price,category,quantity):
        self.id = id
        self.title = title
        self.price = price
        self.category = category
        self.quantity = quantity
    def __str__(self):
        return f"id:{self.id}, title:{self.title}," \
               f"price:{self.price},category: {self.category.title}"