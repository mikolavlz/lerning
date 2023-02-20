class Good:
    def __init__(self,id,title,price,category):
        self.id = id
        self.title = title
        self.price = price
        self.category = category
    def __str__(self):
        return f"id:{self.id}, title:{self.title}," \
               f"price:{self.price},category: {self.category.title}"