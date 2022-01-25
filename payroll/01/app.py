import payroll_system.payroll as pr

salary_employee = pr.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = pr.HourlyEmployee(2, 'John Doe', 40, 15)
commisson_employee = pr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)

payroll_system = pr.Payroll()

payroll_system.calculate_payroll([
    salary_employee, 
    hourly_employee, 
    commisson_employee   
])