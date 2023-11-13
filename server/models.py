from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db=SQLAlchemy()

class Patient(db.Model,SerializerMixin):
    __tablename__='patients'

    id=db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String)
    lastname=db.Column(db.String)
    gender=db.Column(db.String)
    age=db.Column(db.Integer)
    phonenumber=db.Column(db.Integer)
    national_id=db.Column(db.Integer)

    #relationships
    appointments=db.relationship('Appointment', backref='patient')

    serialize_rules=('-appointments.patient',)


class Appointment(db.Model,SerializerMixin):
    __tablename__='appointments'
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.String)
    time=db.Column(db.String)
    status=db.Column(db.String)

    #F.keys
    patient_id=db.Column(db.Integer, db.ForeignKey('patients.id'))
    patient_visit_id=db.Column(db.Integer, db.ForeignKey('patient_visits.id'))

    serialize_rules=('-patient.appointments', '-patient_visit.appointments',)


class PatientVisit(db.Model,SerializerMixin):
    __tablename__='patient_visits'

    id=db.Column(db.Integer, primary_key=True)
    diagnosis=db.Column(db.String)
    prescription=db.Column(db.String)
    dosage=db.Column(db.String)
    date=db.Column(db.DateTime, server_default=db.func.now())

    #relationship
    appointments=db.relationship('Appointment', backref='patient_visit')
    drugs=db.relationship('Drug', backref='patient_visit')

    serialize_rules=('-appointments.patient_visit','-drugs.patient_visit',)

class Drug(db.Model,SerializerMixin):
    __tablename__='drugs'

    id=db.Column(db.Integer, primary_key=True)
    drug_name=db.Column(db.String)
    description=db.Column(db.String)
    date=db.Column(db.DateTime, server_default=db.func.now())
    
    #F.key
    patient_visit_id=db.Column(db.Integer, db.ForeignKey('patient_visits.id'))

    serialize_rules=('-patient_visit.drugs')