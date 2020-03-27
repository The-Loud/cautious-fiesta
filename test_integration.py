import pytest
# from factories import SourceFactory, TargetFactory
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

    # SourceFactory._meta.sqlalchemy_session = session
    # TargetFactory._meta.sqlalchemy_session = session

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
def test_tables_exist(connection):
    '''Sanity check'''
    assert connection.dialect.has_table(connection,
                                        table_name=source_table) is not None
    assert connection.dialect.has_table(connection,
                                        table_name=target_table) is not None


def test_row_counts(session, source, target):
    '''Takes in two tables and determines row counts between them'''
    assert source.zero_records() == target.zero_records()


def test_empty_tables(session, source, target):
    assert source.zero_records() == 0 == target.zero_records()


def test_col_match(session):
    '''Verifies that the column values are the same in each table'''
    assert SourceModel.__table__.columns.keys() == TargetModel.__table__.columns.keys()


def test_val_match(session, source, target):
    '''Verifies that the column values are the same in each table'''
    for s, t in zip(source.all_records(), target.all_records()):
        assert s == t


'''
    for s in source.all_records():
        for t in target.all_records():
            assert s == t
'''
