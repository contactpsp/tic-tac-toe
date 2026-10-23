const wsUri = "ws://localhost:8000/"
const websocket = new WebSocket(wsUri)
websocket.onopen = function (event) {
    console.log(event);
    //alert("A WebSocket has been opened :) you may proceed")
}
websocket.onclose = function (event) {
    console.log(event)
    alert("A WebSocket Closed :/ Try Refreshing the Page")
}
websocket.onerror = function (event){
    console.log(event)
    alert("A WebSocket Error Occured :/ Try Refreshing the Page")
}
websocket.onmessage = function (event) {
    var message = JSON.parse(event.data)
    console.log("Received from server:", message)
    switch (message.id) {
        case serverToClientMessageIds.GAME_CREATED:
            console.log("Game created with code:", message.code)
            alert("Created game\n" + message.code + "\nJOIN LINK:\n" + document.URL + "?code=" + message.code)
            break;
        case serverToClientMessageIds.GAME_JOINED:
            console.log("Joined game with code:", message.code)
            alert("Joined game\n" + message.code + "\nJOIN LINK:\n" + document.URL + "?code=" + message.code)
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
            alert("GAME HAS ENDED")
            break;
        case serverToClientMessageIds.ERROR:
            console.error("Error from server:", message.error)
            alert("Error from server :/\n"+message.error)
            //window.location.href = "index.html"
            //alert("error from server :/")
            break;
    }
}
