from pydantic import BaseModel
from enum import Enum

class is_available(str, Enum):
    OPEN = "True"
    CLOSED = "False"


class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    status: is_available = is_available.OPEN


class DoctorsCreate(BaseModel):
    name: str
    specialization: str
    phone: str
    status: is_available = is_available.OPEN


Doctors: dict[int, Doctors] = {
    0: Doctors(
        id=1, name='Kunle Elusade', specialization='', phone='08068632113',status= 'True' ),
    1: Doctors(
        id=2, name='Imama Igein', specialization='', phone='08068632113', status= 'True'),
    2: Doctors(
        id=3, name='Curtis Jackson', specialization='', phone='08068632113',status='True' )
}