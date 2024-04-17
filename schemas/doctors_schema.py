from pydantic import BaseModel
from enum import Enum

class is_available(str, Enum):
    OPEN = "FREE"
    CLOSED = "BUSY"

class DoctorsStatus(str, Enum):
    OPEN = "ENABLED"
    CLOSED = "DISABLED"

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    status: is_available = is_available.OPEN
    active: DoctorsStatus = DoctorsStatus.OPEN


class DoctorsCreate(BaseModel):
    name: str
    specialization: str
    phone: str
    status: is_available = is_available.OPEN
    active: DoctorsStatus = DoctorsStatus.OPEN


class DoctorsUpdate(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str


doctors: dict[int, Doctors] = {
    0: Doctors(
        id=0, name='Kunle Elusade', specialization='', phone='08068632113',status= 'FREE', active='ENABLED'),
    1: Doctors(
        id=1, name='Imama Igein', specialization='', phone='08068632113', status='FREE', active='ENABLED'),
    2: Doctors(
        id=2, name='Curtis Jackson', specialization='', phone='08068632113',status='FREE', active='ENABLED')
}