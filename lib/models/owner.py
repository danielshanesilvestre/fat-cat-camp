class Owner:
    def __init__(self, name, phone_number, id = None):
        pass

    @property
    def name(self):
        pass
    @name.setter
    def name(self, name):
        pass

    @property
    def phone_number(self):
        pass
    @phone_number.setter
    def phone_number(self, phone_number):
        pass

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS owners (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone_number TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS owners;
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
    def create(cls, name, phone_number):
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

    def get_owned_cats(self):
        pass
