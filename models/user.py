import uuid


class User:
    def __init__(self, name):
        self._id = uuid.uuid4()
        self._name = name
        self._email = None
        self._phone = None

    def set_id(self, user_id):
        self._id = user_id
        return True

    def get_id(self):
        return self._id

    def set_name(self, name):
        self._name = name
        return True

    def get_name(self):
        return self._name
