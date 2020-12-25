class School:
    def __init__(self, title, location):
        self.title = title
        self.location = location

class Student:
    def __init__(self, age, name, school):
        self.age = age
        self.name = name
        self.school = school
    def __str__(self):
        return (f'{self.name} {self.school.title} {self.age}')

class Profesor(Student):
    pass
    def __init__(self, age, name, school, subject):
        super().__init__(age, name, school)
        self.subject = subject

class Subject:
    def __init__(self, title):
        self.title = title

skola1 = School("Petar Petrovic", "Danilovgrad")
skola2 = School("Marka Miljanova", "Podgorica")

student1 = Student(16,"Danilo",skola1)
student1 = Student(17,"Luka",skola2)

matematika = Subject("matematika")
racunari = Subject("racunari")

profesor1 = Profesor(41,"Radosav",skola1,matematika)
profesor2 = Profesor(56,"Milijana",skola2,racunari)

print(profesor1)
profesor1.name = "Milosav"
profesor1.school = skola2
print(profesor1)
print(student1)