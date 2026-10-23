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
    websocket.send(JSON.stringify(message));
}

function GetGameCode() {
    return document.getElementById("gamecode").value;
}

function JoinGame() {
    JoinGameWithCode(GetGameCode())
}

function JoinGameWithCode(code) {
    var message = {
        id: clientToServerMessageIds.JOIN_GAME,
        cookie: cookie,
        code: code,
    }
    websocket.send(JSON.stringify(message));
}

function Save() {
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
    alert("saved")
    UpdateHTML(true);
}

function Load() {
    cookie = document.cookie;
    if(cookie.length <  1 || document.cookie.length < 1) {
        username = "cookie"
        pfp = "TEAMRED"
        UpdateHTML(true);
        Save();
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