from faker import Faker
from models import db, Appointment, Patient, PatientVisit, Drug
import random


from app import app

fake = Faker()

with app.app_context():
    print("Deleting existing records...")
    Appointment.query.delete()
    Patient.query.delete()
    PatientVisit.query.delete()
    Drug.query.delete()

    print("Done deleting existing records...")

    patients = []

    for _ in range(10):
        patient = Patient(
            firstname = fake.first_name(),
            lastname=fake.last_name(),
            gender=random.choice(['Male', 'Female']),
            age=random.randint(1,80),
            phonenumber=fake.phone_number(),
            national_id=random.randint(15000000, 40000000)
        )
        patients.append(patient)

    print("Adding patients....")
    db.session.add_all(patients)
    db.session.commit()
    print("Done adding patients...")


    drugs = []
    drug_names = ["Neurozyme", "Synthitol", 
                  "Painquil", "Tranqitol", 
                  "Zapamine", "EnergiX", 
                  "Blissifyr", "CogniBoost", 
                  "RejuvaDose", "Globerex"
                  ]

    for drug_name in drug_names:
        drug = Drug(
            drug_name=drug_name,
            description=fake.sentence(10),
            # patient_visit = random.choice(patient_visits)
        )
        drugs.append(drug)

    print("Adding to drugs...")
    db.session.add_all(drugs)
    db.session.commit()

    patient_visits = []
    for _ in range(40):
        patient_visit = PatientVisit(
            diagnosis=fake.sentence(10),
            dosage=random.choice(["2X2", "1X3", "3X3", "1X2"]),
            drug=random.choice(drugs),
        )
        patient_visits.append(patient_visit)

    print("Adding to patient visits....")
    db.session.add_all(patient_visits)
    db.session.commit()
    print("Done adding patient visits...")

    appointments = []

    for _ in range(30):
        appointment = Appointment(
            date=fake.date_between(start_date='today', end_date='+1y'),
            time=fake.time(pattern='%H:%M'),
            status=random.choice(['Approved', 'Pending']),
            patient=random.choice(patients),
            patient_visit=random.choice(patient_visits)
        )
        appointments.append(appointment)

    print("Addint to appointments...")
    db.session.add_all(appointments)
    db.session.commit()
    print("Added all appointments")
    print("-----------------Done seeding------------------")