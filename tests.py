import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from factories import SourceFactory, TargetFactory
from models import SourceModel, TargetModel
from getpass import getpass

PASSWORD = getpass('Enter your password: ')


DB_ENG_STR = 'oracle+cx_oracle://UHG_001271993:' + PASSWORD + '@AAPPR03 = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = ep05)(PORT = 1521))(CONNECT_DATA = (SERVER = DEDICATED)(SERVICE_NAME = aappr03svc.uhc.com)))'
engine = create_engine('DB_ENG_STR')
Session = sessionmaker()

#   Create a clean connection for the duration of the entire script
@pytest.fixture(scope='module')
def connection():
    '''One connection per run of module'''
    connection = engine.connect()
    yield connection
    connection.close()

#   Create a session for each test run
@pytest.fixture(scope='function')
def session(connection):
    '''We need to ensure that there is a fresh session per test run'''
    transaction = connection.begin()
    session = Session(bind=connection)

    SourceFactory._meta.sqlalchemy_session = session
    TargetFactory._meta.sqlalchemy_session = session

    yield session
    session.close()
    transaction.rollback()


@pytest.fixture
def source(session):
    return SourceRepository(session)


@pytest.fixture
def target(session):
    return TargetRepository(session)


#   Begin tests here

def test_tables_exist(connection, source, target):
    '''Sanity check'''
    assert connection.has_table('source_table_name', schema='schemaname')
    assert connection.has_table('target_table_name', schema='schemaname')


def test_row_counts(session, source, target):
    '''Takes in two tables and determines row counts between them'''
    assert session.query(TargetModel).count() == session.query(SourceModel).count()


def test_empty_tables(session, source, target):
    pass
