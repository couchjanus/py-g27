contacts = [
    ['cat', '2222222', '2021-12-16'],
    ['tom', '1111111', '2021-12-16'],
    ['dog', '3333333', '2021-12-16'],
]

fields = ('name', 'phone', 'date')

# contact = dict.fromkeys(range(10))
contact = dict.fromkeys(fields)
print(contact)


contacts_dict = {}
contacts_dict = dict.fromkeys(fields, 7)

print(contacts_dict)

keys = list(dict.fromkeys(fields))

def convert_list_to_dict(keys, values):
    result = {keys[i]:values[i] for i in range(len(values))}
    return result

contacts_list = []

for item in contacts:
    res = convert_list_to_dict(keys, item) 
    contacts_list.append(res)
    
print(contacts_list)



