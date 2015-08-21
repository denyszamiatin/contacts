import settings
import redis

class Contacts(object):

    def __init__(self, serializer):
        self.serializer = serializer
        self.con=self.get_redis_connect()
   
    def get_redis_connect(self):
   	 return redis.StrictRedis(
       		 host=settings.REDIS_HOST,
       		 port=settings.REDIS_PORT,
        	 db=0
   	 )

    
    def add_contact(self, name, phone):
        if not self.con.setnx(name,phone):
            raise KeyError('Name exists')

    def _fail_if_name_not_exists(self, name):
        if not self.con.exists:
            raise KeyError("Name doesn't exist")

    def get_phone(self, name):
        self._fail_if_name_not_exists(name)
        return self.con.get(name)

    def delete_contact(self, name):
        self._fail_if_name_not_exists(name)
        self.con.delete(name)

    def update_contact(self, name, new_phone):
        self._fail_if_name_not_exists(name)
        self.con.set(name, new_phone)

    def list_contacts(self):
	return [(key,self.con.get(key)) for key in self.con.keys()]

    def save(self):
	pass

