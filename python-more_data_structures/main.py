from employee import Employee
from company import Company

employee1 = Employee("ben", 3000, "developer")
employee2 = Employee("xhon", 4000, "junior developer")
xhoi_company = Company("Xhoi Company")
xhoi_company.add_employee(employee1)
xhoi_company.add_employee(employee2)
xhoi_company.remove_employee("ben")
xhoi_company.show_employees()
