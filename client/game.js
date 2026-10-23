function place(spot){
    const message = {
        id: clientToServerMessageIds.PLACE_MARK,
        spot: spot
    }
    console.log("Placing at" + spot);
    websocket.send(JSON.stringify(message))
}

function updateBoard(message){
    console.log(message);
}