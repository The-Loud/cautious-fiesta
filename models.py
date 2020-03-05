from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table
from connection import DB_ENG


Base = declarative_base(bind=DB_ENG['sql'])

#   Set global variables here
schema = 'pybudget'
source_table = 'accounts'
target_table = 'transactions'


#   Use SQLAlchemy Reflection to pull back table metadata
class SourceModel(Base):
    '''The source table base. This is used to pull meta from the DB.'''
    __table__ = Table(source_table, Base.metadata, autoload=True, autoload_with=DB_ENG['sql'], schema=schema)


class TargetModel(Base):
    '''Target table base. Initalizes table and column objects based on the
       metadata from the DB.'''
    __table__ = Table(target_table, Base.metadata, autoload=True, autoload_with=DB_ENG['sql'], schema=schema)


'''
class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')
'''
