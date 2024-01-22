# ABClinic Project

There are various challenges that come with soring patients' data using the traditional file system method, some of which include the tedious process of retrieving patient records, and also risk of massive data loss in case of natural calamities like fire. To help solve this, we created a web application, ABClinic, that helps store patient records in a database, and retrieve the records in just a few clicks. This ensures safety of patient information (including previous and future visits, and their health records).

The project was created using [React JS](https://react.dev/), a JavaScript library for creating front-end applications, and [Flask](https://flask.palletsprojects.com/en/3.0.x/), a minimalist Python framework for creating back-end applications.

## How to get started

To contribute or have a local copy of this project in your development environment, follow the steps below:

1. Fork this project to create your own copy in your own GitHub Account

2. Clone the forked project using `git clone git@github.com:your-username/ABClinc.git`

3. Navigate to the project's directory using your terminal or file explorer.

4. Run `pipenv install && pipenv shell` at the root of the project directory to install the necessary libraries.

5. Navigate into the `server` directory using `cd server/`

6. Run `flask db upgrade` run the migrations and create the models and run `python seed.py` to insert some dummy data into the database.

8. Create environment variables using the following commands:

```
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555
```

This will have your Flask app running on port 5555

## API Endpoints Available

9. In a separate terminal, navigate into the `client` directory using the command `cd client`.
10. Install the NPM packages using `npm install`
11. Start the React server using the command `npm start` and this will start the application on `localhost:3000`

### 1. Patients
This is the endpoint for retrieving and adding patient details

```http
GET /patients
```

#### Responses

```javascript
{
  "first_name": string,
  "last_name": string,
  "gender": string,
  "age": integer,
  "phone_number": integer,
  "national_id": integer
}
```

#### Status Codes

| Status Code | Description |
| :--- | :--- |
| 200 | `SUCCESSFUL` |

```http
POST /patients
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `first_name` | `string` | **Required**. A patient's first name |
| `last_name` | `string` | **Required**, A patient's last name |
| `gender` | `string` | **Required**. A patient's gender |
| `age` | `integer` | **Required**. A patient's age |
| `phone_number ` | `integer` | **Required**, A patient's phone number |
| `national_id` | `integer` | **Required**, A patient's national ID number |

#### Responses

```javascript
{
  "first_name": string,
  "last_name": string,
  "gender": string,
  "age": integer,
  "phone_number": integer,
  "national_id": integer
}
```

#### Status Codes

| Status Code | Description |
| :--- | :--- |
| 201 | `CREATED` |

### 2. Patients By ID
This is the endpoint for retrieving, updating and deleting a particular patient's details.

```http
GET /patients/PATIENT_ID
```

#### Responses
```javascript
{
  "first_name": string,
  "last_name": string,
  "gender": string,
  "age": integer,
  "phone_number": integer,
  "national_id": integer
}
```

#### Status codes

| Status Code | Description |
| :--- | :--- |
| 200 | `SUCCESSFUL` |

```http
PATCH /patients/PATIENT_ID
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `attribute` | `attribute type` | **Required**. An attribute whose values are being updated |

#### Responses

```javascript
{
  "first_name": string,
  "last_name": string,
  "gender": string,
  "age": integer,
  "phone_number": integer,
  "national_id": integer
}
```
#### Status codes

| Status Code | Description |
| :--- | :--- |
| 200 | `SUCCESSFUL` |

```http
DELETE /patients/PATIENT_ID
```
#### Parameters

* None

#### Responses

```javascript
{
  "message": "patient deleted successfully"
}
```

#### Status codes

| Status Code | Description |
| :--- | :--- |
| 200 | `SUCCESSFUL` |

### 2. Appointments

This is an endpoint for retrieving, updating and deleting appointments.

```http
GET /appointments
```

#### Parameters

* None

#### Responses

```javascript
{
  "first_name": string,
  "last_name": string,
  "gender": string,
  "age": integer,
  "phone_number": integer,
  "national_id": integer
}
```

### 3. Appointments by ID

This is the endpoint for retrieving, updating, and deleting a specific appointment.

```http
GET /appointments/APPOINTMENT_ID
```

#### Responses

```javascript
{
  "date": string,
  "time": string,
  "status": string,
  "patient_id": integer,
  "patient_visit_id": integer
}
```
#### Status codes

| Status Code | Description |
| :--- | :--- |
| 200 | `SUCCESSFUL` |

```http
PATCH /patients/PATIENT_ID
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `attribute` | `attribute type` | **Required**. An attribute whose values are being updated |

#### Responses

```javascript
{
  "date": string,
  "time": string,
  "status": string,
  "patient_id": integer,
  "patient_visit_id": integer
}
```

#### Status codes

| Status Code | Description |
| :--- | :--- |
| 200 | `SUCCESSFUL` |

```http
DELETE /appointments/APPOINTMENT_ID
```
#### Parameters

* None

#### Responses

```javascript
{
  "message": "appointment deleted successfully"
}
```



5. Open Postman or ThunderClient (VS Code extension) to try out the endpoints which include:

* /patients
* /patients/\<int:id\>
* /appointments
* /appointmments/\<int:id\>


## Contributors

1. [Mercy Muriithi](https://github.com/mercy2525)
2. [Joel Nyongesa](https://github.com/joelnyongesa)
3. [Medrine Mulindi](https://github.com/mulindi123)

## Models
<img src='ABC_Clinic ERD.jpeg' />

