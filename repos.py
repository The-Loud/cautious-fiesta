#   Query methods will be defined here
from models import SourceModel, TargetModel

class SourceRepository:
    model_cls = SourceModel

    def __init__(self, session):
        self.session = session

    def authenticate(self, email, password):
        query = self.session.query(self.model_cls)
        query = query.filter(self.model_cls.email == email)
        query = query.filter(self.model_cls.password == ez_sha(password))

        return query.one_or_none()

    def change_name(self, user_id, first_name, last_name):
        query = self.session.query(self.model_cls)
        query = query.filter(self.model_cls.id == user_id)
        query = query.with_for_update()
        source = query.one()

        source.first_name = first_name
        source.last_name = last_name

        self.session.flush()

        return source


class TargetRepository:
    model_cls = TargetModel

    def __init__(self, session):
        self.session = session

    def authenticate(self, email, password):
        query = self.session.query(self.model_cls)
        query = query.filter(self.model_cls.email == email)
        query = query.filter(self.model_cls.password == ez_sha(password))

        return query.one_or_none()

    def change_name(self, user_id, first_name, last_name):
        query = self.session.query(self.model_cls)
        query = query.filter(self.model_cls.id == user_id)
        query = query.with_for_update()
        target = query.one()

        target.first_name = first_name
        target.last_name = last_name

        self.session.flush()

        return target
