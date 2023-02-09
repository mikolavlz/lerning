class Test:
    def __init__(self,name):
        self.name = name
    def f(self):
        print(111)

obj = Test("demo")
delattr(obj,"demo")
print(obj.name)