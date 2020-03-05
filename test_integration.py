import pytest
#from factories import SourceFactory, TargetFactory
from repos import SourceRepository, TargetRepository
from models import SourceModel, TargetModel, source_table, target_table
from connection import Session, DB_ENG


#   Create a clean connection for the duration of the entire script
@pytest.fixture(scope='module')
def connection():
    '''One connection per run of module'''
    connection = DB_ENG['orc'].connect()
    yield connection
    connection.close()

#   Create a session for each test run
@pytest.fixture(scope='function')
def session(connection):
    '''We need to ensure that there is a fresh session per test run'''
    transaction = connection.begin()
    session = Session(bind=connection)

    #SourceFactory._meta.sqlalchemy_session = session
    #TargetFactory._meta.sqlalchemy_session = session

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
    assert connection.dialect.has_table(connection, table_name=source_table)
    assert connection.dialect.has_table(connection, table_name=target_table)


def test_row_counts(session, source, target):
    '''Takes in two tables and determines row counts between them'''
    assert session.query(TargetModel).count() == session.query(SourceModel).count()


def test_empty_tables(session, source, target):
    pass


def test_col_match(session, source, target):
    '''Verifies that the column values are the same in each table'''
    assert source.get_columns() == target.get_columns()

'''
    assert chosen_one.first_name != user.first_name
    assert chosen_one.last_name != user.last_name
    retrieved = session.query(UserModel).get(chosen_one.id)
    assert new_first_name == retrieved.first_name
    assert new_last_name == retrieved.last_name
    assert count == session.query(UserModel).count()
'''
