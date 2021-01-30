"""CRUD operations."""

from model import db, connect_to_db, Doctor, Appointment, Patient

import os
import requests

def get_doctors():
    """Return all doctors."""

    return Doctor.query.all()

def get_apts_by_doc_day(doc_id, day):
    """Return a list of all appointments for a particular doctor and particular day."""

    apts = Appointment.query.\
        filter(Appointment.doc_id == doc_id, Appointment.date_time.day == day).all()

    return apts

def delete_apt(apt_id):
    """Delete an appointment."""

    apt = Appointment.query.filter(Appointment.apt_id == apt_id).first()

    db.session.delete(apt)
    db.session.commit()


def create_apt(doc_id, pat_id, date_time, kind):
    """Create an appointment."""

    new_apt = Appointment(
        doc_id = doc_id,
        pat_id = pat_id,
        date_time = date_time,
        kind=kind
    )

    db.session.add(new_apt)
    db.session.commit()

    return new_apt


if __name__ == '__main__':
    from server import app
    connect_to_db(app)