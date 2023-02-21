#!/usr/bin/env python3

""" password in database Auth module
"""
from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> str:
    '''self descriptive'''
    salted_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return salted_password
