from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String
from connection import DB_ENG



#   Set global variables here
con = 'orc'
schema = 'RR_REG_FM'
source_table = 'VA_FACT_MAP_202002'
target_table = 'Va_Fact_Map_202002_prd'


Base = declarative_base(bind=DB_ENG[con])

#   Use SQLAlchemy Reflection to pull back table metadata
class SourceModel(Base):
    '''The source table base. This is used to pull meta from the DB.'''
    __table__ = Table(source_table, Base.metadata,
                Column('concat_pk', String, primary_key=True),
                autoload=True, extend_existing=True, autoload_with=DB_ENG[con], schema=schema)


class TargetModel(Base):
    '''Target table base. Initalizes table and column objects based on the
       metadata from the DB.'''
    __table__ = Table(source_table, Base.metadata,
                Column('concat_pk', String, primary_key=True),
                autoload=True, extend_existing=True, autoload_with=DB_ENG[con], schema=schema)


'''
class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')


class StgRRRegModel(Base):
    __table__ = Table('stg_rr_jobs', Base.metadata, autoload=True, autoload_with=engine, schema='rr_jobs')
'''
