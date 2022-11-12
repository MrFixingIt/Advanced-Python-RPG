# fixes in first loop
# edit "health" and "attack damage" values for all characters
# pull damage values from dictionaries instead of filling in values manually
# break up the project and test each individul loop!
# 10:00 rewatch import info from (Video-Advanced Python RPG-HeroData Structure Walkthrough)
#   AND the Code Demo
#       slow print statements (When project is completed)
#       colorful print statements  (When project is completed)

import random

# -------------------------------------- Character Dictionaries and Variables--------------------------------------
hero = {
    "name": "Garen",
    "level": 15,
    "health": 1000,
    "equipment": {"shoulder plates","chest plate","armored leggings","sword"},
    "attacks": (("decisive strike", 30), ("demacian justice spin", 40), ("judgment", 50)),
    "coins": {"copper": 5, "silver": 3, "gold": 1}
}

enemy_one = {
    "name": "Melee Minion",
    "level": 10,
    "health": 180,
    "equipment": {"hooded cloak", "sword", "shield"},
    "attacks": (("swing", 25), ("shield bash", 50)),
    "coins": {"copper": 6, "silver": 5, "gold": 4}
}

enemy_two = {
    "name": "ranged minion",
    "level": 11,
    "health": 140,
    "equipment": {"hooded cloak", "wand", "dark seal necklace"},
    "attacks": (("smite", 50), ("focus", 75)),
    "coins": {"copper": 9, "silver": 11, "gold": 14}
}

enemy_three = {
    "name": "cannon minion",
    "level": 12,
    "health": 200,
    "equipment": {"hooded cloak", "cannon mount"},
    "attacks": (("fire", 75), ("focus fire", 100)),
    "coins": {"copper": 12, "silver": 16, "gold": 20}
}

h_health = hero["health"]
e_one_health = enemy_one["health"]
e_two_health = enemy_two["health"]
e_three_health = enemy_three["health"]

h_money = hero["coins"]
e_one_money = enemy_one["coins"]
e_two_money = enemy_two["coins"]
e_three_money = enemy_three["coins"]

h_equipment = hero["equipment"]
e_one_equipment = enemy_one["equipment"]
e_two_equipment = enemy_two["equipment"]
e_three_equipment = enemy_three["equipment"]

# ---------------------------------------- Story Begins ----------------------------------------
print("------------------------------ Narrator ------------------------------")
print("As our hero, Garen, spawns in Runeterra to start his adventure and turns to the shopkeeper to purchase his starter gear.")
print("He gets suited up and gazes off into the distance while thinking to himself...")
print("Should I go into the jungle?... Maybe I can go suppot ADC... I think I'll go top lane.")
print("Our hero takes a deep breath, gazes upon the enemy nexus off in the distance, readies his sword and starts on his journey towards top lane...")
print("Our hero makes it out of the base and about half way accross the field without incident until he hears a voice from the jungle.")

print(" ------------------------------ Cannon Minion ------------------------------ ")
print("Hey you!... Yea you!")

print("------------------------------ Narrator ------------------------------")
print("Garen stops and looks to his right side toward the sound of the voice...")

print(" ------------------------------ Garen ------------------------------ ")
print("Who goes there! Don't waste my time! Show yourself!")

print("------------------------------ Narrator ------------------------------")
print("Garen, isn't too concerned but he is always cautions.")
print("He knows the rift is a dangerous place. For this reason, he never completely lets his guard down.")
print("Damacian warriors are feared and respected accross all lands for their raw strength, fearlessness and sharp, heavy weapons.")
print("A cannon minion appears from the darkness of the jungle.")

print(" ------------------------------ Cannon Minion ------------------------------ ")
print("HAHAHAHA... It's not safe out here! You shouldn't be out here alone.")

print("------------------------------ Narrator ------------------------------")
print("Suddenly, a warning shot is fired from a wand from the bushes behind Garen! Garen doesn't even flinch as the shot flies by missing him by inches!")

print(" ------------------------------ Ranged Minion ------------------------------ ")
print("HeHeHeHe!!!...")

print("------------------------------ Narrator ------------------------------")
print("A Ranged minion slowly appears from the bush.")

print(" ------------------------------ Melee Minion ------------------------------ ")
print("Look what we have here guys, another wannabe hero who thinks he's a tough guy...")

print("------------------------------ Narrator ------------------------------")
print("The melee minion mocks Garen as he appear from behind the cannon minion.")

print(" ------------------------------ Ranged Minion ------------------------------ ")
print("This one looks like he'll be fun... do us a favor tough guy and don't embarrass us by crying like a...")

print(" ------------------------------ Garen ------------------------------ ")
print("Do not bother me and DO NOT GET IN MY WAY, I am on a mission to destroy the enemy nexus! Anyone or anything that hinders me will share the same fate!")

print(" ------------------------------ Ranged Minion ------------------------------ ")
print("You have some nerve interrupting me while I'm talking. I'm really going to enjoy what happens next!")

print(" ------------------------------ Cannon Minion ------------------------------ ")
print("Headed to the nexus you say? I don't think so tough guy, you have to get through us first, so I guess you're not gunna MAKE IT!!! HAHAHAHAH!!!")

print(" ------------------------------ Ranged Minion ------------------------------ ")
print("HeHeHeHeHe!!!")

print(" ------------------------------ Melee Minion ------------------------------ ")
print("HAHAHAHAH!!!")

print("------------------------------ Narrator ------------------------------")
print("At the point, Garen has had enough of their disrespectful babbling!!! He grips his sword tighly and swings behind him. He cleanly cleaves through the bush with his razor sharp blade leaving a perfectly precise, level cut. The ranged minion quickly dodges the blade as a sliver of his cloak slowly falls to the ground. The ranged minion quickly joins the others as they prepare for battle.")
print("Our hero strikes firts!.")

# ---------------------------------------- FIGHT ----------------------------------------

# ---------------------------- Garen Strikes Melee Minion----------------------------
garen_chosen_attack = random.choice(hero["attacks"])

def garen_vs_melee_minion():

    for h_attack in garen_chosen_attack:
        if h_attack == ("decisive strike", 30):
            enemy_one["health"] -= 30
            print(f"{h_health} health Garen attacks Melee Minion with Decisive Strike for 30 dmg")

    for h_attack in garen_chosen_attack:
        if h_attack == ("demacian justice spin", 40):   # spin effects all enemies
            enemy_one["health"] -= 40
            enemy_two["health"] -= 40
            enemy_three["health"] -= 40
            print(f"{h_health} health Garen attacks all enemies with Demacian Justice Spin for 40 dmg each")

    for h_attack in garen_chosen_attack:
        if h_attack == ("judgment", 50):
            enemy_one["health"] -= 50
            print(f"{h_health} health Garen attacks Melee Minion with Judgment for 50 dmg") 

    if e_one_health <= 0:
        print("Melee Minion has been defeated and Garen collects his loot.")
        print(f"He collects Melee Minion's equipment: {e_one_equipment}")
        print(f"He has collected Melee Minion's money: {e_one_money}")
        hero["coins"]["copper"] += 6
        hero["coins"]["silver"] += 5
        hero["coins"]["gold"] += 4
        hero["equipment"] += enemy_one["equipment"]
        hero["level"] += 1
        hero["abilities"] += ("courage", -5)
        print("Our hero has leveled up from 15 to 16 and learned a new ability!")
        print("(Courage) - Passively block 5 dmg from all attacks.")
        print(hero)
        ranged_minion_vs_garen()
    else:
        melee_minion_vs_garen()     

# ---------------------------- Melee Minion Strikes ----------------------------
melee_chosen_attack = random.choice(enemy_one["attacks"])

def melee_minion_vs_garen():

    for m_attack in melee_chosen_attack:
        if m_attack == ("swing", 25):
            hero["health"] -= 25
            print(f"{e_one_health} health Melee Minion attacks Garen with Swing for 25 dmg")
            garen_vs_melee_minion()

    for m_attack in melee_chosen_attack:
        if m_attack == ("shield bash", 50):
            hero["health"] -= 50
            print(f"{e_one_health} health Melee Minion attacks Garen with Shield Bash for 50 dmg")
            garen_vs_melee_minion()     

# ---------------------------- Ranged Minion Strikes ---------------------------- 
# Melee Minion has been defeated at this point. Garen now faces Ranged Minion.
ranged_chosen_attack = random.choice(enemy_two["attacks"])

def ranged_minion_vs_garen():

    for r_attack in ranged_chosen_attack:
        if r_attack == ("smite", 50):
            hero["health"] -= 45
            print("Ranged Minion attacks Garen with Smite for 50 dmg -5")
            garen_vs_ranged_minion()

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
        print("Range Minion has been defeated and Garen collects his loot.")
        print(f"He collects Ranged Minion's equipment: {e_two_equipment}")
        print(f"He has collected Ranged Minion's money: {e_two_money}")
        hero["coins"]["copper"] += 9
        hero["coins"]["silver"] += 11
        hero["coins"]["gold"] += 14
        hero["equipment"] += enemy_two["equipment"]
        hero["level"] += 1
        hero["abilities"] += ("courage", -5)
        print("Our hero has leveled up from 16 to 17 and learned a new ability!")
        print("(Demacian Rage) - Passively increase the damage of all attacks by 5")
        print(hero)
        cannon_minion_vs_garen()
    else:
        melee_minion_vs_garen()     

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
            enemy_three["health"] -= 35
            print("Garen attacks Cannon Minion with Decisive Strike for 30 dmg +5")

    for h_attack in garen_chosen_attack:
        if h_attack == ("demacian justice spin", 40):   # spin effects all enemies
            enemy_three["health"] -= 45
            print("Garen attacks Cannon Minion with Demacian Dustice Dpin for 40 dmg +5")

    for h_attack in garen_chosen_attack:
        if h_attack == ("judgment", 50):
            enemy_three["health"] -= 55
            print("Garen attacks Cannon Minion with Decisive Strike for 50 dmg +5")

    if e_three_health <= 0:
        print("Cannon Minion has been defeated and Garen collects his loot.")
        print(f"He collects Cannon Minion's equipment: {e_three_equipment}")
        print(f"He has collected Cannon Minion's money: {e_three_money}")
        hero["coins"]["copper"] += 12
        hero["coins"]["silver"] += 16
        hero["coins"]["gold"] += 20
        hero["equipment"] += enemy_three["equipment"]
        hero["level"] += 1
        hero["abilities"] += ("Warlord's Infamy", 0)
        print("(Warlord's Infamy) - Half of all enemies flee from the sight of Garen.")
        print("Our hero has reached max level of 18 and learned a new ability!")
        print(hero)
        garen_ending()
    else:
        cannon_minion_vs_garen()

# ---------------------------------------- Endings ----------------------------------------
def garen_ending():

    print("Our hero continues heading towards the enemy nexus as he passively heals to full heal along the way. He reaches the defenses and shruggs off their attacks as he reduces them to piles of rubble one after another. With all of the equipment, abilities and levels he has gained from his enemies, he knows that he is unstoppable. The enemy obviously never expected anyone to reach their base. Half the guards were low level and the other half threw down their weapons and ran away. Our hero completed his mission and returned to Demacia a hero. He was celebrated by his people and a statue was erected in his honor.")
    print("--------------- THE END ---------------")
    exit()

def enemy_ending():

    print("Cannon Minion climbed down from his cannon and stood over garen as he chuckled and looted his body. He returned to his base a hero and modified his newly aquired equipment to suit himself. He then purchase some equipment for his empty item slots, waited for another Melee Minion and Ranged Minion to spawn and returned to the battle field to scount for more enemies. His newly looted and purchased equipment made him stronger than ever. Our next brave challenger would be in for an even tougher battle than Garen could handle.")
    print("--------------- THE END... UNFORTUNATELY... ---------------")
    exit()