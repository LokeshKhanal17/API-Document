from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()
#create api for health care 
class HealthCare(BaseModel):
    id : int
    name: str
    age: int
    #date of birth
    date_of_birth: Optional[str] = None
    #gender
    gender: Optional[str] = None
    #address
    address: Optional[str] = None
    #phone number
    phone_number: Optional[str] = None
    #email
    email: Optional[str] = None
    #blood group
    blood_group: Optional[str] = None
    #height
    height: Optional[str] = None
    #weight
    weight: Optional[str] = None
    #allergies
    allergies: Optional[str] = None
    #chronic diseases
    chronic_diseases: Optional[str] = None
    #medications
    medications: Optional[str] = None

#create a database for health care to store the patient details
Patient_details = [
    { 
        "id": 1,
        "name": "Raj",
        "age": 25,
        "date_of_birth": "1996-05-25",
        "gender" : "male",
        "address": "Kathmandu",
        "phone_number": "9841234567",
        "email": "raj@gmail.com",
        "blood_group": "A+",
        "height": "5.5",
        "weight": "60",
        "allergies": "none",
        "chronic_diseases": "none",
    },
    {
        "id": 2,
        "name": "Rita",
        "age": 25,
        "date_of_birth": "1996-05-25",
        "gender" : "female",
        "address": "Kathmandu",
        "phone_number": "9841235567",
        "email": "rita@gmail.com",
        "blood_group": "A+",
        "height": "5.5",
        "weight": "60",
        "allergies": "none",
        "chronic_diseases": "none",
    }

]

#get request to get all the patient details
@app.get("/healthcare")
async def get_patient_details():
    return Patient_details

#get request to get the patient details by id
@app.get("/healthcare/{id}")
async def get_patient_details_by_id(id: int):
    #use exception handling
    try:
        for patient in Patient_details:
            if patient["id"] == id:
             return patient
    except:
        return "Patient not found"


#post request to add new patient details
@app.post("/healthcare")
async def add_patient_details(healthcare: HealthCare):
    Patient_details.append(healthcare.dict())
    return healthcare
#patch method to update the patient allergies and chronic diseases by id
@app.patch("/healthcare/{id}")
async def update_patient_allergies_and_chronic_diseases(id: int, healthcare: HealthCare):
    try:
        for patient in Patient_details:
            if patient["id"] == id:
                patient["allergies"] = healthcare.allergies
                patient["chronic_diseases"] = healthcare.chronic_diseases
                return patient
    except:
        return "Patient not found"

#put request to update the patient details by id 
@app.put("/healthcare/{id}")
async def update_patient_details(id: int, healthcare: HealthCare):
    try:

        for patient in Patient_details:
            if patient["id"] == id:
                patient["name"] = healthcare.name
                patient["age"] = healthcare.age
                patient["date_of_birth"] = healthcare.date_of_birth
                patient["gender"] = healthcare.gender
                patient["address"] = healthcare.address
                patient["phone_number"] = healthcare.phone_number
                patient["email"] = healthcare.email
                patient["blood_group"] = healthcare.blood_group
                patient["height"] = healthcare.height
                patient["weight"] = healthcare.weight
                patient["allergies"] = healthcare.allergies
                patient["chronic_diseases"] = healthcare.chronic_diseases
                patient["medications"] = healthcare.medications
                return patient
    except:
     return "Patient not found"

#delete request to delete the patient details by id
@app.delete("/healthcare/{id}")
async def delete_patient_details(id: int):
    try:
        for patient in Patient_details:
            if patient["id"] == id:
                Patient_details.remove(patient)
                return patient
    except:
        return "Patient not found"








