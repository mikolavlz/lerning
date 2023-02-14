class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Imya:{self.name}, Familia : {self.surname}"

class Teacher(Person):
    def __str__(self,name,surname):
        super().__init__(name,surname)
    def teach(self,subject,students):
        for students in students:
            students.study(subject)
         .....

class Student(Person):
    def __init__(self,name,surname):
        super.__init__(name,surname)
        self.subjects = []
    def study(self,subjects):
        self.subjects.append(subjects)
    def show_subjects(self):
        for i,item in enumerate(self.subjects):
            print(f'{item+1}{item}')

class Subject:
    def __init__(self,*subjects):
        self.subjects = list(subjects)
    def get_lisr_subjects(self):
        return self.subjects

s = Subject("Matematika""Inaormatika""Fizika")
t = Teacher("Sidorov""Petov")
s1= Student("Andrei""Sidorov")
s2= Student("Oleg""Sipyanov")
s3= Student("Mixail""Romanov")

print(f'Prepod :{t}\n Student {s}\n ')



man = Person('Ivan','Ivanov')
print(man)