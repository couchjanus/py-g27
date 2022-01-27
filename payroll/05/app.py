from payroll_system.payroll import Payroll
from payroll_system.productivity import Productivity
from payroll_system.employees import EmployeeDatabase



productivity = Productivity()
payroll_system = Payroll()
employee_database = EmployeeDatabase()
employees = employee_database.employees
productivity.track(employees, 40)
payroll_system.calculate_payroll(employees)

