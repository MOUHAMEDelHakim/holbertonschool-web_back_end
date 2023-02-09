#!/usr/bin/env python3
"""
Module for filtered_logger
"""
import re
import logging
import os
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

