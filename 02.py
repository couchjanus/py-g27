from datetime import datetime

# def welcome():
#     return input("""Welcome to Phone Book
#                     At hand:
#                     1. All contacts
#                     2. New contact
#                     3. Show contact
#                     4. Edit contact
#                     5. Delete contact
#                     6. Exit
#                     Your choice (1,2,3,4,5,6)>:""")

contacts = [
    ['cat', '2222222', '2021-12-16'],
    ['tom', '1111111', '2021-12-16'],
    ['dog', '3333333', '2021-12-16'],
]

choices = [
    '',
    'All contacts', 
    'New contact',
    'Show contact',
    'Edit contact',
    'Delete contact',
    'Exit'
]

# def welcome():
#     prompt = """Welcome to Phone Book
#         At hand:\n"""
#     for index, item in enumerate(choices):
#         if index == 0: continue
#         prompt += f'{" "*12} {index}. {item}\n' 
        
#     prompt += f'{" "*12} Your choice (1,2,3,4,5,6)>:'    
                    
#     return prompt
   
def welcome():
    prompt = """Welcome to Phone Book
        At hand:\n"""
    tmp = "Your choice("
    
    for index, item in enumerate(choices):
        if index == 0: continue
        tmp += f'{index},'
        
        prompt += f'{" "*12} {index}. {item}\n' 
        
    return prompt + f'{" "*12} {tmp[:-1]} Or q)>:' 
                    
# fields = ('name', 'phone', 'date')
fields = ('name', 'phone')

def add_contact():
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
    return contact


def find_contact():
    name = input(f'Enter {fields[0]} for search: ')
    for contact in contacts: 
        print(contact)
        for item in contact:
            if name in item:
                return item         
    return None
        
def edit_contact(i):
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
    contact.append(datetime.today().strftime("%Y-%m-%d"))
    contacts[i] = contact
    
def main():
        
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
                contacts.append(add_contact())
            case 3:
                res = find_contact()
                contact = res if res else 'Nothing found'
                print(contact)
            case 4:
                res = find_contact()
                index = contacts.index(res)
                edit_contact(index)
                print(contacts)
            case 5:
                res = find_contact()
                index = contacts.index(res)
                del contacts[index]
                print(contacts)
            case 6:
                print('Thanks for using Phone Book')
                break
            case _:
                print('Incorrect choice')
                    
if __name__ == '__main__':
    main()
    # print(type([])) #<class 'list'>
    # print(len([])) # 0
    # print(len(list()))
    
    # for item in choices:
    #     print(item)
    
    # for index, item in enumerate(choices):
    #     print(index, item)
    
    # print(welcome())
    # for i in range(0, len(choices)):
    #     print(i)
    #     print(choices[i])