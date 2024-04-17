from fastapi import APIRouter, HTTPException
from schemas.doctors_schema import Doctors, DoctorsCreate, DoctorsUpdate, doctors

from services.doctors_services import DoctorSerivce

doctor_router = APIRouter()

@doctor_router.get('/GetAllDoctors', status_code=200)
def getAllDoctors():
    return {'message': 'successful', 'data': doctors}

@doctor_router.get('/GetAllActiveDoctors', status_code=200)
def getAllActiveDoctors():
    data = DoctorSerivce.get_doctor_all_active()
    return {'message': 'successful', 'data': data}


@doctor_router.get('/GetAllDeActiveDoctors', status_code=200)
def getAllActiveDoctors():
    data = DoctorSerivce.get_doctor_all_deactive()
    return {'message': 'successful', 'data': data}


@doctor_router.get('/GetDoctorByID/{id}', status_code=200)
def GetDoctorByID(id: int):
    data = DoctorSerivce.get_doctor_by_id(id)
    return {'message': 'successful', 'data': data}


@doctor_router.post('/CreateDoctor', status_code=201)
def CreateDoctor(payload: DoctorsCreate):
    data = DoctorSerivce.create_doctors(payload)
    return {'message': 'successful', 'data': data}

@doctor_router.put('/UpdateAvailabilityToBusy/{id}', status_code=200)
def update_availability_busy(id: int):
    data = DoctorSerivce.update_doctors_status_busy(id)
    return {'message': 'successful', 'data': data}

@doctor_router.put('/UpdateAvailabilityToFree/{id}', status_code=200)
def update_availability_free(id: int):
    data = DoctorSerivce.update_doctors_status_free(id)
    return {'message': 'successful', 'data': data}

@doctor_router.post('/UpdateStatus', status_code=200)
def update_doctors_status(active: str, doctor_id : int):
    if active not in ["ENABLED", "DISABLED"]:
        # If the status is not valid, raise an HTTPException with a 400 status code
        raise HTTPException(status_code=400, detail="Invalid status. Please provide 'ENABLED' or 'DISABLED'.")
    data = DoctorSerivce.update_doctors_status(active, doctor_id)
    return {'message': 'successful', 'data': data}

@doctor_router.post('/UpdateStatusByID', status_code=200)
def update_doctors_by_id(payload: DoctorsUpdate):
    data = DoctorSerivce.update_doctors_status_id(payload)
    return {'message': 'successful', 'data': data}
    
# @doctor_router.delete('/DeleteDoctorByID/{id}', status_code=200)
# def DeleteDoctorByID(id: int):
#     data = DoctorSerivce.delete_doctors_by_id(id)
#     return {'message': 'successful', 'data': data}