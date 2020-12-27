import json
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
student2 = Student(17,"Luka",skola2)

matematika = Subject("matematika")
racunari = Subject("racunari")

profesor1 = Profesor(41,"Radosav",skola1,matematika)
profesor2 = Profesor(56,"Milijana",skola2,racunari)

print(profesor1)
profesor1.name = "Milosav"
profesor1.school = skola2
print(profesor1)
print(student1)
data = {}
data['schools'] = [
    {'name':skola1.title,'location':skola1.location},
    {'name':skola2.title,'location':skola2.location}
]
data['students'] = [
    {'name':student1.name,'age':student1.age,'school':student1.school.title},
    {'name':student2.name,'age':student2.age,'school':student2.school.title}
]
data['profesors'] = [
    {'name':profesor1.name,'age':profesor1.age,'school':profesor1.school.title,'predmet':profesor1.subject.title},
    {'name':profesor2.name,'age':profesor2.age,'school':profesor2.school.title,'predmet':profesor2.subject.title}
]
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)