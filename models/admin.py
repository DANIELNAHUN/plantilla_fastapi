from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Date, Float

from config.db import Base

class Employee(Base):
    __tablename__ = "employees"

    id_employee = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    last_name = Column(String(255))
    admission_date = Column(Date)
    email = Column(String(255))
    position_id = Column(Integer, ForeignKey("positions.id"))
    at_created = Column(DateTime)
    at_updated = Column(DateTime)
    at_deleted = Column(DateTime)

class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    userpassword = Column(Text)
    id_employee = Column(Integer, ForeignKey("employees.id_employee"))
    at_created = Column(DateTime)
    at_updated = Column(DateTime)
    at_deleted = Column(DateTime)

class Position(Base):
    __tablename__ = "positions"

    id_position = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    salary = Column(Float)
    at_created = Column(DateTime)
    at_updated = Column(DateTime)
    at_deleted = Column(DateTime)