import json

from game import Game
from player import Player
from websockets.protocol import CLOSED, OPEN
from network import ServerToClientMessageIds

class Room:
    def __init__(self, _code, _status):
        self.code = _code
        self.status = _status
        self.hostPlayer = Player(None, None, None, None)
        self.guestPlayer = Player(None, None, None, None)
        self.game = Game()
        self.rematch = 0

    def getOppositePlayer(self, player):
        if player.isHost():
            return self.guestPlayer;
        else: 
            return self.hostPlayer;

    def getPlayer(self, player):
        if player.isHost():
            return self.hostPlayer;
        else:
            return self.guestPlayer;

    # Handles the player disconnecting
    # If it returns true, the room is disposed
    def onDisconnect(self, player):
        if(self.isFull()):
            if(player.isHost()):
                self.hostPlayer = self.guestPlayer
        else:
            self.hostPlayer.connection = None
            self.hostPlayer = None
        self.guestPlayer.connection = None
        self.guestPlayer = None
        return self.hostPlayer == None and self.guestPlayer == None
    
    def isFull(self):
        return self.hostPlayer.connection != None and self.guestPlayer.connection != None

    async def broadcast(self, message):
        await self.hostPlayer.connection.send(message);
        await self.guestPlayer.connection.send(message);

    async def broadcastGameStart(self):
        await self.hostPlayer.connection.send(json.dumps({"id": ServerToClientMessageIds.GAME_STARTED, "opponent": self.guestPlayer.id}))
        await self.guestPlayer.connection.send(json.dumps({"id": ServerToClientMessageIds.GAME_STARTED, "opponent": self.hostPlayer.id}))
