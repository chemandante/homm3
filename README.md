
# Simple trainer for Heroes of Might and Magic III

Used to add any artifact (or spell scroll) to any hero

Usage:
```
python -B homm3.py <savegame> [<hero name> <item ID>]
```

This trainer takes savegame file, looks for a hero by **hero name** and adds artifact with specified **item ID** at the first available inventory slot (backpack).
When **hero name** and **item ID** are not specified in command-line, trainer will ask for it. In this case you can enter part ot the item name (at least 4 chars) as **item ID**. If there are more than one item containing that part of the name, you have to choose what item to pup into inventory (see examples).

```
<item ID> := <artifact ID> | s<spell ID>
```

Artifact ID should be entered in hex without '0x' prefix. See table [below](#artifact-list) for a list of all artifacts with their IDs. If you want to add a spell scroll, write 's' before spell ID (see spell list [below](#spell-list))

Then the trainer renames original savegame to `*.bak` and writes unpacked and patched version to original savegame, which can be loaded by HOMM3 as usual.

### Examples

Adding Cloak of Undead King to hero Vidomina in dialog mode by ID (CoUK has ID 82):
```
>>> python -B homm3.py 1.GM1

Enter hero name:
>>> vidomina
Enter item: Artifact ID, Spell ID prefixed with 's', artifact/spell name
(at least 4 chars part of the name, see readme.md):
>>> 82

Free slot found at position 0x3D5AD
Cloak of undead king was added to hero's inventory slot 1
353169 bytes written
Press Enter to continue...
```

Adding Cloak of Undead King to hero Vidomina in dialog mode by part of name:
```
Enter hero name:
>>> vidomina
Enter item: Artifact ID, Spell ID prefixed with 's', artifact/spell name
(at least 4 chars part of the name, see readme.md):
>>> cloak

3 item(s) found:
1. Recanter's cloak
2. Everflowing cristal cloak
3. Cloak of undead king
Choose which one to add (enter number):
>>> 3
Free slot found at position 0x3D5AD
Cloak of undead king was added to hero's inventory slot 1
353169 bytes written
Press Enter to continue...
```

Adding scroll with Town Portal to Sandro in command-line mode:
```
>>> python -B homm3.py 1.GM1 Sandro s09

Free slot found at position 0x3AF37
Spell scroll with "Town Portal" was added to hero's inventory slot 1
353169 bytes written
Press Enter to continue...
```

### Note on savegame file

Savegames in HOMM3 look like GZIP-files, but unpacking it raises CRC error. To eliminate this behaviour standard Python **gzip** module was patched and included in project as **gzip_homm3.py**.

Because HOMM3 can load uncompressed savegames, this trainer doesn't compress patched savegame back. So, don't worry if the corrected savegame will be 3 times larger, it is just uncompressed.

### Appreciations

I thank [Maurice](http://heroescommunity.com/member.php3?action=viewprofile&UserName=Maurice) for his post at [heroescommunity.com](http://heroescommunity.com/viewthread.php3?TID=18817) forum for valuable information.

### Artifact list

07 - Centaur's axe\
08 - Blackshard of the dead knight\
09 - Greater Gnoll's Fail\
0A - Ogre's club of havoc\
0B - Sword of Hellfire\
0C - Titan's gladius\
0D - Shield of the dwarven lords\
0E - Shield of the yawning dead\
0F - Buckler of the gnoll king\
10 - Targ of the rampaging ogre\
11 - Shield of the dammed\
12 - Sentinel's Shield\
13 - Helm of the alabaster unicorn\
14 - Skull helmet\
15 - Helm of chaos\
16 - Crown of the supreme magi\
17 - Hellstorm helmet\
18 - Thunder helmet\
19 - Beastplate of petrified wood\
1A - Rib cage\
1B - Scales of the greater balilisk\
1C - Tunic of the cyclops king\
1D - Breastplate of brimstone\
1E - Titan's cuirass\
1F - Armor of wonder\
20 - Sandals of the saint\
21 - Celestial necklace of bliss\
22 - Lion's shield of courage\
23 - Sword of judgement\
24 - Helm of hevenly enlightenment\
25 - Quiet eye of the dragon\
26 - Red dragon flame tongue\
27 - Dragon scale shield\
28 - Dragon scale armor\
29 - Dragonbone greaves\
2A - Dragon wing tabard\
2B - Neckace of dragonteeth\
2C - Crown of dragontooth\
2D - Still eye of the dragon\
2E - Clover of fortune\
2F - Cards of prophecy\
30 - Ladybird of luck\
31 - Badge of courage\
32 - Crest of valor\
33 - Gryph of gallantry\
34 - Speculum\
35 - Spyglass\
36 - Amulet of the undertaker\
37 - Vampire's cowl\
38 - Dead men's boots\
39 - Garniture of interference\
3A - Surcoat of counterpoise\
3B - Boots of polarity\
3C - Bow of elven cherrywood\
3D - Bowstring of the unicorns's mane\
3E - Angel feather arrows\
3F - Bird of perception\
40 - Stoic watchman\
41 - Emblem of cognizance\
42 - Statesmen's medal\
43 - Diplomat Ring\
44 - Ambassador's sash\
45 - Ring of the wayfarer\
46 - Equestrian's gloves\
47 - Necklace of ocean guidance\
48 - Angel wings\
49 - Charm of mana\
4A - Talisman of mana\
4B - Mystic orb of mana\
4C - Collar of conjuring\
4D - Ring of conjuring\
4E - Cape of conjuring\
4F - Orb of firmament\
50 - Orb of silt\
51 - Orb of tempestous fire\
52 - Orb of driving rain\
53 - Recanter's cloak\
54 - Spirit of opression\
55 - Hourglass of the evil hour\
56 - Tome of fire magic\
57 - Tome of wind magic\
58 - Tome of water magic\
59 - Tome of earth magic\
5A - Boots of levitation\
5B - Golden bow\
5C - Sphere of permanence\
5D - Orb of vulnerability\
5E - Ring of vitality\
5F - Ring of life\
60 - Vail of lifeblood\
61 - Necklace of swiftness\
62 - Boots of speed\
63 - Cape of velocity\
64 - Pendant of dispassion\
65 - Pendant of second sight\
66 - Pendant of holiness\
67 - Pendant of life\
68 - Pendant of death\
69 - Pendant of free will\
6A - Pendant of agitation\
6B - Pendant of total recall\
6C - Pendant of courage\
6D - Everflowing cristal cloak\
6E - Ring of infinite gems\
6F - Everpouring vial of mercury\
70 - Inexhaustable cart of ore\
71 - Eversmoking ring of sulfur\
72 - Inexhaustable cart of lumber\
73 - Endless sack of gold\
74 - Endless bag of gold\
75 - Endless purse of gold\
76 - Legs of legion\
77 - Loins of legion\
78 - Torso of legion\
79 - Arms of legion\
7A - Head of legion\
7B - Sea capitan's hat\
7C - Spellbinder's hat\
7D - Shackles of war\
7E - Orb of inhibition\
**Combined artifacts and specials:**\
7F - Vial of dragonblood\
80 - Armageddon's blade\
81 - Angelic alliance\
82 - Cloak of undead king\
83 - Elixir of life\
84 - Armor of the dammed\
85 - Statue of legions\
86 - Power of the dragon father\
87 - Titans lightning\
88 - Admiral's hat\
89 - Archer's bow

### Spell list

00 - Summon Boat\
01 - Scuttle Boat\
02 - Visions\
03 - View Earth\
04 - Disguise\
05 - View Air\
06 - Fly\
07 - Water Walk\
08 - Dimension Door\
09 - Town Portal\
0A - Quick Sand\
0B - Land Mine\
0C - Force Field\
0D - Fire Wall\
0E - Earthquake\
0F - Magic Arrow\
10 - Ice Bolt\
11 - Lightning Bolt\
12 - Implosion\
13 - Chain Lightning\
14 - Frost Ring\
15 - Fireball\
16 - Inferno\
17 - Meteor Shower\
18 - Death Ripple\
19 - Destroy Undead\
1A - Armageddon\
1B - Shield\
1C - Air Shield\
1D - Fire Shield\
1E - Protection from Air\
1F - Protection from Fire\
20 - Protection from Water\
21 - Protection from Earth\
22 - Anti-Magic\
23 - Dispel\
24 - Magic Mirror\
25 - Cure\
26 - Resurrection\
27 - Animate Dead\
28 - Sacrifice\
29 - Bless\
2A - Curse\
2B - Bloodlust\
2C - Precision\
2D - Weakness\
2E - Stone Skin\
2F - Disrupting Ray\
30 - Prayer\
31 - Mirth\
32 - Sorrow\
33 - Fortune\
34 - Misfortune\
35 - Haste\
36 - Slow\
37 - Slayer\
38 - Frenzy\
39 - Titan's Lightning Bolt\
3A - Counterstrike\
3B - Berserk\
3C - Hypnotize\
3D - Forgetfulness\
3E - Blind\
3F - Teleport\
40 - Remove Obstacle\
41 - Clone\
42 - Fire Elemental\
43 - Earth Elemental\
44 - Water Elemental\
45 - Air Elemental
