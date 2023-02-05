class univer:
    def __init__(self,title,student):
        self.title = title
        self.student = student

    def show_info(self):
        print(f"Название офиса: {self.title}\nВ универе учатся следующие студенты:")
        i = 1
        for man in self.student:
            print(f"{i}){man.get_info()}")
            i += 1
        excellent_student =  self.get_excellent_student()
        print("Список хорошистов")
        for l in range(len(excellent_student)):
            print(f"Студент {excellent_student[l].fio} имеет балл более 4.5 = {excellent_student[l].ball}")
    def get_excellent_student(self):
        excellent_student = []
        print("\n")
        for i in range(1, len(self.student)):
            if self.student[i].ball >= 4.5:
                excellent_student.append(self.student[i])
        return excellent_student
class student:
    def __init__(self,id,fio,ball):
        self.fio = fio
        self.ball = ball

    def get_info(self):#self ссылается на объект, который вызывает наш метод
        return f"Студент {self.fio} имеет средний балл {self.ball}"


man1 = student(1,"Иванов",3.5)
man2 = student(2,"Петров",4.7)
man3 = student(3,"Сидоров",4.6)
man4 = student(4,"Егоров",2.6)
man5 = student(5,"Петросян",5)
man6 = student(6,"Курянов",4.8)
man7 = student(7,"Жлобов",2.7)
man8 = student(8,"Котов",3.7)


men = [man1,man2,man3,man4,man5,man6,man7,man8]
university = univer("МГУ",men)
university.show_info() #выведем всю информацию об студентах

