
class Payroll:
    def calculate_payroll(self, employees):
        print('Calculate Payroll')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f' - Check amount: {employee.calculate_payroll()}')
            print('')

    