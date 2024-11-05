from models.__init__ import CURSOR, CONN
from models.owner import Owner

class Cat:
    all = {}

    def __init__(self, name, weight, owner_id, id_ = None):
        self.id = id_
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
        if type(weight) is float:
            self._weight = weight
        else:
            raise ValueError("Weight must be an integer")
    
    @property
    def owner_id(self):
        return self._owner_id
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
                weight REAL,
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
        sql = """
            INSERT INTO cats (name, weight, owner_id)
                VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.weight, self.owner_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE cats
            SET name = ?, weight = ?, owner_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.weight, self.owner_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM cats
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def create(cls, name, weight, owner_id):
        cat = cls(name, weight, owner_id)
        cat.save()
        return cat

    @classmethod
    def instance_from_db(cls, row):
        cat = cls.all.get(row[0])
        if cat:
            cat.name = row[1]
            cat.weight = row[2]
            cat.owner_id = row[3]
        else:
            id_ = row[0]
            cat = cls(row[1], row[2], row[3], id_=id_)
            cls.all[id_] = cat
        return cat

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM cats"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM cats
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM cats
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_weight(cls, weight):
        sql = """
            SELECT *
            FROM cats
            WHERE weight = ?
        """
        row = CURSOR.execute(sql, (weight,)).fetchone()
        return cls.instance_from_db(row) if row else None
        
    @classmethod
    def find_all_by_owner_id(cls, owner_id):
        sql = """
            SELECT *
            FROM cats
            WHERE owner_id = ?
        """
        rows = CURSOR.execute(sql, (owner_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]#  if row else None