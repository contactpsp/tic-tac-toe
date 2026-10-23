class Player:
    def __init__(self, _connection, _id, _role, _room):
        self.connection = _connection
        self.id = str(_id)
        self.role = _role
        self.room = _room
        self.isValid = False

    def isHost(self):
        return self.room.hostPlayer == self