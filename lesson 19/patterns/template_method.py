class TestBase:
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    def step_one(self):
        raise NotImplementedError

    def step_two(self):
        raise NotImplementedError

    def step_three(self):
        raise NotImplementedError
class Child(TestBase):
    def step_one(self):
        print(1)

    def step_two(self):
        print(2)