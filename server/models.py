from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


db=SQLAlchemy()
bcrypt = Bcrypt()


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

class Admin(db.Models,SerializerMixin):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    # We need to agree on the serialize rules and the relationships

    @hybrid_property
    def password_hash(self):
        raise ValueError("password hash cannot be viewed")
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))

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
    # prescription=db.Column(db.String)
    dosage=db.Column(db.String)
    date=db.Column(db.DateTime, server_default=db.func.now())

    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'))

    #relationship
    appointments=db.relationship('Appointment', backref='patient_visit')
    # drugs=db.relationship('Drug', backref='patient_visit')

    serialize_rules=('-appointments.patient_visit','-drug.patient_visits',)

    # many patient visits can get one drug prescription,.............

class Drug(db.Model,SerializerMixin):
    __tablename__='drugs'

    id=db.Column(db.Integer, primary_key=True)
    drug_name=db.Column(db.String)
    description=db.Column(db.String)
    date=db.Column(db.DateTime, server_default=db.func.now())
    
    #F.key
    # patient_visit_id=db.Column(db.Integer, db.ForeignKey('patient_visits.id'))

    patient_visits = db.relationship('PatientVisit', backref='drug')

    serialize_rules=('-patient_visits.drug',)