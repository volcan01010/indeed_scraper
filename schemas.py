"""SQLAlchemy model schemas for data items"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class IndeedJobSpec(Base):
    __tablename__ = 'indeed_job_specs'

    job_key = Column(String, primary_key=True)
    description = Column(String)

    def __repr__(self):
        return f"<IndeedJob(job_key={self.job_key})>"


class IndeedJobSpecSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = IndeedJobSpec
        include_relationships = True
        load_instance = True
