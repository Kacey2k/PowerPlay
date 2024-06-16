from enum import Enum

class MapType(Enum):
    ACHIEVEMENT = "achievement"
    ARENA = "arena"
    CTF = "ctf"
    CP = "cp"
    IDLE = "idle"
    JUMP = "jump"
    KOTH = "koth"
    MISC = "misc"
    MVM = "mvm"
    PASS = "pass"
    PL = "pl"
    PLR = "plr"
    PD = "pd"
    RD = "rd"
    SD = "sd"
    TC = "tc"
    TRADE = "trade"
    TR = "tr"
    VSH = "vsh"
    ZI = "zi"

maps = {
    MapType.ACHIEVEMENT: [
        "engineer",
        "idle"
        "idle_awesomebox",
        "idle_sandbox",
    ],
    MapType.ARENA: [
        "badlands",
        "byre",
        "granary",
        "graveyard",
        "lumberyard",
        "nucleus",
        "offblast",
        "perks",
        "ravine",
        "sawmill",
        "watchtower",
        "well"
    ],
    MapType.CTF: [
        "2fort",
        "2fort_Invasion",
        "crasher",
        "double_cross",
        "doublefrost",
        "frosty",
        "haarp",
        "helltrain",
        "landfall",
        "pelican_peak",
        "sawmill",
        "snowfall",
        "turbine",
        "turbine_winter",
        "well"
    ],
    MapType.CP: [
        "5gorge",
        "badlands",
        "coldfront",
        "fastlane",
        "foundry",
        "freight",
        "gorge",
        "granary",
        "gravelpit",
        "industrial",
        "metalworks",
        "mossrock",
        "mountainlab",
        "powerhouse",
        "process",
        "snakewater",
        "standin",
        "steel",
        "sunshine",
        "vanguard",
        "well",
        "woodland"
    ],
    MapType.JUMP: [
        "jump_academy"
    ],
    MapType.KOTH: [
        "badlands",
        "highpass",
        "kongking",
        "lakeside",
        "maple_ridge",
        "moonshine_event",
        "nucleus",
        "probed",
        "ramjam",
        "sawmill",
        "viaduct",
        "vanguard"
    ],
    MapType.MISC: [
        "itemtest"
    ],
    MapType.MVM: [
        "bigrock",
        "coal_town",
        "decoy",
        "ghost_town",
        "mannhattan",
        "rottenburg"
    ],
    MapType.PASS: [
        "pass_brickyard",
        "pass_district",
        "pass_timbertown"
    ],
    MapType.PL: [
        "badwater",
        "barnblitz",
        "bloodwater",
        "borneo",
        "bread_space",
        "brimstone",
        "camber",
        "cashworks",
        "chilly",
        "corruption",
        "emerge",
        "frontier",
        "frostcliff",
        "ghoulpit",
        "gravestone",
        "hassle_castle",
        "hellstone",
        "phoenix",
        "pier",
        "polar",
        "precipice",
        "rumford",
        "snowycoast",
        "spineyard",
        "swiftwater",
        "terror",
        "venice"
    ],
    MapType.PLR: [
        "bananabay",
        "bonesaw",
        "hacksaw",
        "helltower",
        "hightower",
        "nightfall",
        "pipeline"
    ],
    MapType.PD: [
        "cursed_cove_event",
        "farmageddon",
        "galleria",
        "mannsylvania",
        "monster_bash",
        "pit_of_death_event",
        "selbyen",
        "snowville",
        "watergate"
    ],
    MapType.RD: [
        "asteroid"
    ],
    MapType.SD: [
        "doomsday_event",
        "doomsday"
    ],
    MapType.TC: [
        "hydro"
    ],
    MapType.TRADE: [
        "plaza",
        "minecraft_realms_v2",
        "minecraft_realms_final",
        "hopi_plaza",
        "hopi_trade_v2",
        "center_b1"
    ],
    MapType.TR: [
        "aim",
        "dustbowl",
        "target",
        "walkway"
    ],
    MapType.VSH: [
        "distillery",
        "nucleus",
        "skirmish",
        "tinyrock"
    ],
    MapType.ZI: [
        "atoll",
        "devastation",
        "murky",
        "sanitarium",
        "woods"
    ]
}