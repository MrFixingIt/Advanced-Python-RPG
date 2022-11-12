
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

hero["coins"]["copper"] += 3
hero["coins"]["silver"] += 4
hero["coins"]["gold"] += 5
hero["level"] += 1
hero["abilities"] = ("courage", -5)

# print(hero["coins"])
# print(hero["level"])
# print(hero["attacks"])
# print(hero["abilities"])
# print(hero["health"])
