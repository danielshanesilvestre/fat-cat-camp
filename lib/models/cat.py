


class Cat:
    def __init__(self, name, weight, owner_id, id = None):
        pass

    @property
    def name(self):
        pass
    @name.setter
    def name(self, name):
        pass

    @property
    def weight(self):
        pass
    @weight.setter
    def weight(self, weight):
        pass
    
    @property
    def owner_id(self):
        pass
    @owner_id.setter
    def owner_id(self, weight):
        pass

    @classmethod
    def create_table(cls):
        pass
    
    @classmethod
    def drop_table(cls):
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
    
    @classmethod
    def create(cls, name, weight, owner_id):
        pass

    @classmethod
    def instance_from_db(cls):
        pass

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def find_by_id(cls):
        pass
    
    @classmethod
    def find_by_name(cls):
        pass
