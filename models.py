from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table
from sqlalchemy import create_engine

DB_ENG_STR = ''
engine = create_engine(DB_ENG_STR)
Base = declarative_base(bind=engine)

#   Set global variables here
schema = 'SCHEMANAME'
source_table = 'Changeme_source'
target_table = 'Changeme_target'


#   Use SQLAlchemy Reflection to pull back table metadata
class SourceModel(Base):
    '''The source table base. This is used to pull meta from the DB.'''
    __table__ = Table(source_table, Base.metadata, autoload=True, autoload_with=engine, schema=schema)


class TargetModel(Base):
    '''Target table base. Initalizes table and column objects based on the
       metadata from the DB.'''
    __table__ = Table(target_table, Base.metadata, autoload=True, autoload_with=engine, schema=schema)


'''
class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')
'''
