import models
import factory
from datetime import datetime, timezone
from uuid import uuid4
from repos import ez_sha


def random_sha():
    return ez_sha(str(uuid4()))


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
