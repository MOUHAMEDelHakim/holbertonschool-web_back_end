#!/usr/bin/env python3

""" API endpoints
"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def root() -> str:
    ''' root route '''
    return jsonify({'message': 'Bienvenue'})
