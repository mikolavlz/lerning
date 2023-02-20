from Developer import Programmer
from Economist import Economist
from Manager import Manager

programmer = Programmer("Junior разработчик")
economist = Economist("Главный экономист")
director = Manager("Управляющий")

men = [programmer,economist,director]
for man in men:
    man.calc_salary()
