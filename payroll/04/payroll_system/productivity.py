class Productivity:
    def track(self, employees, hours):
        print('Tracking System')
        for employee in employees:
            employee.work(hours)
        print('')
        

class ManagerRole():
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')
        
class SecretaryRole():
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')
        
class SalesRole():
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')
        
class FactoryRole():
    def work(self, hours):
        print(f'{self.name} manufactures gadgrts for {hours} hours.')
          