import payroll_system.payroll as pr

import payroll_system.employees as employees
import payroll_system.productivity as productivity

import payroll_system.contacts as contacts

manager = employees.Manager(1, 'John Smith', 3000)
manager.address = contacts.Address(
   '121 Admin Rd',
   'Concord',
   'NH',
   '03301'
)

secretary = employees.Secretary(2, 'Mary Poppins', 2000)
secretary.address = contacts.Address(
   '11 Park Rd',
   'Brovary',
   'Kyiv',
   '01234'
)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
sales_guy.address = contacts.Address(
   '144 Rouse Rd',
   'Kyiv',
   'Kyiv',
   '01001'
)
factory_guy = employees.FactoryWorker(4, 'John Doe', 40, 25)
factory_guy.address = contacts.Address(
   '144 Mayakovsky Str',
   'Kyiv',
   'Kyiv',
   '01023'
)

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

