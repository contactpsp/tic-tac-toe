import asyncio
import websockets
import json
import uuid

from network import ClientToServerMessageIds, ServerToClientMessageIds
from room import Room
from player import Player
rooms = {}
players = {}
async def handler(connection):
    print("Client connected", connection.remote_address)
    players[connection] = (Player)
    while True:
        try:
            data = await connection.recv()
            print("Received from client:", data)
            message = json.loads(data)
            match message["id"]:
                case ClientToServerMessageIds.CREATE_GAME:
                    print("Client requested to create a game:", message["cookie"])
                    room = CreateRoom("waiting")
                    myPlayer =  Player(connection, message["cookie"], 1, room)
                    room.hostPlayer = myPlayer
                    players[connection] = myPlayer;
                    await connection.send(json.dumps({
                        "id": ServerToClientMessageIds.GAME_CREATED,
                        "code": room.code
                    }))
                    print("Created Room with", room.code)
                case ClientToServerMessageIds.JOIN_GAME:
                    print("Client requested to join a game:", message["cookie"], "with code:", message["code"])
                    code = message["code"]
                    if code not in rooms:
                        await connection.send(json.dumps({
                            "id": ServerToClientMessageIds.ERROR,
                            "message": "Room not found"
                        }))
                        pass
                    room = rooms[code];
                    myPlayer = Player(connection, message["cookie"], 2, room);
                    room.guestPlayer = myPlayer
                    players[connection] = myPlayer
                    await connection.send(json.dumps({
                        "id": ServerToClientMessageIds.GAME_JOINED,
                        "otherPlayer": room.hostPlayer.id,
                        "code": code
                    }))
                case ClientToServerMessageIds.PLACE_MARK:
                        myPlayer = players[connection];
                        myRoom = myPlayer.room;
                        if myRoom.game.canPlay(myPlayer.role):
                            myRoom.game.placeMark(myPlayer.role, message["spot"]);
                        if(myRoom.game.validateBoard(myPlayer.role)):
                            myRoom.status = "complete"
                        await sendUpdateBoard(room);

                        
        except Exception as e:
            print(e)
            # await connection.send(json.dumps({
            #                             "id": ServerToClientMessageIds.ERROR,
            #                             "message": "Room not found"
            #                         }))
            players[connection] = None
            await connection.close()
            break;
    print("Client disconnected", connection.remote_address)

async def startAsync():
    async with websockets.serve(handler, "localhost", 8000):
        print("Server running at ws://localhost:8000")
        await asyncio.Future()

async def sendUpdateBoard(room):
    dump = json.dumps({
        "id": ServerToClientMessageIds.UPDATE_BOARD,
        "board": room.game.board,
        "turn": room.game.turn,
        "status": room.status,
        "host": room.hostPlayer.id,
        "guest": room.guestPlayer.id,
    })
    await room.hostPlayer.connection.send(dump);
    await room.guestPlayer.connection.send(dump);

def start():
    asyncio.run(startAsync())


def  CreateRoom(status):
    code = str(uuid.uuid4())[:6]
    if code not in rooms:
        room = Room(code, status)
        rooms[code] = room
        return room
    else:
        return CreateRoom(status)


start();