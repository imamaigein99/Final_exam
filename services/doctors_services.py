from schemas.doctors_schema import DoctorsCreate, Doctors, doctors

class DoctorSerivce:


    @staticmethod
    def get_doctor_by_id(id):
        if id in Doctors:
            return Doctors[id]
        else: 
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Does Not Exist"}

    @staticmethod    
    def create_doctors(Doctor_data: DoctorsCreate):
        id = len(doctors)
        doctor = Doctors(
            id=id,
            **Doctor_data.model_dump()            
        )
        Doctors[id] = doctor
        if 1 == 1:
            return {"ResponseCode": "00", "ResponseMessage": "Doctor Successfully Created"}
        else:
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Not Created"}
     