# fixes in first loop
# create checklist to double check each loop
# melee vs garen        # edited/corrected don't forget to copy and paste this strategy!

import random

# ---------------------------------------- Character Dictionaries ----------------------------------------
hero = {
    "name": "garen",
    "level": 15,
    "health": 1000,
    "equipment": ("shoulder plates","chest plate","armored leggings","sword"),
    "attacks": (("decisive strike", 30), ("demacian justice spin", 40), ("judgment", 50)),
    "coins": {"copper": 5, "silver": 3, "gold": 1}
}

enemy_one = {
    "name": "melee minion",
    "level": 10,
    "health": 180,
    "equipment": ("hooded cloak", "sword", "shield"),
    "attacks": (("swing", 25), ("shield bash", 50)),
    "coins": {"copper": 3, "silver": 4, "gold": 5}
}

enemy_two = {
    "name": "ranged minion",
    "level": 11,
    "health": 140,
    "equipment": ("hooded cloak", "wand", "dark seal necklace"),
    "attacks": (("smite", 50), ("focus", 75)),
    "coins": {"copper": 6, "silver": 8, "gold": 10}
}

enemy_three = {
    "name": "cannon minion",
    "level": 12,
    "health": 200,
    "equipment": ("hooded cloak", "cannon mount"),
    "attacks": (("fire", 75), ("focus fire", 100)),
    "coins": {"copper": 12, "silver": 16, "gold": 20}
}

# ---------------------------------------- Story Begins ----------------------------------------
# print("------------------------------ Narrator ------------------------------")
# print("As our hero, Garen, spawns in Runeterra to start yet another adventure,")
# print("he turns to the shopkeeper to purchase his starter gear.")
# print("He gets suited up and gazes off into the distance while thinking to himself...")
# print("Should I go into the jungle?... Maybe I can go suppot ADC...")
# print("I think I'll go top today.")
# print("Our hero takes a deep breath, gazes upon the enemy nexus off in the distance,")
# print("readies his sword and starts on his journey towards top lane...")
# print("Our hero makes it out of the base and about half way accross the field without incident")
# print("until he hears a voice from the jungle.")

# print(" ------------------------------ Cannon Minion ------------------------------ ")
# print("Hey you!... Yea you!")

# print("------------------------------ Narrator ------------------------------")
# print("Garen stops and looks to his right side toward the sound of the voice...")

# print(" ------------------------------ Garen ------------------------------ ")
# print("Who goes there! Don't waste my time! Show yourself!")

# print("------------------------------ Narrator ------------------------------")
# print("Garen, isn't too concerned but he is always cautions.")
# print("He knows the rift is a dangerous place. For this reason, he never completely lets his guard down.")
# print("Damacian warriors are feared and respected accross all lands for their raw strength, fearlessness")
# print("and sharp, heavy weapons.")
# print("A cannon minion appears from the darkness of the jungle.")

# print(" ------------------------------ Cannon Minion ------------------------------ ")
# print("HAHAHAHA... It's not safe out here! You shouldn't be out here alone.")

# print("------------------------------ Narrator ------------------------------")
# print("Suddenly, a warning shot is fired from a wand from the bushes behind Garen!")
# print("Garen doesn't even flinch as the shot flies by missing him by inches!")

# print(" ------------------------------ Ranged Minion ------------------------------ ")
# print("HeHeHeHe!!!...")

# print("------------------------------ Narrator ------------------------------")
# print("A Ranged minion slowly appears from the bush.")

# print(" ------------------------------ Melee Minion ------------------------------ ")
# print("Look what we have here guys, another wannabe hero who thinks he's a tough guy...")

# print("------------------------------ Narrator ------------------------------")
# print("The melee minion mocks Garen as he appear from behind the cannon minion.")

# print(" ------------------------------ Ranged Minion ------------------------------ ")
# print("This one looks like he'll be fun... do us a favor tough guy and don't embarrass us by crying like a...")

# print(" ------------------------------ Garen ------------------------------ ")
# print("Do not bother me and DO NOT GET IN MY WAY, I am on a mission to destroy the enemy nexus..., ")
# print("anyone or anything that hinders me will share the same fate!")

# print(" ------------------------------ Ranged Minion ------------------------------ ")
# print("You have some nerve interrupting me while I'm talking. I'm really going to enjoy what happens next!")

# print(" ------------------------------ Cannon Minion ------------------------------ ")
# print("Headed to the nexus you say? I don't think so tough guy,")
# print("You have to get through us first, so I guess you're not gunna MAKE IT!!! HAHAHAHAH!!!")

# print(" ------------------------------ Ranged Minion ------------------------------ ")
# print("HeHeHeHeHe!!!")

# print(" ------------------------------ Melee Minion ------------------------------ ")
# print("HAHAHAHAH!!!")

print("------------------------------ Narrator ------------------------------")
print("Garen has had enough of their disrespectful babbling!!! He grips his sword tighly and swings behind him. He cleanly")
print("cleaves through the bush with his razor sharp blade leaving a perfectly precise, level cut. The ranged minion")
print("quickly dodges the blade as a sliver of his cloak slowly falls to the ground. The ranged minion quickly joins the")
print("others as they prepare for battle.")

h_health = hero["health"]
e_one_health = enemy_one["health"]
e_two_health = enemy_two["health"]
e_three_health = enemy_three["health"]

# ---------------------------------------- FIGHT ----------------------------------------

# ---------------------------- Garen Strikes Melee Minion----------------------------
garen_chosen_attack = random.choice(hero["attacks"])

def garen_vs_melee_minion():

    for h_attack in garen_chosen_attack:
        if h_attack == ("decisive strike", 30):
            enemy_one["health"] -= 30
            print(f"{h_health} health Garen attacks Melee Minion with Decisive Strike for 30 dmg")   # FIX?

    for h_attack in garen_chosen_attack:
        if h_attack == ("demacian justice spin", 40):   # spin effects all enemies
            enemy_one["health"] -= 40
            enemy_two["health"] -= 40
            enemy_three["health"] -= 40
            print(f"{h_health} health Garen attacks all enemies with Demacian Justice Spin for 40 dmg each")   # FIX?

    for h_attack in garen_chosen_attack:
        if h_attack == ("judgment", 50):
            enemy_one["health"] -= 50
            print(f"{h_health} health Garen attacks Melee Minion with Judgment for 50 dmg")   # FIX?

    if e_one_health <= 0:
        print("Melee Minion has been defeated and Garen collects his loot.")
        print("He has added 3 Copper, 4 Silver and 5 Gold")
        print("to his 5 Copper, 3 Silver, and 1 Gold!")
        print("Our hero has leveled up from 15 to 16 and learned a new ability!")
        print("(Courage) - Passively block 5 dmg from all attacks.")

        hero["coins"]["copper"] += 3
        hero["coins"]["silver"] += 4
        hero["coins"]["gold"] += 5
        hero["level"] += 1
        hero["abilities"] = ("courage", -5)

        ranged_minion_vs_garen()
    else:
        melee_minion_vs_garen()     

# ---------------------------- Melee Minion Strikes ----------------------------
melee_chosen_attack = random.choice(enemy_one["attacks"])

def melee_minion_vs_garen():

    for m_attack in melee_chosen_attack:
        if m_attack == ("swing", 25):
            hero["health"] -= 20
            print(f"{e_one_health} health Melee Minion attacks Garen with Swing for 25 dmg -5")

    for m_attack in melee_chosen_attack:
        if m_attack == ("shield bash", 50):
            hero["health"] -= 45
            print(f"{e_one_health} health Melee Minion attacks Garen with Shield Bash for 50 dmg -5")

garen_vs_melee_minion()     

# ---------------------------- Ranged Minion Strikes ---------------------------- 
# Melee Minion has been defeated at this point. Garen now faces Ranged Minion.
ranged_chosen_attack = random.choice(enemy_two["attacks"])

def ranged_minion_vs_garen():

    for r_attack in ranged_chosen_attack:
        if r_attack == ("smite", 50):
            hero["health"] -= 45
            print("Ranged Minion attacks Garen with Smite for 50 dmg -5")

    for r_attack in ranged_chosen_attack:
        if r_attack == ("focus", 75):
            hero["health"] -= 70
            print("Ranged Minion attacks Garen with Focus for 75 dmg -5")

        garen_vs_ranged_minion()

# ---------------------------- Garen Strikes Ranged Minion ----------------------------
garen_chosen_attack = random.choice(hero["attacks"])

def garen_vs_ranged_minion():

    for h_attack in garen_chosen_attack:
        if h_attack == ("decisive strike", 30):
            enemy_two["health"] -= 30
            print("Garen at {h_health} attacks Ranged Minion with Decisive Strike for 30 dmg")

    for h_attack in garen_chosen_attack:
        if h_attack == ("demacian justice spin", 40):   # spin effects all enemies
            enemy_two["health"] -= 40
            enemy_three["health"] -= 40
            print("Garen at {h_health} attacks both enemies with Demacian Justice Spin for 40 dmg each")

    for h_attack in garen_chosen_attack:
        if h_attack == ("judgment", 50):
            enemy_two["health"] -= 50
            print("Garen at {h_health} attacks Ranged Minion with Judgment for 50 dmg")

    if e_two_health <= 0:
        print("Ranged Minion has been defeated and Garen collects his loot.")
        print("He has added 6 Copper, 8 Silver and 10 Gold")
        print("to his 8 Copper, 7 Silver, and 6 Gold!")
        print("Our hero has leveled up from 16 to 17 and learned a new ability!")
        print("(Demacian Rage) - Passively increase the damage of all Garen's attacks by 5.")

        hero["coins"]["copper"] += 6
        hero["coins"]["silver"] += 8
        hero["coins"]["gold"] += 10
        hero["level"] += 1
        hero["abilities"] = ("Demacian Rage", +5)

        cannon_minion_vs_garen()
    else:
        ranged_minion_vs_garen()     

# ---------------------------- Cannon Minion Strikes ---------------------------- 
# Melee Minion AND Ranged Minion have been defeated at this point. Garen now faces Cannon Minion.
cannon_chosen_attack = random.choice(enemy_three["attacks"])

def cannon_minion_vs_garen():

    for c_attack in cannon_chosen_attack:
        if c_attack == ("fire", 75):
            hero["health"] -= 70
            print("Cannon Minion attacks Garen with Fire for 75 dmg -5")

    for c_attack in cannon_chosen_attack:
        if c_attack == ("focus fire", 100):
            hero["health"] -= 95
            print("Cannon Minion attacks Garen with Focus Fire for 100 dmg -5")

    if h_health <= 0:
        print("Our hero has fallen in battle. The enemy minions were able to defend their nexus.")
        enemy_ending()
    else:
        garen_vs_cannon_minion()

# ---------------------------- Garen Strikes Cannon Minion---------------------- 
garen_chosen_attack = random.choice(hero["attacks"])

def garen_vs_cannon_minion():

    for h_attack in garen_chosen_attack:
        if h_attack == ("decisive strike", 30):
            enemy_three["health"] -= 30
            print("Garen attacks Cannon Minion with Decisive Strike for 30 dmg")

    for h_attack in garen_chosen_attack:
        if h_attack == ("demacian justice spin", 40):   # spin effects all enemies
            enemy_three["health"] -= 40
            print("Garen attacks Cannon Minion with Demacian Dustice Dpin for 40 dmg")

    for h_attack in garen_chosen_attack:
        if h_attack == ("judgment", 50):
            enemy_three["health"] -= 50
            print("Garen attacks Cannon Minion with Decisive Strike for 50 dmg")

    if e_three_health <= 0:
        print("Cannon Minion has been defeated and Garen collects his loot.")
        print("He has added 12 Copper, 16 Silver and 20 Gold")
        print("to his 14 Copper, 15 Silver, and 16 Gold!")
        print("Our hero has gained max level of 18 and learned a new ability!")
        print("(Warrior's Infamy) -  of all enemies will flee at the sight of Garen.")

        hero["coins"]["copper"] += 12
        hero["coins"]["silver"] += 16
        hero["coins"]["gold"] += 20
        hero["level"] += 1
        hero["abilities"] = ("Warrior's Infamy", 0)

        garen_ending()
    else:
        cannon_minion_vs_garen()

# ---------------------------------------- Ending ----------------------------------------
def garen_ending():

    print("Our hero continues heading towards the enemy nexus as he passively heals to full heal along the way.")
    print("He reaches the defenses and shruggs off their attacks as he reduces them to piles of rubble one after")
    print("another. The enemy obviously never expected anyone to reach their base because half the guards were.")
    print("low level and the other half threw down their weapons and ran away.")
    print("Our hero completed his mission and returned to Demacia a hero.")
    print("--------------- THE END ---------------")
    exit()

def enemy_ending():

    print("Cannon Minion climbed down from his cannon and stood over garen as he chuckled and looted his body.")
    print("He returned to his base a hero, waited for another Melee Minion and Ranged Minion to spawn and")
    print("returned to the battle field to scount for more enemies.")
    print("--------------- THE END... UNFORTUNATELY... ---------------")
