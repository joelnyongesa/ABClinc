from flask import Flask, jsonify, make_response,request

from flask_migrate import Migrate
from models import db, Patient, Drug, Appointment, PatientVisit
from flask_restful import Api, Resource

from werkzeug.exceptions import NotFound


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

        response = make_response(
            jsonify(patients),
            200
        )

        return response
    
    def post(self):
        first_name = request.get_json()['firstname']
        last_name = request.get_json()['lastname']
        gender = request.get_json()['gender']
        age = request.get_json()['age']
        phone_number = request.get_json()['phonenumber']
        national_id = request.get_json()['national_id']

        patient = Patient(
            firstname=first_name,
            lastname=last_name,
            gender=gender,
            age=age,
            phonenumber=phone_number,
            national_id=national_id
        )

        db.session.add(patient)
        db.session.commit()

        patient_dict = patient.to_dict()

        response = make_response(
            jsonify(patient_dict),
            201
        )

        return response
    
class PatientByID(Resource):
    def get(self, id):
        patient = Patient.query.filter_by(id=id).first()

        return make_response(jsonify(patient.to_dict()),200)
    

    def patch(self, id):
        patient = Patient.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(patient, attr, request.get_json()[attr])
        
        db.session.add(patient)
        db.session.commit()

        patient_dict = patient.to_dict()
        response = make_response(
            jsonify(patient_dict),
            200
        )

        response.headers['Content-Type'] = "application/json"

        return response
    
    def delete(self, id):
        patient = Patient.query.filter_by(id=id).first()

        db.session.delete(patient)
        db.session.commit()

        response = make_response(
            jsonify({"message": "patient deleted successfully!"}), 
            200
            )

        return response
    


class Appointments(Resource):
    def get(self):
        appointments = [appointment.to_dict() for appointment in Appointment.query.all()]

        response = make_response(
            jsonify(appointments),
            200
        )

        return response
    
    def post(self):
        date = request.get_json()['date']
        time = request.get_json()['time']
        status = request.get_json()['status']
        patient_id = request.get_json()['patient_id']
        patient_visit_id = request.get_json()['patient_visit_id']

        appointment = Appointment(
            date=date,
            time=time,
            status=status,
            patient_id=patient_id,
            patient_visit_id=patient_visit_id,
        )

        db.session.add(appointment)
        db.session.commit()

        appointment_dict = appointment.to_dict()

        response = make_response(
            jsonify(appointment_dict),
            201
        )

        return response
    
class AppointmentByID(Resource):
    def get(self, id):
        appointment = Appointment.query.filter_by(id=id).first().to_dict()

        response = make_response(
            jsonify(appointment),
            200
        )

        return response
    
    def patch(self, id):
        appointmet = Appointment.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(appointmet, attr, request.get_json()[attr])

        db.session.add(appointmet)
        db.session.commit()

        appointmet_dict = appointmet.to_dict()

        response = make_response(
            jsonify(appointmet_dict),
            200
        )

        return response
    
    def delete(self, id):
        appointment = Appointment.query.filter_by(id=id).first()
        db.session.delete(appointment)
        db.session.commit()

        response = make_response(
            jsonify({"message": "appointment deleted successfully!"}),
            200
        )

        return response
    
class Drugs(Resource):
    def get(self):
        drugs=[drug.to_dict() for drug in Drug.query.all()]

        return make_response(jsonify(drugs),200)
    
    def post(self):
        drug_name=request.get_json()['drug_name']
        description=request.get_json()['description']

        new_drug=Drug(
            drug_name=drug_name,
            description=description
        )

        db.session.add(new_drug)
        db.session.commit()

        drug_dict=new_drug.to_dict()

        return make_response(jsonify(drug_dict),201)
    
class DrugByID(Resource):
    def get(self,id):
        drug=Drug.query.filter_by(id=id).first().to_dict()

        return make_response(drug,200)


    def patch(self,id):
        drug=Drug.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(drug,attr,request.get_json()[attr])

        db.session.add(drug)
        db.session.commit()

        drug_dict=drug.to_dict()

        response=make_response(jsonify(drug_dict),201)

        return response
    
    def delete(self,id):
        drug=Drug.query.filter_by(id=id).first()

        db.session.delete(drug)
        db.session.commit()

        return make_response({"Message": "Drug deleted successfully"})

class Visits(Resource):
    def get(self):
        visits=[visit.to_dict() for visit in PatientVisit.query.all()]

        response=jsonify(visits)

        return make_response(response,200)
    
    def post(self):
        new_visit=PatientVisit(
            diagnosis=request.get_json()['diagnosis'],
            dosage=request.get_json()['dosage'],
            drug_id=request.get_json()['drug_id']
        )

        db.session.add(new_visit)
        db.session.commit()

        visit_dict=new_visit.to_dict()

        response=make_response(visit_dict,201)
        return response
    

class VisitsByID(Resource):
    def get(self,id):
        visit=PatientVisit.query.filter_by(id=id).first().to_dict()

        return make_response(jsonify(visit),200)
    
    def patch(self,id):
        visit=PatientVisit.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(visit,attr,request.get_json()[attr])

        db.session.add(visit)
        db.session.commit()

        visit_dict=visit.to_dict()

        return make_response(visit_dict,201)
    
    def delete(self,id):
        visit=PatientVisit.query.filter_by(id=id).first()

        db.session.delete(visit)
        db.session.commit()

        return make_response({'message':"patient visit deleted successfully"})

    

@app.errorhandler(NotFound)
def handle_error(self):
    return make_response("Not Found: The requested Resource(endpoint) does not exists",404)
    

    

api.add_resource(Patients, '/patients', endpoint='patients')
api.add_resource(PatientByID, '/patients/<int:id>', endpoint='patients_id')
api.add_resource(Appointments, '/appointments', endpoint='appointments')
api.add_resource(AppointmentByID, '/appointments/<int:id>', endpoint='appointment_id')
api.add_resource(Drugs,'/drugs', endpoint='drugs')
api.add_resource(DrugByID,'/drugs/<int:id>', endpoint='drugs_id')
api.add_resource(Visits,'/visits', endpoint='visits')
api.add_resource(VisitsByID, '/visits/<int:id>', endpoint='visits_id')

#making sure added to development branch
