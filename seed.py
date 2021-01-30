"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb notable_db')
os.system('createdb notable_db')

model.connect_to_db(server.app)
model.db.create_all()

doc_1 = crud.create_doc('Paul', 'Smith')
doc_2 = crud.create_doc('John', 'Watson')

pat_1 = crud.create_patient('Sarah', 'Jones')
pat_2 = crud.create_patient('Joe', 'Blah')
pat_3 = crud.create_patient('Raul', 'Tom')
pat_4 = crud.create_patient('George', 'Win')


apt_1 = crud.create_apt(1, 1, '12-12-20', '08:30AM', 'New Patient')
apt_2 = crud.create_apt(2, 2, '12-12-20', '08:30AM', 'Follow-up')
apt_3 = crud.create_apt(1, 3, '12-12-20', '09:30AM', 'Follow-up')
apt_4 = crud.create_apt(1, 4, '12-12-20', '08:30AM', 'New Patient')
apt_5 = crud.create_apt(1, 2, '12-16-20', '08:30AM', 'New Patient')


