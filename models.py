from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Table
from sqlalchemy import create_engine

engine = create_engine(['DB_URL'])
Base = declarative_base(bind=engine)


class TestModel(Base):
    __table__ = Table('Tests', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRJobsModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')
