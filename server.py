from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, make_response)

import os
from model import connect_to_db
import crud

FLASK_SECRET_KEY = os.environ['FLASK_SECRET_KEY']

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

@app.route('/')
def index():
    """Home page."""
    return render_template('index.html')

@app.route('/doctors')
def get_doctors():
    """Return a list of all doctors."""

    doctors = crud.get_doctors()

    return jsonify(doctors)

@app.route('/apts', methods=['POST'])
def get_apts():
    """Return a list of all appointments for a particular doctor and particular day."""

    doc_id = request.json.get('doc_id')
    date = request.json.get('date')

    apts = crud.get_apts_by_doc_day(doc_id, date)

    return jsonify(apts)

@app.route('/apts/<apt_id>', methods=['DELETE'])
def delete_apt(apt_id):
    """Delete an appointment."""

    res = crud.delete_apt(apt_id)

    return res

@app.route('/apts/create', methods=['POST'])
def create_apt():
    """Create an appointment."""

    doc_id = request.json.get('doc_id')
    pat_id = request.json.get('pat_id')
    date = request.json.get('date')
    time = request.json.get('time')
    kind = request.json.get('kind')

    if int(time[3:5]) % 15 != 0:
        return "New appointments can only start at 15 minute intervals."

    apt_count = crud.check_apt_availabilities(doc_id, date, time)
    if apt_count < 3:
        new_apt = crud.create_apt(doc_id, pat_id, date, time, kind)
        return jsonify(new_apt)
    else:
        return "Too many appointments at that date/time."



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)