from fastapi import APIRouter, HTTPException
from schemas.doctors_schema import Doctors, DoctorsCreate, doctors
from services.doctors_services import DoctorSerivce

doctor_router = APIRouter()

@doctor_router.get('/GetAllDoctors', status_code=200)
def getAllDoctors():
    return {'message': 'successful', 'data': doctors}


@doctor_router.get('/GetDoctorByID/{id}', status_code=200)
def GetDoctorByID(id: int):
    data = DoctorSerivce.get_doctor_by_id(id)
    return {'message': 'successful', 'data': data}


@doctor_router.post('/CreateDoctor', status_code=201)
def CreateDoctor(payload: DoctorsCreate):
    data = DoctorSerivce.create_doctors(payload)
    return {'message': 'successful', 'data': data}

@doctor_router.put('/UpdateStatusToBusy/{id}', status_code=200)
def update_status(id: int):
    data = DoctorSerivce.update_doctors_status_busy(id)
    return {'message': 'successful', 'data': data}

@doctor_router.put('/UpdateStatusToFree/{id}', status_code=200)
def update_status(id: int):
    data = DoctorSerivce.update_doctors_status_free(id)
    return {'message': 'successful', 'data': data}


# @doctor_router.delete('/DeleteDoctorByID/{id}', status_code=200)
# def DeleteDoctorByID(id: int):
#     data = DoctorSerivce.delete_doctors_by_id(id)
#     return {'message': 'successful', 'data': data}