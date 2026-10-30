const wsUri = "ws://localhost:8000/"
const websocket = new WebSocket(wsUri)
var inviteCode = "";
var inviteURL = "";
websocket.onopen = function (event) {
    console.log(event);
    //alert("A WebSocket has been opened :) you may proceed")
    if (params.has("code")) {
        console.log(params.get("code"))
        JoinGameWithCode(params.get("code"))
    }
}
websocket.onclose = function (event) {
    console.log(event)
    //alert("A WebSocket Closed :/ Try Refreshing the Page")
}
websocket.onerror = function (event){
    console.log(event)
    //alert("A WebSocket Error Occured :/ Try Refreshing the Page")
}
websocket.onmessage = function (event) {
    var message = JSON.parse(event.data)
    console.log("Received from server:", message)
    switch (message.id) {
        case serverToClientMessageIds.GAME_CREATED:
            inviteCode = message.code;
            inviteURL = document.URL + "?code=" + message.code;
            console.log("Game created with code:", inviteCode)
            alert("Created game\n" + inviteCode+ "\nJOIN LINK:\n" + inviteURL)
            break;
        case serverToClientMessageIds.GAME_JOINED:
            inviteCode = message.code;
            inviteURL = document.URL + "?code=" + message.code;
            console.log("Joined game with code:", inviteCode)
            alert("Joined game\n" + inviteCode + "\nJOIN LINK:\n" + inviteURL)
            break;
        case serverToClientMessageIds.GAME_STARTED:
            console.log("GAME HAS STARTED");
            var opponent = JSON.parse(message.opponent);
            document.getElementById("op-u").innerText = opponent["username"]
            document.getElementById("op-pfp").src = pfps.get(opponent["pfp"]);
            alert("GAME HAS STARTED!\nYour opponent is\n" + opponent["username"]);
            break;
        case serverToClientMessageIds.UPDATE_BOARD:
            console.log("Board has been updated: ", event.data)
            updateBoard(message)
            break;
        case serverToClientMessageIds.GAME_ENDED:
            updateBoard(message)
            var rematch = confirm("GAME HAS ENDED!\n" + message.winner + "\n Rematch?")
            if(!rematch){
                window.location.href = "index.html"
            }
            websocket.send(JSON.stringify({id:clientToServerMessageIds.REQUEST_REMATCH, rematch: rematch}));
            break;
        case serverToClientMessageIds.ENABLE_BOARD:
            enabledBoard()
            break;
        case serverToClientMessageIds.DISABLE_BOARD:
            disableBoard()
            break;
        case serverToClientMessageIds.ERROR:
            console.error("Error from server:", message.error)
            alert("Error from server :/\n"+message.error)
            //window.location.href = "index.html"
            //alert("error from server :/")
            break;
    }
}
