import random
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if type(value) is not str:
              raise TypeError("Value must be a string")
        self.__name = value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if type(age) is not int:
              raise TypeError("Age must be an integer")
        if age <= 0:
             raise ValueError("Age must be greater than 0")
        self.__age = age
    @property
    def grades(self):
        return self.__grades
    def add_grade(self, grade):
        if type(grade) is not int:
            raise TypeError("Grade must be an integer")
        if 4 <= grade <= 10:
            self.grades.append(grade)
    def average_grade(self):
        return  sum(self.grades) / len(self.grades)
    def to_dict(self):
        return {
            "name" : self.name,
            "age" : self.age,
            "grade" : self.grades
        }
    def __str__(self):
        return f"Student({self.name}, {self.age}, {self.grades})"
john_doe = Student("Test", 12)
for i in range(5):
    grade = random.randint(4, 10)
    john_doe.add_grade(grade)
print(f"Average grade is {john_doe.average_grade()}")
print(john_doe.to_dict())
