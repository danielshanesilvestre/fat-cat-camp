from models.__init__ import CURSOR, CONN

class Owner:
    all = {}

    def __init__(self, name, phone_number, id_ = None):
        self.id = id_
        self.name = name
        self.phone_number = phone_number
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
    def phone_number(self):
        return self._phone_number
    # TODO: Validate phone number input as actual phone number
    @phone_number.setter
    def phone_number(self, phone_number):
        if isinstance(phone_number, str) and len(phone_number):
            self._phone_number = phone_number
        else:
            raise ValueError("Phone number must be a non-empty string")

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
        sql = """
            INSERT INTO owners (name, phone_number)
                VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.phone_number))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE owners
            SET name = ?, phone_number = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.phone_number, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM owners
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def create(cls, name, phone_number):
        owner = cls(name, phone_number)
        owner.save()
        return owner

    @classmethod
    def instance_from_db(cls, row):
        owner = cls.all.get(row[0])
        if owner:
            owner.name = row[1]
            owner.phone_number = row[2]
        else:
            id_ = row[0]
            owner = cls(row[1], row[2], id_=id_)
            cls.all[id_] = owner
        return owner

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM owners"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM owners
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM owners
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
