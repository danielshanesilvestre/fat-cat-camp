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

ipdb.set_trace()
