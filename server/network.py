from enum import IntEnum

class ClientToServerMessageIds(IntEnum):
    CREATE_GAME = 0,
    JOIN_GAME = 1,
    PLACE_MARK = 2,
    REQUEST_REMATCH = 3,
    DISCONNECT = 4,

class ServerToClientMessageIds(IntEnum):
    ERROR = -1,
    GAME_CREATED = 0,
    GAME_JOINED = 1,
    GAME_STARTED = 2,
    UPDATE_BOARD = 3,
    GAME_ENDED = 4,