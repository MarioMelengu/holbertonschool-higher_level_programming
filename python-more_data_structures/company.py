from employee import Employee
class Company:
    def __init__(self, company_name):
        self.__company_name = company_name
        self.__employees = []
    
    @property
    def company_name(self):
        return self.__company_name
    
    @company_name.setter
    def company_name(self, new_company_name):
        self.__company_name = new_company_name
    
    @property
    def employee(self):
        return self.__employees
    
    def add_employee(self, employee):
        self.__employees.append(employee)
    
    def show_employees(self):
        for employee in self.__employees:
            print(employee)
    
    def remove_employee(self, employee_name):
        for employee in self.__employees:
            if employee.name == employee_name:
                self.__employees.remove(employee)
