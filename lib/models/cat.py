from models.__init__ import CURSOR, CONN

class Cat:
    all = {}

    def __init__(self, name, weight, owner_id, id = None):
        self.id = id
        self.name = name
        self.weight = weight
        self.owner_id = owner_id
        pass

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, weight):
        if type(weight) is int:
            self._weight = weight
        else:
            raise ValueError("Weight must be an integer")
    
    @property
    def owner_id(self):
        pass
    @owner_id.setter
    def owner_id(self, owner_id):
        if type(owner_id) is int and Owner.find_by_id(owner_id):
            self._owner_id = owner_id
        else:
            raise ValueError("owner_id must reference an owner in the database")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS cats (
                id INTEGER PRIMARY KEY,
                name TEXT,
                weight INTEGER,
                owner_id INTEGER,
                FOREIGN KEY (owner_id) REFERENCES owners(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS cats;
        """
        CURSOR.execute(sql)
        CONN.commit()

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

    def get_cats_with_same_owner(self):
        pass