const wsUri = "ws://localhost:8000/"
const websocket = new WebSocket(wsUri)
websocket.onopen = function (event) {
    console.log(event);
}
websocket.onclose = function (event) {
    console.log(event)
}
websocket.onerror = function (event){
    console.log(event)
}
websocket.onmessage = function (event) {
    var message = JSON.parse(event.data)
    console.log("Received from server:", message)
    switch (message.id) {
        case serverToClientMessageIds.GAME_CREATED:
            console.log("Game created with code:", message.code)
            break;
        case serverToClientMessageIds.GAME_JOINED:
            console.log("Joined game with code:", message.code)
            break;
        case serverToClientMessageIds.GAME_STARTED:
            console.log("GAME HAS STARTED");
            document.getElementById("op-u").innerText = message.opponent.username
            document.getElementById("op-pfp").src = pfps.get(message.opponent.pfp);
            break;
        case serverToClientMessageIds.UPDATE_BOARD:
            console.log("Board has been updated: ", event.data)
            updateBoard(message)
            break;
        case serverToClientMessageIds.GAME_ENDED:
            break;
        case serverToClientMessageIds.ERROR:
            console.error("Error from server:", message.error)
            window.location.href = "index.html"
            break;
    }
}
