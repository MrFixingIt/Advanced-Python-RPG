import sys
import time

def slow_print(string_to_print):
	for letter in string_to_print:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.06)
	print("")

narrator_dialog = "------------------------------ Narrator ------------------------------"
hero_dialog = " ------------------------------ Garen ------------------------------ "
melee_minion_dialog = " ------------------------------ Melee Minion ------------------------------ "
ranged_minion_dialog = " ------------------------------ Ranged Minion ------------------------------ "
cannon_minion_dialog = " ------------------------------ Cannon Minion ------------------------------ "

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
