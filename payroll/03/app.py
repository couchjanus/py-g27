import payroll_system.payroll as pr

import payroll_system.employees as employees
import payroll_system.productivity as productivity

manager = employees.Manager(1, 'John Smith', 3000)
secretary = employees.Secretary(2, 'Mary Poppins', 2000)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_guy = employees.FactoryWorker(4, 'John Doe', 40, 25)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_guy
    
]

productivity = productivity.Productivity()
productivity.track(employees, 40)

payroll_system = pr.Payroll()

payroll_system.calculate_payroll(employees)

