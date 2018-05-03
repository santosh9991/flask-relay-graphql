from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base
import os
engine = create_engine(
        os.getenv('localdb'),
        convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class EmployeeModel(Base):
    """This model describes the
     CPU data of AT&T devices"""
    __tablename__ = 'employee'# representation of table inside database
    employee_id = Column(Integer,nullable=False,primary_key=True)
    first_name = Column(Unicode,nullable=False)
    last_name = Column(Unicode,nullable=False)
    department_id = Column(Integer,
        ForeignKey('department.department_id'),nullable=False)
    # department_id = Column(Integer,nullable=False)
    # hardwares = relationship('HardwareModel',
    #     backref='hardware',lazy=True)

class DepartmentModel(Base):
    __tablename__ = 'department'
    department_id = Column(Integer,nullable=False,primary_key=True)
    department_name = Column(Unicode,nullable=False)
