"""CRUD operations."""

from model import db, connect_to_db

import os
import requests

if __name__ == '__main__':
    from server import app
    connect_to_db(app)