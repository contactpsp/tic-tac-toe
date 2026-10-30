var profile = 0;
var cookie = document.cookie;
var username = "cookie";
var pfp = "TEAMRED"
let params = new URLSearchParams(document.location.search);

function Start() {
    pfps.keys().forEach(key => {
        var option = document.createElement("option");
        option.text = key;
        document.getElementById("pfp").add(option);
    });
    
    Load();
    if (params.has("code")) {
        JoinGame(params.get("code"))
    }
}

function CreateGame() {
    var message = {
        id: clientToServerMessageIds.CREATE_GAME,
        cookie: cookie
    }
    console.log("creating game")
    websocket.send(JSON.stringify(message));
}

function GetGameCode() {
    console.log("getting game code")
    return document.getElementById("gamecode").value;
}

function JoinGame() {
    console.log("Joining game")
    JoinGameWithCode(GetGameCode())
}

function LeaveGame(){
    var message = {
        id: clientToServerMessageIds.DISCONNECT,
    }
    websocket.send(JSON.stringify(message));
}

function JoinGameWithCode(code) {
    console.log("joining game with " + code)
    var message = {
        id: clientToServerMessageIds.JOIN_GAME,
        cookie: cookie,
        code: code,
    }
    websocket.send(JSON.stringify(message));
}

function Save(canAlert = false) {
    console.log("saving cookies")
    var temp1 = String(document.getElementById("username").value);
    if (temp1.length < 3 && temp1.length > 16) {
        console.error("invalid name");
        alert("invalid name")
        return;
    }
    pfp = document.getElementById("pfp").value;
    username = temp1;
    cookie = JSON.stringify({ username: username, pfp: pfp })
    document.cookie = cookie
    if(canAlert)alert("Account Details Saved")
    UpdateHTML(true);
}

function Load() {
    console.log("loading cookies")
    cookie = document.cookie;
    if(cookie.length <  1 || document.cookie.length < 1) {
        username = "cookie"
        pfp = "TEAMRED"
        UpdateHTML(true);
        Save(false);
        return;
    }
    json = JSON.parse(cookie);
    username = json["username"]
    pfp = json["pfp"]
    UpdateHTML(true);
}

function UpdateHTML(updateCrucial = false){
    if(updateCrucial){
        document.getElementById("username").value = username;
        document.getElementById("pfp").value = pfp;
    }
    document.getElementById("mepfp").src = pfps.get(pfp);
    document.getElementById("me").innerText = username;
}

function RandomRange(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}