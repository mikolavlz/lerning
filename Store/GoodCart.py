from  good import  Good
class Good :
    def __init__(self,id,title,price,quantity):
        super().__init__(self,id,title,price,quantity)

    def __str__(self):
        return f"id:{self.id,}, title: {self.title}, price: {self.price}, cqtegory: { self.category.title}"\
    def __str__(self):
