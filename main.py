import random

from characters import hero
from characters import enemy_one
from characters import enemy_two
from characters import enemy_three
from characters import second_ability
from characters import third_ability

import sys
import time

def slow_print(string_to_print):
	for letter in string_to_print:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.065)
	print("")

narrator_dialog = "------------------------------ Narrator ------------------------------"
hero_dialog = " ------------------------------ Garen ------------------------------ "
melee_minion_dialog = " ------------------------------ Melee Minion ------------------------------ "
ranged_minion_dialog = " ------------------------------ Ranged Minion ------------------------------ "
cannon_minion_dialog = " ------------------------------ Cannon Minion ------------------------------ "

# ---------------------------------------- Story Begins ----------------------------------------
print(narrator_dialog)
dialog1 = "Our hero, Garen, spawns in Runeterra to start his adventure and turns to the shopkeeper to purchase his starter gear. He gets suited up and gazes off into the distance while thinking to himself... Should I go into the jungle?... Maybe I can go suppot ADC... I think I'll go top lane. Our hero takes a deep breath, gazes upon the enemy nexus off in the distance, readies his sword and starts on his journey towards top lane. He makes it out of the base and about half way accross the field without incident until he hears a voice from the jungle."
slow_print(dialog1)
print("   ")

print(cannon_minion_dialog)
dialog2 = "Hey you!... Yea you!"
slow_print(dialog2)
print("   ")

print(narrator_dialog)
dialog3 = "Garen stops and looks toward the sound of the voice..."
slow_print(dialog3)
print("   ")

print(hero_dialog)
dialog4 = "Who goes there! Don't waste my time! Show yourself!"
slow_print(dialog4)
print("   ")

print(narrator_dialog)
dialog5 = "Garen, isn't too concerned but he is always cautions."
dialog6 = "He knows the rift is a dangerous place. For this reason, he never completely lets his guard down. Damacian warriors are feared and respected accross all lands for their raw strength, fearlessness and sharp, heavy weapons."
dialog7 = "A cannon minion appears from the darkness of the jungle."
slow_print(dialog5)
slow_print(dialog6)
slow_print(dialog7)
print("   ")

print(cannon_minion_dialog)
dialog8 = "HAHAHAHA... It's not safe out here! You shouldn't be out here alone."
slow_print(dialog8)
print("   ")

print(narrator_dialog)
dialog9 = "Suddenly, a warning shot is fired from a wand from the bushes behind Garen! Garen doesn't even flinch as the shot flies by missing him by inches!"
slow_print(dialog9)
print("   ")

print(ranged_minion_dialog)
dialog10 = "HeHeHeHe!!!..."
slow_print(dialog10)
print("   ")

print(narrator_dialog)
dialog11 = "A Ranged minion slowly appears from the bush."
slow_print(dialog11)
print("   ")

print(melee_minion_dialog)
dialog12 = "Look what we have here guys, another wannabe hero who thinks he's a tough guy..."
slow_print(dialog12)
print("   ")

print(narrator_dialog)
dialog13 = "The melee minion mocks Garen as he appears from behind the cannon minion."
slow_print(dialog13)
print("   ")

print(ranged_minion_dialog)
dialog14 = "This one looks like he'll be fun... do us a favor tough guy and don't embarrass us by crying like a..."
slow_print(dialog14)
print("   ")

print(hero_dialog)
dialog15 = "Do not bother me and DO NOT GET IN MY WAY, I am on a mission to destroy the enemy nexus! Anyone or anything that hinders me will share the same fate!"
slow_print(dialog15)
print("   ")

print(ranged_minion_dialog)
dialog16 = "You have some nerve interrupting me while I'm talking. I'm really going to enjoy what happens next!"
slow_print(dialog16)
print("   ")

print(cannon_minion_dialog)
dialog17 = "Headed to the nexus you say? I don't think so tough guy, you have to get through us first, so I guess that mean you're not gunna MAKE IT!!! HAHAHAHAH!!!"
slow_print(dialog17)
print("   ")

print(ranged_minion_dialog)
dialog18 = "HeHeHeHeHe!!!"
slow_print(dialog18)
print("   ")

print(melee_minion_dialog)
dialog19 = "HAHAHAHAH!!!"
slow_print(dialog19)
print("   ")

print(narrator_dialog)
dialog20 = "At the point, Garen has had enough of their disrespectful babbling!!! He grips his sword tighly and swings behind him. He cleanly cleaves through the bush with his razor sharp blade leaving a perfectly precise, level cut. The ranged minion quickly dodges the blade as a sliver of his cloak slowly falls to the ground. The ranged minion quickly joins the others as they prepare for battle."
dialog21 = "Our hero strikes first!"
slow_print(dialog20)
slow_print(dialog21)

# ---------------------------------------- Fight Begins----------------------------------------

# ---------------------------- Garen Strikes Melee Minion----------------------------
def garen_vs_melee_minion():

    garen_chosen_attack = random.choice(hero["attacks"])

    if garen_chosen_attack == hero["attacks"][0]:    # ("decisive strike", 30)
        enemy_one["health"] -= 30
        print(f"{hero['health']} health Garen attacks Melee Minion with Decisive Strike for 30 dmg")

    if garen_chosen_attack == hero["attacks"][1]:   # ("demacian justice spin", 40)  
        enemy_one["health"] -= 40                   # spin effects all enemies!
        enemy_two["health"] -= 40
        enemy_three["health"] -= 40
        print(f"{hero['health']} health Garen attacks all enemies with Demacian Justice Spin for 40 dmg each")

    if garen_chosen_attack == hero["attacks"][2]:   # ("judgment", 50)
        enemy_one["health"] -= 50
        print(f"{hero['health']} health Garen attacks Melee Minion with Judgment for 50 dmg") 

    if enemy_one["health"] <= 0:
        print("Melee Minion has been defeated and Garen collects his loot.")
        print(f"He collects Melee Minion's equipment: {enemy_one['equipment']}")
        print(f"He collected Melee Minion's money: {enemy_one['coins']}")
        hero["coins"]["copper"] += 6
        hero["coins"]["silver"] += 5
        hero["coins"]["gold"] += 4
        hero["equipment"].update(enemy_one["equipment"])
        hero["level"] += 1
        hero["abilities"] = ("courage", -5)
        print("Our hero has leveled up from 15 to 16 and learned a new ability!")
        print("(Courage) - Passively block 5 dmg from all attacks.")
        print(hero)
        ranged_minion_vs_garen()

    if enemy_one["health"] > 0:
        melee_minion_vs_garen()

# ---------------------------- Melee Minion Strikes ----------------------------
def melee_minion_vs_garen():

    melee_chosen_attack = random.choice(enemy_one["attacks"])

    if melee_chosen_attack == enemy_one["attacks"][0]:   # ("swing", 25)
        hero["health"] -= 25
        print(f"{enemy_one['health']} health Melee Minion attacks Garen with Swing for 25 dmg")
        garen_vs_melee_minion()

    if melee_chosen_attack == enemy_one["attacks"][1]:  #("shield bash", 50)
        hero["health"] -= 50
        print(f"{enemy_one['health']} health Melee Minion attacks Garen with Shield Bash for 50 dmg")
        garen_vs_melee_minion()     

# ---------------------------- Ranged Minion Strikes ---------------------------- 
# Melee Minion has been defeated at this point. Garen now faces Ranged Minion.
def ranged_minion_vs_garen():

    if enemy_two["health"] <= 0:
        print("Range Minion has been defeated and Garen collects his loot.")
        print(f"He collects Ranged Minion's equipment: {enemy_two['equipment']}")
        print(f"He collected Ranged Minion's money: {enemy_two['coins']}")
        hero["coins"]["copper"] += 9
        hero["coins"]["silver"] += 11
        hero["coins"]["gold"] += 14
        hero["equipment"].update(enemy_two["equipment"])
        hero["level"] += 1
        hero["abilities"] += (second_ability["abilities"])
        print("Our hero has leveled up from 16 to 17 and learned a new ability!")
        print("(Demacian Rage) - Garen's attacks passively deal +5 dmg")
        print(hero)
        cannon_minion_vs_garen()

    ranged_chosen_attack = random.choice(enemy_two["attacks"])

    if ranged_chosen_attack == enemy_two["attacks"][0]: # ("smite", 50)
        hero["health"] -= 45
        print(f"{enemy_two['health']} health Ranged Minion attacks Garen with Smite for 50 dmg -5")
        garen_vs_ranged_minion()

    if ranged_chosen_attack == enemy_two["attacks"][1]: #("focus", 75)
        hero["health"] -= 70
        print(f"{enemy_two['health']} health Ranged Minion attacks Garen with Focus for 75 dmg -5")
        garen_vs_ranged_minion()

# ---------------------------- Garen Strikes Ranged Minion ----------------------------
def garen_vs_ranged_minion():

    garen_chosen_attack = random.choice(hero["attacks"])

    if garen_chosen_attack == hero["attacks"][0]:   # ("decisive strike", 30)
        enemy_two["health"] -= 30
        print(f"{hero['health']} health Garen attacks Ranged Minion with Decisive Strike for 30 dmg")

    if garen_chosen_attack == hero["attacks"][1]:   # ("demacian justice spin", 40):   
        enemy_two["health"] -= 40                   # spin effects all enemies!
        enemy_three["health"] -= 40
        print(f"{hero['health']} health Garen attacks both enemies with Demacian Justice Spin for 40 dmg each")

    if garen_chosen_attack == hero["attacks"][2]:   # ("judgment", 50)
        enemy_two["health"] -= 50
        print(f"{hero['health']} health Garen attacks Ranged Minion with Judgment for 50 dmg")

    if enemy_two["health"] <= 0:        
        print("Range Minion has been defeated and Garen collects his loot.")
        print(f"He collects Ranged Minion's equipment: {enemy_two['equipment']}")
        print(f"He collected Ranged Minion's money: {enemy_two['coins']}")
        hero["coins"]["copper"] += 9
        hero["coins"]["silver"] += 11
        hero["coins"]["gold"] += 14
        hero["equipment"].update(enemy_two["equipment"])
        hero["level"] += 1
        hero["abilities"] += (second_ability["abilities"])
        print("Our hero has leveled up from 16 to 17 and learned a new ability!")
        print("(Demacian Rage) - Garen's attacks passively deal +5 dmg")
        print(hero)
        cannon_minion_vs_garen()

    if enemy_two["health"] > 0:
        ranged_minion_vs_garen()

# ---------------------------- Cannon Minion Strikes ---------------------------- 
# Melee Minion AND Ranged Minion have been defeated at this point. Garen now faces Cannon Minion.
def cannon_minion_vs_garen():

    cannon_chosen_attack = random.choice(enemy_three["attacks"])

    if cannon_chosen_attack == enemy_three["attacks"][0]:   # ("fire", 75)
        hero["health"] -= 70
        print(f"{enemy_three['health']} health Cannon Minion attacks Garen with Fire for 75 dmg -5")

    if cannon_chosen_attack == enemy_three["attacks"][1]:   # ("focus fire", 100)
        hero["health"] -= 95
        print(f"{enemy_three['health']} health Cannon Minion attacks Garen with Focus Fire for 100 dmg -5")

    if hero["health"] <= 0:
        print("Our hero has fallen in battle. The enemy minions were able to defend their nexus.")
        enemy_ending()

    if hero["health"] > 0:
        garen_vs_cannon_minion()

# ---------------------------- Garen Strikes Cannon Minion---------------------- 
def garen_vs_cannon_minion():

    garen_chosen_attack = random.choice(hero["attacks"])

    if garen_chosen_attack == hero["attacks"][0]:   # ("decisive strike", 30)
        enemy_three["health"] -= 35
        print(f"{hero['health']} health Garen attacks Cannon Minion with Decisive Strike for 30 dmg +5")

    if garen_chosen_attack == hero["attacks"][1]:   # ("demacian justice spin", 40)   
        enemy_three["health"] -= 45                 # spin effects all enemies
        print(f"{hero['health']} health Garen attacks Cannon Minion with Demacian Dustice Dpin for 40 dmg +5")

    if garen_chosen_attack == hero["attacks"][2]:   # ("judgment", 50)
        enemy_three["health"] -= 55
        print(f"{hero['health']} health Garen attacks Cannon Minion with Decisive Strike for 50 dmg +5")

    if enemy_three["health"] <= 0:
        print("Cannon Minion has been defeated and Garen collects his loot.")
        print(f"He collects Cannon Minion's equipment: {enemy_three['equipment']}")
        print(f"He collected Cannon Minion's money: {enemy_three['coins']}")
        hero["coins"]["copper"] += 12
        hero["coins"]["silver"] += 16
        hero["coins"]["gold"] += 20
        hero["equipment"].update(enemy_three["equipment"])
        hero["level"] += 1
        hero["abilities"] += (third_ability["abilities"])
        print("Our hero has reached max level of 18 and learned a new ability!")
        print("(Warlord's Infamy) - Half of all enemies flee from the sight of Garen.")
        print(hero)
        garen_ending()

    if enemy_three["health"] > 0:
        cannon_minion_vs_garen()

# ---------------------------------------- Endings ----------------------------------------
# Garen won. This is his ending.
def garen_ending():

    print("Our hero continues heading towards the enemy nexus as he passively heals to full heal along")
    print("the way. He reaches the defenses and shruggs off their attacks as he reduces them to piles of")
    print("rubble one after another. With all of the equipment, abilities and levels he has gained from")
    print("his enemies, he knows that he is unstoppable. The enemy obviously never expected anyone to")
    print("reach their base. Half the guards were low level and the other half threw down their weapons")
    print("and ran away. Our hero completed his mission and returned to Demacia a hero. He was celebrated")
    print("by his people and a statue was erected in his honor.")
    print("--------------- THE END ---------------")
    exit()

# Garen died. This is the alternate ending.
def enemy_ending():

    print("Cannon Minion climbed down from his cannon and stood over garen as he chuckled and looted his")
    print("body. He returned to his base a hero and modified his newly aquired equipment to suit himself.")
    print("He then purchase some equipment for his empty item slots, waited for another Melee Minion and")
    print("Ranged Minion to spawn and returned to the battle field to scount for more enemies. His newly")
    print("looted and purchased equipment made him stronger than ever. Our next brave challenger would be")
    print("in for an even tougher battle than Garen could handle.")
    print("--------------- THE END... UNFORTUNATELY... ---------------")
    exit()

# ---------------------------------------- Calling All Functions ----------------------------------------
def run_game():

    hero_attacks_enemy_one = garen_vs_melee_minion()
    enemy_one_attacks_hero = melee_minion_vs_garen()
    enemy_two_attacks_hero = ranged_minion_vs_garen()
    hero_attacks_enemy_two = garen_vs_ranged_minion()
    enemy_three_attacks_hero = cannon_minion_vs_garen()
    hero_attacks_enemy_three = garen_vs_cannon_minion()
    garen_victory = garen_ending()
    enemy_victory = enemy_ending()

run_game()