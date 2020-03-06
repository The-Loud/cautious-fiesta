#   Query methods will be defined here
from models import SourceModel, TargetModel
from hashlib import sha256


def ez_sha(s, encoding='UTF-8'):
    return sha256(s.encode(encoding)).hexdigest()


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

    def grab_columns(self):
        query = self.session.query(self.model_cls)
        source = query.column_descriptions
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

    def grab_columns(self):
        query = self.session.query(self.model_cls)
        target = query.column_descriptions
        return target
