import gzip_homm3
import shutil

from sys import argv

dicItems = {
    # Artifacts
    "07": "Centaur's axe",
    "08": "Blackshard of the dead knight",
    "09": "Greater Gnoll's Flail",
    "0A": "Ogre's club of havoc",
    "0B": "Sword of Hellfire",
    "0C": "Titan's gladius",
    "0D": "Shield of the dwarven lords",
    "0E": "Shield of the yawning dead",
    "0F": "Buckler of the gnoll king",
    "10": "Targ of the rampaging ogre",
    "11": "Shield of the dammed",
    "12": "Sentinel's Shield",
    "13": "Helm of the alabaster unicorn",
    "14": "Skull helmet",
    "15": "Helm of chaos",
    "16": "Crown of the supreme magi",
    "17": "Hellstorm helmet",
    "18": "Thunder helmet",
    "19": "Beastplate of petrified wood",
    "1A": "Rib cage",
    "1B": "Scales of the greater basilisk",
    "1C": "Tunic of the cyclops king",
    "1D": "Breastplate of brimstone",
    "1E": "Titan's cuirass",
    "1F": "Armor of wonder",
    "20": "Sandals of the saint",
    "21": "Celestial necklace of bliss",
    "22": "Lion's shield of courage",
    "23": "Sword of judgement",
    "24": "Helm of heavenly enlightenment",
    "25": "Quiet eye of the dragon",
    "26": "Red dragon flame tongue",
    "27": "Dragon scale shield",
    "28": "Dragon scale armor",
    "29": "Dragonbone greaves",
    "2A": "Dragon wing tabard",
    "2B": "Necklace of dragonteeth",
    "2C": "Crown of dragontooth",
    "2D": "Still eye of the dragon",
    "2E": "Clover of fortune",
    "2F": "Cards of prophecy",
    "30": "Ladybird of luck",
    "31": "Badge of courage",
    "32": "Crest of valor",
    "33": "Glyph of gallantry",
    "34": "Speculum",
    "35": "Spyglass",
    "36": "Amulet of the undertaker",
    "37": "Vampire's cowl",
    "38": "Dead men's boots",
    "39": "Garniture of interference",
    "3A": "Surcoat of counterpoise",
    "3B": "Boots of polarity",
    "3C": "Bow of elven cherrywood",
    "3D": "Bowstring of the unicorns's mane",
    "3E": "Angel feather arrows",
    "3F": "Bird of perception",
    "40": "Stoic watchman",
    "41": "Emblem of cognizance",
    "42": "Statesmen's medal",
    "43": "Diplomat's Ring",
    "44": "Ambassador's sash",
    "45": "Ring of the wayfarer",
    "46": "Equestrian's gloves",
    "47": "Necklace of ocean guidance",
    "48": "Angel wings",
    "49": "Charm of mana",
    "4A": "Talisman of mana",
    "4B": "Mystic orb of mana",
    "4C": "Collar of conjuring",
    "4D": "Ring of conjuring",
    "4E": "Cape of conjuring",
    "4F": "Orb of firmament",
    "50": "Orb of silt",
    "51": "Orb of tempestuous fire",
    "52": "Orb of driving rain",
    "53": "Recanter's cloak",
    "54": "Spirit of oppression",
    "55": "Hourglass of the evil hour",
    "56": "Tome of fire magic",
    "57": "Tome of wind magic",
    "58": "Tome of water magic",
    "59": "Tome of earth magic",
    "5A": "Boots of levitation",
    "5B": "Golden bow",
    "5C": "Sphere of permanence",
    "5D": "Orb of vulnerability",
    "5E": "Ring of vitality",
    "5F": "Ring of life",
    "60": "Vial of lifeblood",
    "61": "Necklace of swiftness",
    "62": "Boots of speed",
    "63": "Cape of velocity",
    "64": "Pendant of dispassion",
    "65": "Pendant of second sight",
    "66": "Pendant of holiness",
    "67": "Pendant of life",
    "68": "Pendant of death",
    "69": "Pendant of free will",
    "6A": "Pendant of negativity",
    "6B": "Pendant of total recall",
    "6C": "Pendant of courage",
    "6D": "Everflowing crystal cloak",
    "6E": "Ring of infinite gems",
    "6F": "Everpouring vial of mercury",
    "70": "Inexhaustable cart of ore",
    "71": "Eversmoking ring of sulfur",
    "72": "Inexhaustable cart of lumber",
    "73": "Endless sack of gold",
    "74": "Endless bag of gold",
    "75": "Endless purse of gold",
    "76": "Legs of legion",
    "77": "Loins of legion",
    "78": "Torso of legion",
    "79": "Arms of legion",
    "7A": "Head of legion",
    "7B": "Sea captain's hat",
    "7C": "Spellbinder's hat",
    "7D": "Shackles of war",
    "7E": "Orb of inhibition",
    "7F": "Vial of dragonblood",
    "80": "Armageddon's blade",
    "81": "Angelic alliance",
    "82": "Cloak of undead king",
    "83": "Elixir of life",
    "84": "Armor of the dammed",
    "85": "Statue of legions",
    "86": "Power of the dragon father",
    "87": "Titan's thunder",
    "88": "Admiral's hat",
    "89": "Archer's bow",
    # Spell scrolls
    "s00": "Summon Boat",
    "s01": "Scuttle Boat",
    "s02": "Visions",
    "s03": "View Earth",
    "s04": "Disguise",
    "s05": "View Air",
    "s06": "Fly",
    "s07": "Water Walk",
    "s08": "Dimension Door",
    "s09": "Town Portal",
    "s0A": "Quick Sand",
    "s0B": "Land Mine",
    "s0C": "Force Field",
    "s0D": "Fire Wall",
    "s0E": "Earthquake",
    "s0F": "Magic Arrow",
    "s10": "Ice Bolt",
    "s11": "Lightning Bolt",
    "s12": "Implosion",
    "s13": "Chain Lightning",
    "s14": "Frost Ring",
    "s15": "Fireball",
    "s16": "Inferno",
    "s17": "Meteor Shower",
    "s18": "Death Ripple",
    "s19": "Destroy Undead",
    "s1A": "Armageddon",
    "s1B": "Shield",
    "s1C": "Air Shield",
    "s1D": "Fire Shield",
    "s1E": "Protection from Air",
    "s1F": "Protection from Fire",
    "s20": "Protection from Water",
    "s21": "Protection from Earth",
    "s22": "Anti-Magic",
    "s23": "Dispel",
    "s24": "Magic Mirror",
    "s25": "Cure",
    "s26": "Resurrection",
    "s27": "Animate Dead",
    "s28": "Sacrifice",
    "s29": "Bless",
    "s2A": "Curse",
    "s2B": "Bloodlust",
    "s2C": "Precision",
    "s2D": "Weakness",
    "s2E": "Stone Skin",
    "s2F": "Disrupting Ray",
    "s30": "Prayer",
    "s31": "Mirth",
    "s32": "Sorrow",
    "s33": "Fortune",
    "s34": "Misfortune",
    "s35": "Haste",
    "s36": "Slow",
    "s37": "Slayer",
    "s38": "Frenzy",
    "s39": "Titan's Lightning Bolt",
    "s3A": "Counterstrike",
    "s3B": "Berserk",
    "s3C": "Hypnotize",
    "s3D": "Forgetfulness",
    "s3E": "Blind",
    "s3F": "Teleport",
    "s40": "Remove Obstacle",
    "s41": "Clone",
    "s42": "Fire Elemental",
    "s43": "Earth Elemental",
    "s44": "Water Elemental",
    "s45": "Air Elemental"
}


def findItemIDByName(name):
    name = name.lower()
    lst = []
    for iID in dicItems:
        if name in dicItems[iID].lower():
            lst.append((iID, dicItems[iID]))
    # When only one item found, that's it!
    n = len(lst)
    if n == 1:
        return lst[0][0]
    elif n > 1:  # When there are more than one item, print them all and let the user choose
        print("{} item(s) found:".format(n))
        for i in range(0, n):
            if lst[i][0][0] == "s":
                print("{}. Spell scroll '{}'".format(i + 1, lst[i][1]))
            else:
                print("{}. {}".format(i + 1, lst[i][1]))
        i = int(input("Choose which one to add (enter number):"))
        if i < 1 or i > len(lst):
            print("Wrong answer. Can't add item.")
            return -1
        return lst[i - 1][0]

    print("Item not found")
    return -2


def my_exit(exit_code):
    input("Press Enter to continue...")
    exit(exit_code)


if not(len(argv) == 2 or len(argv) == 4):
    print("Usage:\n")
    print("python homm3.py <savegame> [<hero name> <item ID>]")
    my_exit(1)

gm_file = argv[1]
gm_content = []
hero = ""
itemID = 0
itemName = ""
bSpell = False
bFromArgs = False

if len(argv) > 2:
    hero = argv[2]
    itemID = argv[3]
    bFromArgs = True
else:
    hero = input("Enter hero name:\n")
    itemID = input("Enter item: Artifact ID, Spell ID prefixed with 's', artifact/spell name\n"
                   "(at least 4 chars part of the name, see readme.md):\n")

hero = hero.capitalize()
# Parse item ID (spell or artifact)
if len(itemID) >= 4 and not bFromArgs:  # Entered name (not ID) from console input
    itemID = findItemIDByName(itemID)
    if type(itemID) == int:
        my_exit(1)

print("")

if itemID[0].lower() == 's':
    try:
        itemID = int(itemID[1:], 16)
        tmp = "s{:02X}".format(itemID)
        if tmp in dicItems:
            itemName = "Spell scroll with \"" + dicItems[tmp] + "\""
        else:
            raise ValueError
        bSpell = True

    except ValueError:
        print("Invalid spell ID")
        my_exit(1)
else:
    try:
        tmp = itemID.upper()
        if tmp in dicItems:
            itemName = dicItems[tmp]
        else:
            raise ValueError
        itemID = int(itemID, 16)

    except ValueError:
        print("Invalid artifact ID")
        my_exit(1)

try:
    gm = gzip_homm3.open(gm_file)
    gm_content = bytearray(gm.read())
    gm.close()
except FileNotFoundError as err:
    print("File '{}' not found".format(err.filename))
    my_exit(1)

# Looking for hero by name (name must be followed by zero byte)
hero_b = hero.encode(encoding="ascii")
c = 0
while c >= 0:
    c = gm_content.find(hero_b, c + 1)
    if c > 0 and gm_content[c - 1] == 0 and gm_content[c + len(hero)] == 0:
        # Going to catapult slot (offset 0x155)
        d = c + 0x155
        # Check for catapult (int32 == 3) in this offset
        val = int.from_bytes(gm_content[d:d+4], byteorder='little')
        if val == 3:
            break

if c < 0:
    print("Hero {} not found".format(hero))
    my_exit(1)

# Going to first inventory item (offset 0x18 from catapult slot)
c += 0x155 + 0x18
d = 0
while d < 64:
    # Check for non-null in this offset
    idx = c + d * 8
    val = int.from_bytes(gm_content[idx:idx + 4], byteorder='little')
    if val == 0xFFFFFFFF:
        break
    d += 1

if d < 64:
    c += d * 8
    print("Free slot found at position 0x{:X}".format(c))
    print("{} was added to hero's inventory slot {}".format(itemName, d + 1))
    # Adding item
    if bSpell:
        gm_content[c:c + 4] = 0x01.to_bytes(4, byteorder='little')
        gm_content[c + 4:c + 8] = itemID.to_bytes(4, byteorder='little')
    else:
        gm_content[c:c + 4] = itemID.to_bytes(4, byteorder='little')
        gm_content[c + 4:c + 8] = 0xFFFFFFFF.to_bytes(4, byteorder='little')

else:
    print("No free slot found in inventory")
    my_exit(1)

# Renaming old file and writing new one
shutil.move(gm_file, gm_file + ".bak")
gm = open(gm_file, mode="wb")
gm.write(gm_content)
gm.close()

print("{} bytes written".format(len(gm_content)))

my_exit(0)
