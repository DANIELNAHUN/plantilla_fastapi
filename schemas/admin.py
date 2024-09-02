from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class EmployeeBase(BaseModel):
    id_employee: Optional[int] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    admission_date: Optional[date] = None
    email: Optional[str] = None
    position_id: Optional[int] = None
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    id_user: Optional[int] = None
    username: Optional[str] = None
    userpassword: Optional[str] = None
    id_employee: Optional[int] = None
    class Config:
        orm_mode = True