from schemas.doctors_schema import DoctorsCreate, Doctors, doctors

class DoctorSerivce:


    @staticmethod
    def get_doctor_by_id(id):
        if id in doctors:
            return doctors[id]
        else: 
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Does Not Exist"}


    @staticmethod
    def create_doctors(Doctor_data: DoctorsCreate):
        # Check if the phone number already exists
        for doctor_id, doctor in doctors.items():
            if doctor.phone == Doctor_data.phone:
                return {"ResponseCode": "01", "ResponseMessage": "Doctor with the same msisdn already exists"}
        
        new_id = max(doctors.keys(), default=0) + 1

        # If the phone number does not exist, create a new doctor
        id = len(doctors)
        doctor = Doctors(
            id=new_id,
            **Doctor_data.model_dump()
        )
        doctors[id] = doctor

        return {"ResponseCode": "00", "ResponseMessage": "Doctor Created Successfully"}

    @staticmethod
    def update_doctors_status_busy(id):
        # Check if the doctor exists in the dictionary
        if id in doctors:
            # Access the doctor object using the id
            doctor = doctors[id]
        
            # Check the current status of the doctor
            if doctor.status == "FREE":
                # Update the status to "BUSY"
                doctor.status = "BUSY"
                return {"ResponseCode": "00", "ResponseMessage": "Doctor Status Updated Successfully"}
            elif doctor.status == "BUSY":
                return {"ResponseCode": "02", "ResponseMessage": "Doctor Already in Busy state"}
        else:
            # If the doctor does not exist in the dictionary
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Does Not Exist"}

        # If the code reaches this point, it indicates an internal logic issue
        return {"ResponseCode": "03", "ResponseMessage": "Internal Logic issue"}
    

    @staticmethod
    def update_doctors_status_free(id):
        # Check if the doctor exists in the dictionary
        if id in doctors:
            # Access the doctor object using the id
            doctor = doctors[id]
        
            # Check the current status of the doctor
            if doctor.status == "BUSY":
                # Update the status to "BUSY"
                doctor.status = "FREE"
                return {"ResponseCode": "00", "ResponseMessage": "Doctor Status Updated Successfully"}
            elif doctor.status == "FREE":
                return {"ResponseCode": "02", "ResponseMessage": "Doctor Already in Free state"}
        else:
            # If the doctor does not exist in the dictionary
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Does Not Exist"}

        # If the code reaches this point, it indicates an internal logic issue
        return {"ResponseCode": "03", "ResponseMessage": "Internal Logic issue"}



    # @staticmethod
    # def delete_doctors_by_id(id):
    # # Check if the Doctor ID exists
    #     if id in doctors:
    #         # Delete the doctor with the provided ID
    #         del doctors[id]
    #         return {"ResponseCode": "00", "ResponseMessage": "Doctor Deleted Successfully"}
    #     else:
    #         return {"ResponseCode": "01", "ResponseMessage": "Doctor with ID does not exist"}
