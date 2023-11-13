from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from models import db, Patient, Drug, Appointment, PatientVisit
from flask_restful import Api, Resource


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


class Patients(Resource):
    def get(self):
        patients = [patient.to_dict() for patient in Patient.query.all()]

        return make_response(jsonify(patients), 200)
    
class PatientByID(Resource):
    def get(self, id):
        patient = Patient.query.filter_by(id=id).first()

        return make_response(jsonify(patient.to_dict()),200)

api.add_resource(Patients, '/patients', endpoint='patients')
api.add_resource(PatientByID, '/patients/<int:id>', endpoint='patients_id')