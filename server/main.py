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
                    if code not in rooms.keys():
                        await connection.send(json.dumps({
                            "id": ServerToClientMessageIds.ERROR,
                            "error": "Room not found"
                        }))
                        pass
                    else:
                        room = rooms[code];
                        if(room.isFull()):
                            print("room full")
                            await sendError(connection, "room full")
                            pass
                        elif(room.hostPlayer.connection == connection):
                            await sendError(connection, "you cannot join the same room as you are in...\nah cheeky boy");
                            pass
                        else:
                            myPlayer = Player(connection, str(message["cookie"]), 2, room);
                            room.guestPlayer = myPlayer
                            players[connection] = myPlayer
                            await connection.send(json.dumps({
                                "id": ServerToClientMessageIds.GAME_JOINED,
                                "code": code
                            }))
                            await sendGameStart(room)
                case ClientToServerMessageIds.PLACE_MARK:
                        if connection not in players.keys():
                            pass
                        myPlayer = players[connection];
                        myRoom = myPlayer.room;
                        if myRoom.game.placeMark(myPlayer.role, message["spot"]):
                            match myRoom.game.validateBoard(myPlayer.role):
                                case "Win":
                                    myRoom.status = "complete"
                                    await sendGameEnd(room, json.loads(myPlayer.id)["username"] + "\n got the victory royale")
                                case "Draw":
                                    myRoom.status = "complete"
                                    await sendGameEnd(room, "DRAW!\n get rekt")
                                case _:
                                    await sendUpdateBoard(room)
                        else:
                            await sendError(connection, "invalid move")
                            pass;
                        
        except websockets.exceptions.ConnectionClosed:
            if (connection not in players.keys()):
                pass
            player = players[connection]
            if(player.room.onDisconnect(player)):
                rooms.pop(room.code)
            players.pop(connection)
            await connection.close()
            break;
        except Exception as e:
            print(e)
            pass;
    
    print("Client disconnected", connection.remote_address)

async def startAsync():
    async with websockets.serve(handler, "localhost", 8000):
        print("Server running at ws://localhost:8000")
        await asyncio.Future()

async def sendGameStart(room):
    room.game.board =  [0, 0, 0, 
                       0, 0, 0, 
                       0, 0, 0]
    await sendUpdateBoard(room)
    await room.broadcastGameStart();
    
# await connection.send(json.dumps({"id": ServerToClientMessageIds.GAME_STARTED, "opponent": players[connection].id}))

async def sendError(connection, error):
    await connection.send(json.dumps({"id": ServerToClientMessageIds.ERROR, "error": error}))

async def sendGameEnd(room, winner):
    dump = json.dumps({
        "id": ServerToClientMessageIds.GAME_ENDED,
        "board": room.game.board,
        "status": room.status,
        "winner": winner
    })
    await room.broadcast(dump)

async def sendUpdateBoard(room):
    dump = json.dumps({
        "id": ServerToClientMessageIds.UPDATE_BOARD,
        "board": room.game.board,
        "turn": room.game.turn,
        "status": room.status,
    })
    await room.broadcast(dump)

def start():
    asyncio.run(startAsync())


def CreateRoom(status):
    code = str(uuid.uuid4())[:6]
    if code not in rooms.keys():
        room = Room(code, status)
        rooms[code] = room
        return room
    else:
        return CreateRoom(status)


start();