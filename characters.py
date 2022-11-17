hero = {
    "name": "Garen",
    "level": 15,
    "health": 500,
    "equipment": {"shoulder plates","chest plate","armored leggings","long sword"},
    "attacks": (("decisive strike", 30), ("demacian justice spin", 40), ("judgment", 50)),
    "coins": {"copper": 5, "silver": 3, "gold": 1}
}

enemy_one = {
    "name": "Melee Minion",
    "level": 10,
    "health": 180,
    "equipment": {"short sword",  "shield", "chain mail armor"},
    "attacks": (("swing", 25), ("shield bash", 50)),
    "coins": {"copper": 6, "silver": 5, "gold": 4}
}

enemy_two = {
    "name": "ranged minion",
    "level": 11,
    "health": 140,
    "equipment": {"wand", "dark seal necklace", "hooded cloak"},
    "attacks": (("smite", 50), ("focus", 75)),
    "coins": {"copper": 9, "silver": 11, "gold": 14}
}

enemy_three = {
    "name": "cannon minion",
    "level": 12,
    "health": 200,
    "equipment": {"binoculars", "hooded cloak", "cannon mount"},
    "attacks": (("fire", 75), ("focus fire", 100)),
    "coins": {"copper": 12, "silver": 16, "gold": 20}
}

second_ability = {
    "name": "number two",
    "abilities": ("demacian rage", +5)
}

third_ability = {
    "name": "number three",
    "abilities": ("Warlord's Infamy", 0)
}

hero["abilities"] = ("courage", -5)

# first_ability = {
#     "name": "number one",
#     "abilities": ("courage", -5)
# }

# hero["abilities"] += (second_ability["abilities"])

# hero["equipment"].update(enemy_one["equipment"])    # prints all 7 pieces of equipment

# print(hero["abilities"])

