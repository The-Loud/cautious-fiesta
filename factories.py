from . import models
import factory

class TestFactory(factory.sqlalchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.TestModel
        sqlalchemy_session = session
