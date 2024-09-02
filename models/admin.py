from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Text, DateTime, Date, Float

from config.db import Base

class Position(Base):
    __tablename__ = "positions"

    id_position = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    description = Column(Text)
    salary = Column(Float)
    active = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    created_by = Column(Integer, ForeignKey("users.id_user"))
    updated_by = Column(Integer, ForeignKey("users.id_user"))
    deleted_by = Column(Integer, ForeignKey("users.id_user"))

class Employee(Base):
    __tablename__ = "employees"

    id_employee = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    last_name = Column(String(250))
    admission_date = Column(Date)
    email = Column(String(250))
    position_id = Column(Integer, ForeignKey("positions.id"))
    active = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    created_by = Column(Integer, ForeignKey("users.id_user"))
    updated_by = Column(Integer, ForeignKey("users.id_user"))
    deleted_by = Column(Integer, ForeignKey("users.id_user"))

class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String(250))
    userpassword = Column(Text)
    employee_id = Column(Integer, ForeignKey("employees.id_employee"))
    active = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    created_by = Column(Integer, ForeignKey("users.id_user"))
    updated_by = Column(Integer, ForeignKey("users.id_user"))
    deleted_by = Column(Integer, ForeignKey("users.id_user"))
