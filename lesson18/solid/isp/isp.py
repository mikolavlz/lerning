from abc import ABC , abstractmethod
class Employee(ABC):
    @abstractmethod
    def get_work_info(self):
        pass
class Person(ABC):
    def get_private_info(self):
        pass

class SenoirDeveloper(Employee,Person):
    def get_work_info(self):
        print("Обязаности работника")
    def get_private_info(self):
        print("Личная инфа о ведущем")
class JuniorDeveloper(Employee):
    def get_work_info(self):
        print("Обязаности работника")


junior = JuniorDeveloper()
junior.get_private_info()
