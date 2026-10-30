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
    const squares = document.getElementsByClassName("square")
    for (let i = 0; i < squares.length; i++) {
        if(message.board[i] == 0)
            squares[i].innerText = "";
        else if(message.board[i] == 1)
            squares[i].innerText = "X";
        else
            squares[i].innerText = "O";
    }
}

function disableBoard(){
    const squares = document.getElementsByClassName("square")
    for (let i = 0; i < squares.length; i++) {
        squares[i].disabled = true;
        squares[i].ariaDisabled = true
    }
}

function enabledBoard(){
    const squares = document.getElementsByClassName("square")
    for (let i = 0; i < squares.length; i++) {
        squares[i].disabled = false;
        squares[i].ariaDisabled = false;
    }
}