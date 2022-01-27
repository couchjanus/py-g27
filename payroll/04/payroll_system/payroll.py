
class Payroll:
    def calculate_payroll(self, employees):
        print('Calculate Payroll')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f' - Check amount: {employee.calculate_payroll()}')
            if employee.address:
                print('- Sent To:')
                print(employee.address)
            print('')

class SalaryPolicy():
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary
        
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy():
    def __init__(self, hourly_worled, hour_rate):
        
        self.hourly_worled = hourly_worled
        self.hour_rate = hour_rate
        
    def calculate_payroll(self):
        return self.hourly_worled * self.hour_rate
    
class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission
        
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
            
