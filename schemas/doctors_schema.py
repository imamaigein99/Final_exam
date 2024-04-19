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
        id=0, name='Dr Raji Victor', specialization='GP 1', phone='07066296434',status= 'FREE', active='ENABLED'),
    1: Doctors(
        id=1, name='Dr Precious Ugochi', specialization='GP 2', phone='08023020252', status='FREE', active='ENABLED'),
    2: Doctors(
        id=2, name='Dr Curtis Jackson', specialization='GP 3', phone='080372600006',status='FREE', active='ENABLED')
}