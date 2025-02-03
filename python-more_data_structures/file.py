class Employee:
    def __init__(self, name, salary, position):
        self.__name = name
        self.__salary = salary
        self.__position = position
        self.__bonus = 0

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        self.__salary = amount

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def apply_bonus(self, percentage):
        self.__bonus = self.__salary * percentage

    @property
    def bonus(self):
        return self.__bonus

    def annual_salary(self):
        return self.__salary * 12 + self.bonus

    def __str__(self):
        return f"Employee {self.__name} works as {self.__position} with a salary of ${self.__salary}"

emp = Employee("John Doe", 50000, "Developer")
emp.salary = 60000
emp.apply_bonus(10)
print(emp.annual_salary())
print(emp)
