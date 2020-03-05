import pytest
from factories import SourceFactory, TargetFactory
from repos import SourceRepository, TargetRepository
from models import SourceModel, TargetModel
from connection import Session, DB_ENG


#   Create a clean connection for the duration of the entire script
@pytest.fixture(scope='module')
def connection():
    '''One connection per run of module'''
    connection = DB_ENG['sql'].connect()
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
    assert connection.dialect.has_table(connection, table_name='accounts')
    assert connection.dialect.has_table(connection, table_name='transactions')


def test_row_counts(session, source, target):
    '''Takes in two tables and determines row counts between them'''
    assert session.query(TargetModel).count() == session.query(SourceModel).count()


def test_empty_tables(session, source, target):
    pass
