        
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

     
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
        
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hourly_worled, hour_rate):
        super().__init__(id, name)
        self.hourly_worled = hourly_worled
        self.hour_rate = hour_rate
        
    def calculate_payroll(self):
        return self.hourly_worled * self.hour_rate
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
        
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
            

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')
        
class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')
        
class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')
        
class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgrts for {hours} hours.')
          
class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hourly_worled, hour_rate):
        HourlyEmployee.__init__(self, id, name, hourly_worled, hour_rate)
        
    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)