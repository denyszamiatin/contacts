import settings

class Contacts(object):

    def __init__(self, serializer):
        self.serializer = serializer
        self.contacts = self.serializer.load()

    def add_contact(self, name, phone):
        if name in self.contacts:
            raise KeyError('Name exists')
        self.contacts[name] = phone
        
    def _fail_if_name_not_exists(self, name):
        if name not in self.contacts:
            raise KeyError("Name doesn't exist")
        
    def get_phone(self, name):
        self._fail_if_name_not_exists(name)
        return self.contacts[name]
            
    def delete_contact(self, name):
        self._fail_if_name_not_exists(name)
        del self.contacts[name]
            
    def update_contact(self, name, new_phone):
        self._fail_if_name_not_exists(name)
        self.contacts[name] = new_phone
       
    def list_contacts(self):
        return self.contacts.items()
        
    def save(self):
        self.serializer.save(self.contacts)
