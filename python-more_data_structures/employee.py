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
        if amount >= 0:
            self.__salary = amount  
        else:
            print("Salary cannot be negative!")

    @property
    def position(self):
        return self.__position   

    @position.setter
    def position(self, new_position):
        self.__position = new_position 

    def apply_bonus(self, percentage):
        self.__bonus = (self.__salary * percentage) / 100  

    def annual_salary(self):
        return (self.__salary * 12) + self.__bonus  

    def __str__(self):
        return f"Employee {self.__name} works as {self.__position} with a salary of ${self.__salary}"  
    