class Productivity:
    def __init__(self) -> None:
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole
        }
    
    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type()
        
    def track(self, employees, hours):
        print('Tracking System')
        for employee in employees:
            employee.work(hours)
        print('')
        

class ManagerRole():
    def perform_duties(self, hours):
        print(f'screams and yells for {hours} hours.')
        
class SecretaryRole():
    def perform_duties(self, hours):
        print(f' expends {hours} hours doing office paperwork.')
        
class SalesRole():
    def perform_duties(self, hours):
        print(f' expends {hours} hours on the phone.')
        
class FactoryRole():
    def perform_duties(self, hours):
        print(f' manufactures gadgrts for {hours} hours.')
          