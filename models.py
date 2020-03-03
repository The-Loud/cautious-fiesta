from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Table
from sqlalchemy import create_engine

engine = create_engine(['DB_URL'])
Base = declarative_base(bind=engine)

#   Set global variables here
schema='RR_JOBS'
source_table = 'Changeme_source'
target_table = 'Changeme_target'

#   Use SQLAlchemy Reflection to pull back table metadata

class SourceModel(Base):
    __table__ = Table(source_table, Base.metadata, autoload=True, autoload_with=engine, schema=schema)


class TargetModel(Base):
    __table__ = Table(target_table, Base.metadata, autoload=True, autoload_with=engine, schema=schema)

'''
class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')
'''
