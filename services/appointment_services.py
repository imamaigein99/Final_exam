from fastapi import HTTPException
import time
from schemas.appointment_schemas import Appointments, AppointmentStatus, appointment
from schemas.doctors_schema import doctors, Doctors
from services.doctors_services import DoctorSerivce

class AppointmentsSerivce:


    @staticmethod
    def get_appointment_by_id(appointment_id):
        if appointment_id in appointment:
            return appointment[appointment_id]
        else: 
            return {"ResponseCode": "01", "ResponseMessage": "Appointment Does Not Exist"}
        
        
    @staticmethod
    def create_appointment(patient_phone: str, date_timer: str, duration: str, reasons: str, notes: str, location: str):
        timestamp_ms = int(time.time() * 1000)
        free_doctor = DoctorSerivce.find_free_doctor()
        #print (free_doctor)
        if free_doctor is None:
            
            return {"ResponseCode": "01", "ResponseMessage": "There are no Free Doctors at the moment"}
    
        appointment_id = timestamp_ms
        new_appointment = Appointments(
            appointment_id=appointment_id, 
            patient_phone=patient_phone,
            doctor_name=free_doctor.name,
            date_timer=date_timer,
            duration=duration,
            reasons=reasons,
            notes=notes,
            location=location,
            status="scheduled"
        )

        appointment[appointment_id] = new_appointment
        DoctorSerivce.update_doctors_status_busy(free_doctor.id)
        return {"ResponseCode": "00", "ResponseMessage": f"Appointment: {appointment_id} has been scheduled with {free_doctor.name}"}






