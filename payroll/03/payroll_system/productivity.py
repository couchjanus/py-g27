class Productivity:
    def track(self, employees, hours):
        print('Tracking System')
        for employee in employees:
            employee.work(hours)
        print('')