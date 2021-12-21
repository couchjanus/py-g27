from datetime import datetime

# contacts = [
#     ['cat', '2222222', '2021-12-16'],
#     ['tom', '1111111', '2021-12-16'],
#     ['dog', '3333333', '2021-12-16'],
# ]

def init():
    
    contacts = [
        {'name': 'CAT', 'phone': 1234567, 'added': '2021-12-16'}, 
        {'name': 'Mary', 'phone': '5555555', 'added': '2021-12-21'},
        {'name': 'Tom', 'phone': 777777, 'added': '2021-12-16'}
    ]
    
    fields = ('name', 'phone')
    contact = dict.fromkeys(fields)
    
    return (contacts, contact)

choices = (
    '',
    'All contacts', 
    'New contact',
    'Show contact',
    'Edit contact',
    'Delete contact',
    'Exit'
)

def welcome():
    prompt = """Welcome to Phone Book
        At hand:\n"""
    tmp = "Your choice("    
    for index, item in enumerate(choices):
        if index == 0: continue
        tmp += f'{index},'        
        prompt += f'{" "*12} {index}. {item}\n'         
    return prompt + f'{" "*12} {tmp[:-1]} Or q)>:' 


def add_contact(contact):
    for key in contact:
        value = input(f'Enter {key}: ')
        contact[key] = value
    contact['added'] = datetime.today().strftime("%Y-%m-%d")
    return contact


def find_contact(contacts, name):
    for contact in contacts: 
        if contact['name'].lower() == name.lower():
            return contact    
    return None
        
def edit_contact(contact):
    for key in contact:
        value = input(f'Enter {key} for update: ') or contact[key]
        contact[key] = value
    contact['added'] = datetime.today().strftime("%Y-%m-%d")
    contact.update()
    
def main():
    contacts, contact = init()
    while True:
        choice = input(welcome())
        if choice == 'q': break
        choice = int(choice if choice.isdigit() else 0)
        
        match choice:
            case 0:
                continue
            case 1:
                print(contacts)
            
            case 2:
                contacts.append(add_contact(contact))
            case 3:
                name = input(f'Enter name for search contact: ') 
                res = find_contact(contacts, name)
                if res:
                    for item in res.items(): print(item)
                else: print('Nothing found')
            case 4:
                name = input(f'Enter name for edit contact: ') 
                res = find_contact(contacts, name)
                if res:
                    index = contacts.index(res)
                    edit_contact(contacts[index])
                else:
                    print('Nothinf found for edit')
            case 5:
                name = input(f'Enter name for destroy contact: ') 
                res = find_contact(contacts, name)
                if res:
                    confirm = input('Are You shoe? (Y/N') or 'n'
                    if confirm.lower() == 'y':
                        index = contacts.index(res)
                        contacts.remove(contacts[index])
            case 6:
                print('Thanks for using Phone Book')
                break
            case _:
                print('Incorrect choice')
                    
if __name__ == '__main__':
    main()
    