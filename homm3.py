import gzip_homm3
import shutil

from sys import argv


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
bSpell = False

if len(argv) > 2:
    hero = argv[2]
    itemID = argv[3]
else:
    hero = input("Enter hero name:\n")
    itemID = input("Enter item ID (see readme.md):\n")

hero = hero.capitalize()
# Parse item ID (spell or artifact)
if itemID[0].lower() == 's':
    try:
        itemID = int(itemID[1:], 16)
        if itemID > 0x45:
            raise ValueError
        bSpell = True

    except ValueError:
        print("Invalid spell ID")
        my_exit(1)
else:
    try:
        itemID = int(itemID, 16)
        if itemID < 0x07 or itemID > 0x89:
            raise ValueError

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
    print("Free slot found at position 0x{:X} (inventory slot {})".format(c, d + 1))
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
