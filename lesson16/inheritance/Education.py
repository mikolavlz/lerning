class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя:{self.name}, фамилия: {self.surname}"

class Teacher(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def teach(self,subject,*students):
        for student in students:
            student.study(subject)

class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.subjects = [] #знания(предметы)
    def study(self,subject):
        print("Студент изучил ",subject)
        self.subjects = subject
    def show_subjects(self):
        print(self.subjects)
        # for i,item in enumerate(self.subjects):
        #     print(f"{i + 1}) {item}")

class Subject:
    def __init__(self,*subjects):
        self.subjects = list(subjects)
        print("Предметы",self.subjects)
    def get_list_subjects(self):
        return self.subjects

s = Subject("Математика","Информатика","Физика")
t = Teacher("Алексей","Сидоров")
s1 = Student("Андрей","Иванов")
s2 = Student("Олег","Сипьянов")
s3 = Student("Михаил","Романов")


print(f"Преподаватель: {t}\nСтуденты:\n1){s1}\n2){s2}\n3){s3}\n")

t.teach(s.subjects,s1,s2,s3)

print("Студент ",s1.name,"освоил:")
s1.show_subjects()