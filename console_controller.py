#import phones
import pickle_ser
import console_manager
import network_manager
import redis_phones

serializer = pickle_ser.PickleSerializer()
iomanager = console_manager.ConsoleManager()
#iomanager = network_manager.NetworkManager()
contacts = redis_phones.Contacts(serializer)

def input_name():
    return iomanager.input('Name? ')
    
def input_phone():
    return iomanager.input('Phone? ')

def to_str_contact(name, phone):
    return "{}: {}\n".format(name, phone)

def create_contact():
    name = input_name()
    phone = input_phone()
    try:
        contacts.add_contact(name, phone)
    except KeyError as e:
        iomanager.output(str(e))
        
def list_contacts():
    for name, phone in contacts.list_contacts():
        iomanager.output(to_str_contact(name, phone))
        
def find_contact():
    name = input_name()
    try:
        iomanager.output(to_str_contact(name, contacts.get_phone(name)))
    except KeyError as e:
        iomanager.output(str(e))
    
def update_contact():
    name = input_name()
    phone = input_phone()
    try:
        contacts.update_contact(name, phone)
    except KeyError as e:
        iomanager.output(str(e))
        

def delete_contact():
    name = input_name()
    try:
        contacts.delete_contact(name)
    except KeyError as e:
        iomanager.output(str(e))

def quit():
    try:
        contacts.save()
    except IOError as e:
        iomanager.output(str(e))
    exit()

actions = {
    'c': create_contact,
    'l': list_contacts,
    'f': find_contact,
    'u': update_contact,
    'd': delete_contact,
    'q': quit
}

while True:
    action = iomanager.input('Action? ').lower()
    try:
        actions[action]()
    except KeyError:
        iomanager.output("Invalid action")
