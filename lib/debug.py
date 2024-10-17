#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.cat import Cat
from models.owner import Owner
import ipdb


def reset_database():
    Cat.drop_table()
    Owner.drop_table()
    Owner.create_table()
    Cat.create_table()

    john_smith = Owner.create("John Smith", "123 456 7890")
    Cat.create("Mittens", 10.0, john_smith.id)
    Cat.create("Crumbs", 11.1, john_smith.id)
    Cat.create("Laila", 12.2, john_smith.id)

reset_database()
ipdb.set_trace()
