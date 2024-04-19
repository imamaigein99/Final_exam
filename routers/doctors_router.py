from fastapi import APIRouter, HTTPException
from logger.logger import logger
from schemas.doctors_schema import Doctors, DoctorsCreate, DoctorsUpdate, doctors

from services.doctors_services import DoctorSerivce

doctor_router = APIRouter()

@doctor_router.get('/GetAllDoctors', status_code=200)
def getAllDoctors():
    logger.info(f"All Doctors fetched successfully {doctors}")
    return {'message': 'successful', 'data': doctors}

@doctor_router.get('/GetAllActiveDoctors', status_code=200)
def getAllActiveDoctors():
    try:
        data = DoctorSerivce.get_doctor_all_active()
        logger.info(f"All Active Doctors fetched successfully {data}")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Error fetching Active Doctors {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@doctor_router.get('/GetAllDeActiveDoctors', status_code=200)
def getAllActiveDoctors():
    try:
        data = DoctorSerivce.get_doctor_all_deactive()
        logger.info(f"All Inactive Doctors fetched successfully {data}")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Error fetching Inactive Doctors {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@doctor_router.get('/GetDoctorByID/{id}', status_code=200)
def GetDoctorByID(id: int):
    try:
        data = DoctorSerivce.get_doctor_by_id(id)
        logger.info(f"Doctors with ID: {id}, fetched successfully {data}")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Error Getting Doctor by ID: {id}, {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@doctor_router.post('/CreateDoctor', status_code=201)
def CreateDoctor(payload: DoctorsCreate):
    try:
        data = DoctorSerivce.create_doctors(payload)
        logger.info(f"Doctors {payload} successfully created")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Failed to create Doctor {payload})")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@doctor_router.put('/UpdateAvailabilityToBusy/{id}', status_code=200)
def update_availability_busy(id: int):
    try:
        data = DoctorSerivce.update_doctors_status_busy(id)
        logger.info(f"Doctors with {id} Updated to Busy successfully.")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Doctors with {id} Not Updated to Busy successfully.)")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@doctor_router.put('/UpdateAvailabilityToFree/{id}', status_code=200)
def update_availability_free(id: int):
    try:
        data = DoctorSerivce.update_doctors_status_free(id)
        logger.info(f"Doctors with {id} Updated to Free successfully.")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Doctors with {id} Not Updated to Free successfully.)")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@doctor_router.post('/UpdateStatus', status_code=200)
def update_doctors_status(active: str, doctor_id : int):
    try:
        if active not in ["ENABLED", "DISABLED"]:
            logger.error(f"Invalid status. Please provide 'ENABLED' or 'DISABLED', {active}.)")
            raise HTTPException(status_code=400, detail="Invalid status. Please provide 'ENABLED' or 'DISABLED'.")
        data = DoctorSerivce.update_doctors_status(active, doctor_id)
        logger.info(f"Doctor with ID: {doctor_id}, updated successfully.)")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Doctor with ID: {doctor_id}, Not updated successfully.)")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@doctor_router.post('/UpdateStatusByID', status_code=200)
def update_doctors_by_id(payload: DoctorsUpdate):
    try:
        data = DoctorSerivce.update_doctors_status_id(payload)
        logger.info(f"Successful Update, {payload}.)")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Doctor Update failed, {payload} .)")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
# @doctor_router.delete('/DeleteDoctorByID/{id}', status_code=200)
# def DeleteDoctorByID(id: int):
#     data = DoctorSerivce.delete_doctors_by_id(id)
#     return {'message': 'successful', 'data': data}