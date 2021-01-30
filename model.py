"""Data Models"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass


db = SQLAlchemy()

@dataclass
class Doctor(db.Model):
    """A doctor."""
    doc_id: int
    fname: str
    lname: str
    
    __tablename__ = "doctors"

    doc_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)

    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Doctor doc_id={self.doc_id} fname={self.fname}>'

@dataclass
class Patient(db.Model):
    """A patient."""
    pat_id: int
    fname: str
    lname: str
    
    __tablename__ = "patients"

    pat_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)

    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Patient pat_id={self.pat_id} fname={self.fname}>'


@dataclass
class Appointment(db.Model):
    """An appointment."""
    apt_id: int
    doc_id: int
    pat_id: int
    date_time: datetime
    kind: str

    __tablename__ = "appointments"

    apt_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)
    doc_id = db.Column(db.Integer, db.ForeignKey('doctors.doc_id'))
    pat_id = db.Column(db.Integer, db.ForeignKey('patients.pat_id'))
    date_time = db.Column(db.DateTime, nullable=False)
    kind = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Apt apt_id={self.apt_id} doc_id={self.doc_id} pat_id={self.pat_id}>'



def connect_to_db(flask_app, db_uri='postgresql:///notable_db', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    connect_to_db(app)