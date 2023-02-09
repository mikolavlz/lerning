class Test:
    x = 0


    def f(self):
        Test.x += 1
        print(Test.x)


obj1 = Test()
obj2 = Test()

obj1.f()
obj1.f()

obj2.f()
obj2.f()