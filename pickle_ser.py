import pickle
import settings

class PickleSerializer(object):
    def load(self):
        try:
            with open(settings.FILENAME, 'r') as f:
                return pickle.load(f)
        except IOError:
            return {}
            
    def save(self, contacts):
        try:
            with open(settings.FILENAME, 'w') as f:
                pickle.dump(contacts, f)        
        except IOError:
            raise IOError("Can't write file")


