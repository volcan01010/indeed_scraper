"""
SQLAlchemy model schemas for data items

This file describes a flat schema for the Indeed Job spec, as created from the
webpages.  This is used for passing data forward via queues to be enhanced. A
more normalised schema could be used for the final data store.  For example:

+ Making job types, licence, work-remotely, benefits come from different
  tables allows constraint of values and defining a one-to-many relationship.
+ Making company an external table allows company data to be joined with other
  job information.
+ A normalised location makes it easier to search for jobs in the same town.

These features aren't necessary at this point and are best implemented at the
final database storage step.  If the fields are likely to be used only in full
text searches, it may not even be necessary to normalise them.
"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

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
    fetched_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<IndeedJob(job_key={self.job_key})>"


class IndeedJobSpecSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = IndeedJobSpec
        include_relationships = True
        load_instance = True
