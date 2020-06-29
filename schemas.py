"""SQLAlchemy model schemas for data items"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class IndeedJobSpec(Base):
    """Model for Indeed job specification."""
    __tablename__ = 'indeed_job_specs'

    job_key = Column(String, primary_key=True)
    summary = Column(String)
    duties = Column(String)
    job_types = Column(String)
    salary = Column(String)
    benefits = Column(String)
    experience = Column(String)
    licence = Column(String)
    work_remotely = Column(String)

    def __repr__(self):
        return f"<IndeedJob(job_key={self.job_key})>"


class IndeedJobSpecSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = IndeedJobSpec
        include_relationships = True
        load_instance = True
