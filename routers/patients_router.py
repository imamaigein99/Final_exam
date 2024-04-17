from fastapi import APIRouter, HTTPException
from schemas.patient_schema import PatientsCreate, Patients, PatientsStatus, patients, PatientsUpdate
#from schemas.patient_schema import Patients, patients, PatientsUpdate
from services.patients_services import PatientsSerivce, PatientsCreate, PatientsUpdate


patient_router = APIRouter()

@patient_router.get('/GetAllPatient', status_code=200)
def getAllPatient():
    return {'message': 'successful', 'data': patients}

@patient_router.get('/GetPatientByID/{id}', status_code=200)
def GetPatientByID(id: int):
    data = PatientsSerivce.get_patient_by_id(id)
    return {'message': 'successful', 'data': data}

@patient_router.get('/GetPatientByMsisdn/{phone}', status_code=200)
def GetPatientByMsisdn(phone: str):
    data = PatientsSerivce.get_patient_by_msisdn(phone)
    return {'message': 'successful', 'data': data}

@patient_router.post('/CreatePatient', status_code=201)
def CreatePatient(payload: PatientsCreate):
    data = PatientsSerivce.create_patient(payload)
    return {'message': 'successful', 'data': data}

@patient_router.post('/UpdateStatus', status_code=200)
def update_patient_status(active: str, patient_id : int):
    if active not in ["ENABLED", "DISABLED"]:
        # If the status is not valid, raise an HTTPException with a 400 status code
        raise HTTPException(status_code=400, detail="Invalid status. Please provide 'ENABLED' or 'DISABLED'.")
    data = PatientsSerivce.update_patient_status(active, patient_id)
    return {'message': 'successful', 'data': data}

@patient_router.post('/UpdateStatusByID', status_code=200)
def update_patients_status_id(payload: PatientsUpdate):
    data = PatientsSerivce.update_patients_status_id(payload)
    return {'message': 'successful', 'data': data}

