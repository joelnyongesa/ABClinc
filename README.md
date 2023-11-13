# ABClinic Project

In this project, we use Flask and React to create a full stack application for ABClinic. The web application enables easy record storing for patients, their appointments, diagnosis and prescriptions.

## How to get started

1. Clone this repo using the command:

```git
git clone git@github.com:joelnyongesa/ABClinc.git
```

2. Run `pipenv install && pipenv shell` at the root of your directory to install the necessary libraries.

3. Run `flask db upgrade` to prepopulate the database with dummy data.

4. Navigate into the server directory using `cd server/`. To create environment variables, use the following commands:

```
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555
```

This will have your Flask app running on port 5555

5. Open Postman or ThunderClient (VS Code extension) to try out the endpoints which include:

* /patients
* /patients/\<int:id\>
* /appointments
* /appointmments/\<int:id\>


## Contributors

1. [Mercy Muriithi]('https://github.com/mercy2525')
2. [Joel Nyongesa]('https://github.com/joelnyongesa)

## Models
<img src='ABC_Clinic ERD.jpeg' />

