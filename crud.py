"""CRUD operations."""

from model import db, connect_to_db, Doctor, Appointment, Patient

import os
import requests

def create_doc(fname, lname):
    """Register a doctor."""

    new_doc = Doctor(
        fname = fname,
        lname = lname
    )

    db.session.add(new_doc)
    db.session.commit()

    return new_doc

def create_patient(fname, lname):
    """Register a patient."""

    new_pat = Patient(
        fname = fname,
        lname = lname
    )

    db.session.add(new_pat)
    db.session.commit()

    return new_pat

def get_doctors():
    """Return all doctors."""

    return Doctor.query.all()

def get_apts_by_doc_day(doc_id, date):
    """Return a list of all appointments for a particular doctor and particular day."""

    apts = Appointment.query.\
        filter(Appointment.doc_id == doc_id, Appointment.date == date).all()

    return apts

def delete_apt(apt_id):
    """Delete an appointment."""

    apt = Appointment.query.filter(Appointment.apt_id == apt_id).first()

    db.session.delete(apt)
    db.session.commit()

    return "Appointment deleted"

def check_apt_availabilities(doc_id, date, time):

    apt_count = Appointment.query.\
        filter(Appointment.doc_id == doc_id, 
        Appointment.date == date, Appointment.time == time).count()

    return apt_count

def create_apt(doc_id, pat_id, date, time, kind):
    """Create an appointment."""

    new_apt = Appointment(
        doc_id = doc_id,
        pat_id = pat_id,
        date = date,
        time = time,
        kind=kind
    )

    db.session.add(new_apt)
    db.session.commit()

    return new_apt


if __name__ == '__main__':
    from server import app
    connect_to_db(app)