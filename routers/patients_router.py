from fastapi import APIRouter, HTTPException
from logger.logger import logger
from schemas.patient_schema import PatientsCreate, Patients, PatientsStatus, patients, PatientsUpdate
#from schemas.patient_schema import Patients, patients, PatientsUpdate
from services.patients_services import PatientsSerivce, PatientsCreate, PatientsUpdate


patient_router = APIRouter()

@patient_router.get('/GetAllPatient', status_code=200)
def getAllPatient():
     logger.info(f"All appointments fetched successfully {patients}")
     return {'message': 'successful', 'data': patients}

@patient_router.get('/GetPatientByID/{id}', status_code=200)
def GetPatientByID(id: int):
    try:
        data = PatientsSerivce.get_patient_by_id(id)
        logger.info(f"Patient with ID: {id}, fetched successfully")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Error Getting Patient by ID: {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@patient_router.get('/GetPatientByMsisdn/{phone}', status_code=200)
def GetPatientByMsisdn(phone: str):
    try:
        data = PatientsSerivce.get_patient_by_msisdn(phone)
        logger.info(f"Patient with ID: {phone}, fetched successfully.")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Error Getting Patient by ID: {phone}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@patient_router.post('/CreatePatient', status_code=201)
def CreatePatient(payload: PatientsCreate):
    try:
        data = PatientsSerivce.create_patient(payload)
        logger.info(f"Patient {payload} successfully created")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Failed to create Patient {payload})")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@patient_router.post('/UpdateStatus', status_code=200)
def update_patient_status(active: str, patient_id : int):
    try:
        if active not in ["ENABLED", "DISABLED"]:
            logger.error(f"Invalid status. Please provide 'ENABLED' or 'DISABLED', {active}.)")
            raise HTTPException(status_code=400, detail="Invalid status. Please provide 'ENABLED' or 'DISABLED'.")
        data = PatientsSerivce.update_patient_status(active, patient_id)
        logger.info(f"Patient with ID: {patient_id}, updated successfully.)")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Patient with ID: {patient_id}, Not updated successfully.)")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@patient_router.post('/UpdateStatusByID', status_code=200)
def update_patients_status_id(payload: PatientsUpdate):
    try:
        data = PatientsSerivce.update_patients_status_id(payload)
        logger.info(f"Patient Successful Update, {payload}.)")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Patient Update failed, {payload} .)")
        raise HTTPException(status_code=500, detail="Internal Server Error")

