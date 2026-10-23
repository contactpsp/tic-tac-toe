const pfpsList = [
    "BOWSER",
    "DAISY",
    "DK",
    "DRYBONES",
    "LUIGI",
    "MARIO",
    "PEACH",
    "ROB",
    "SHYGUY",
    "TEAMBLUE",
    "TEAMRED",
    "TOAD",
    "WALUIGI",
    "WARIO",
    "YOSHI",
]

const pfps = new Map([
    ["BOWSER", "assets/ui/profiles/MKDSEmblemBowser.png"],
    ["DAISY", "assets/ui/profiles/MKDSEmblemDaisy.webp"],
    ["DK", "assets/ui/profiles/MKDSEmblemDK.png"],
    ["DRYBONES", "assets/ui/profiles/MKDSEmblemDryBones.webp"],
    ["LUIGI", "assets/ui/profiles/MKDSEmblemLuigi.png"],
    ["MARIO", "assets/ui/profiles/MKDSEmblemMario.png"],
    ["PEACH", "assets/ui/profiles/MKDSEmblemPeach.png"],
    ["ROB", "assets/ui/profiles/MKDSEmblemROB.png"],
    ["SHYGUY", "assets/ui/profiles/MKDSEmblemShyGuy.webp"],
    ["TEAMBLUE", "assets/ui/profiles/MKDSEmblemTeamBlue.png"],
    ["TEAMRED", "assets/ui/profiles/MKDSEmblemTeamRed.png"],
    ["TOAD", "assets/ui/profiles/MKDSEmblemToad.png"],
    ["WALUIGI", "assets/ui/profiles/MKDSEmblemWaluigi.webp"],
    ["WARIO", "assets/ui/profiles/MKDSEmblemWario.png"],
    ["YOSHI", "assets/ui/profiles/MKDSEmblemYoshi.png"],
])

const clientToServerMessageIds = {
    CREATE_GAME: 0,
    JOIN_GAME: 1,
    PLACE_MARK: 2,
    REQUEST_REMATCH: 3
}
const serverToClientMessageIds = {
    ERROR: -1,
    GAME_CREATED: 0,
    GAME_JOINED: 1,
    GAME_STARTED: 2,
    UPDATE_BOARD: 3,
    GAME_ENDED: 4.
}