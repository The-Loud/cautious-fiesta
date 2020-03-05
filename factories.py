import models
import factory
import time


class SourceFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.SourceModel
        sqlalchemy_session_persistence = 'commit'

    id = factory.Sequence(lambda n: '%s' % n)
    created = factory.LazyFunction(lambda: datetime.now(tz=timezone.utc))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.LazyFunction(random_sha)


class TargetFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.TargetModel
        sqlalchemy_session_persistence = 'commit'

    id = factory.Sequence(lambda n: '%s' % n)
    created = factory.LazyFunction(lambda: datetime.now(tz=timezone.utc))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.LazyFunction(random_sha)
