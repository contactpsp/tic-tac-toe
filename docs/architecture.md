# Project Structure

    tic-tac-toe/
        client/ # contains the web client and user interfaces
            ~game.html # unused game page
            dataTypes.js # contains dictionaries of data like message headers and paths
            game.js # contains the logic of the game
            network.js # handles the websockets and networking of the game
            script.js # handles the webclient logic
            styles.css # contains the necessary data to make the website look and feel responsive
            assets/ # contains the assets of the client
                sounds/ # unused
                ui/ # contains sprites of the user interface
                    profiles/ # contains sprites of user's profile pictures
        docs/ # all of the project documentation
        excercises/ #contains excercises i've done while making the project
        server/ # contains the server backend logic and netcode
            game.py # class that represents/handles a game state (board, turns)
            gameserver.py #unused
            main.py # handles all the logic of the backend simply (rooms, game, connections, players)
            network.py # contains enums of message headers
            player.py # represents the player state (connection, id, cookie, role)
            room.py # represents the room handles players and game state

# How it works

main.py is ran on a websocket server

it polls through connections and handles their messsages

the clients are hosted on a website or webpage, they can connect and send messages to the server,

the server handles all the games and lobbies
while the client handles sending the input and displaying the game state on their screen,

the server is authoritivate meaning the clients cant cheat

# Core Components and Technology

- Python
- WebSockets
- JavaScript
- HTML
- CSS
- Servers

# Frontend (client)

it's built with HTML, CSS and JS that create a simple yet responsive webpage, the client can communicate with the server via websockets to make the tic-tac-toe game come to life,

the clients can input game commands like placing their markers on the game board and create their own little profiles using cookies that allow nicknames and profile pictures

# Backend (server)
 
 it's built using Pythono and Websockets, it has classes that manages players, connections, rooms and games,

 the server receives and broadcasts messages to the clients, the server also has authority over the game state which makes it so much harder for clients to cheat as they only send their inputs and the server calculates and determines the output of them, the server is a bit hardcoded around some bits due to the lack of my experience with networking in python.