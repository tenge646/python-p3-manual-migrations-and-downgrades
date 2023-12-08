import os
import sys

sys.path.append(os.getcwd())


from datetime import datetime

from sqlalchemy import create_engine, desc
from sqlalchemy import (CheckConstraint, UniqueConstraint,
    Column, DateTime, Integer, String)

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    class Student(Base):
     __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    grade = Column(Integer)  # Renaming 'age' column to 'grade'
    date_of_birth = Column(Date)
    email = Column(String(100))
    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"
