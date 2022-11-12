"""
---------- Basic GIT Commands ----------
-git clone => allows you to get a repo from the server and copy it to your device.
-git status => allows you to see the current status of your project.
-git add . => allows you to add new files to your tracker and stage them to be commited.
-git commit -m "Descriptive Message" => 
    -Backup/Bookmark
    -Grouping of differences (diffs)
    -Stored by Repository a.k.a. repo for short.
    -Commit as often as possible.
    -Always use professional descriptive messages. No more than what you would write on a post-it note.
-git pull => allows you to make sure your code includes your teammate's code.
-git push => allows you to send your changes to the server.
    ---------- Example ----------
    "git add" is like getting everyone together for a picture.
    "git commit" once everyone is together, the picture is taken.
        "Descriptive Message" is what you would write on the picture for context. (for example "New Years 2000")
"""

soda_machine = {
    'cans': [
        {
            'type': 'grape',
            'quantity': 10,
            'cost': 0.50
        },
        {
            'type': 'cola',
            'quantity': 10,
            'cost': 0.50
        },
    ],
    'coins': {
        'quarters': 30,
        'dimes': 40,
        'nickels': 50
    },
    'accepts_credit_card': True
}


print(soda_machine['cans'][0]['type'])
print(soda_machine['cans'][0]['cost'])

soda_machine['cans'][0]['cost'] += 0.10

print(soda_machine['cans'][0]['cost'])

for soda in soda_machine['cans']:
    print(f'{soda["type"]} - ${soda["cost"]}')

soda_machine['coins']['quarters'] += 2

soda_machine['accepts_credit_card'] = False

print(soda_machine)
# --------------------  -------------------- -------------------- --------------------
# -------------------- Another Example in video at 11:35 car = {} --------------------
# --------------------  -------------------- -------------------- --------------------


import random

print("------------------------------------------------------------------------------")
print("Let me help you plan your day trip! Let's start with your desired destination.")
print("------------------------------------------------------------------------------")

def choose_destination():
    # ---------------------------- Destinations Loop ---------------------------- 
    destinations = ["Goodneighbor", "Diamond City", "Sanctuary Hills"]
    chosen_destination_scoped = random.choice(destinations)
    input_destinations = input(f"How does '{chosen_destination_scoped}' sound for your destination? ")

    valid_respons = False
    while valid_respons == False:

        if input_destinations == "yes":
            print(f"Excellent choice, I hear {chosen_destination_scoped} is beautiful this time of year!")
            valid_respons = True
        elif input_destinations == "no":
            chosen_destination_scoped = random.choice(destinations)
            input_destinations = input(f"How does '{chosen_destination_scoped}' sound for your destination? ")
        else:
            print("I'm so sorry, I didnt catch that. Please enter yes or no ")
            input_destinations = input(f"How does '{chosen_destination_scoped}' sound for your destination? ")

    print(f'Awesome, you have finalized {chosen_destination_scoped} as your desired destination!')
    return chosen_destination_scoped

def choose_restaurant():
    # ---------------------------- Restaurants Loop ---------------------------- 
    print("------------------------------------------------")
    print("Let's see if we can find you a great restaurant!")
    print("------------------------------------------------")

    restaurants = ["Slocum Joe's", "Cambridge Campus Diner", "Power Noodles"]
    chosen_resaurant_scoped = random.choice(restaurants)
    input_restaurants = input(f"How does '{chosen_resaurant_scoped}' sound for your restaurant? ")

    valid_respons = False
    while valid_respons == False:

        if input_restaurants == "yes":
            print(f"I LOVE eating at {chosen_resaurant_scoped}! Their whole menu is amazing!")
            valid_respons = True
        elif input_restaurants == "no":
            chosen_resaurant_scoped = random.choice(restaurants)
            input_restaurants = input(f"How does '{chosen_resaurant_scoped}' sound for your restaurant? ")
        else:
            print("I'm so sorry, I didnt catch that. Please enter yes or no ")
            input_restaurants = input(f"How does '{chosen_resaurant_scoped}' sound for your restaurant? ")

    print(f'Awesome, you have finalized {chosen_resaurant_scoped} as your desired restaurant!')
    return chosen_resaurant_scoped

def choose_transportation():
    # ---------------------------- Transportations Loop ---------------------------- 
    print("-------------------------------------------")
    print("Let's get you a ride to your entertainment!")
    print("-------------------------------------------")

    transportations = ["Fast Travel", "Vertibird", "Power Armor"]
    chosen_transportation_scoped = random.choice(transportations)
    input_transportations = input(f"How does '{chosen_transportation_scoped}' sound for your transportation? ")

    valid_respons = False
    while valid_respons == False:

        if input_transportations == "yes":
            print(f"I've heard that traveling by {chosen_transportation_scoped} is very fun! I know you will enjoy it!")
            valid_respons = True
        elif input_transportations == "no":
            chosen_transportation_scoped = random.choice(transportations)
            input_transportations = input(f"How does '{chosen_transportation_scoped}' sound for your destination? ")
        else:
            print("I'm so sorry, I didnt catch that. Please enter yes or no ")
            input_transportations = input(f"How does '{chosen_transportation_scoped}' sound for your destination? ")

    print(f'Awesome, you have finalized {chosen_transportation_scoped} as your desired transportation!')
    return chosen_transportation_scoped

def choose_entertainment():
    # ---------------------------- Entertainments Loop ---------------------------- 
    print("----------------------------------------------------")
    print("Let's find you the BEST entertainment for your trip!")
    print("----------------------------------------------------")
        
    entertainments = ["Starlight Drive-In", "Dugout Inn", "Museum of Witchcraft"]
    chosen_entertainment_scoped = random.choice(entertainments)
    input_entertainments = input(f"How does '{chosen_entertainment_scoped}' sound for your entertainment? ")

    valid_respons = False
    while valid_respons == False:

        if input_entertainments == "yes":
            print(f"My friends and I went to the {chosen_entertainment_scoped} last year and we had a blast!")
            valid_respons = True
        elif input_entertainments == "no":
            chosen_entertainment_scoped = random.choice(entertainments)
            input_entertainments = input(f"How does '{chosen_entertainment_scoped}' sound for your destination? ")
        else:
            print("I'm so sorry, I didnt catch that. Please enter yes or no ")
            input_entertainments = input(f"How does '{chosen_entertainment_scoped}' sound for your destination? ")

    print(f'Awesome, you have finalized {chosen_entertainment_scoped} as your desired entertainment!')
    return chosen_entertainment_scoped

# ---------------------------- User Choices Confirmation ---------------------------- 
def plan_itinerary():

    chosen_destination = choose_destination()
    chosen_restaurant = choose_restaurant()
    chosen_transportation = choose_transportation()
    chosen_entertainment = choose_entertainment()

    final_trip = {"destination": [chosen_destination], "restaurant": [chosen_restaurant], "transprtation": [chosen_transportation], "entertainment": [chosen_entertainment]}
    user_choices = final_trip.items()

    print(f"Looks like you're all set! Here is your completed itinerary. It includes...")

    valid_respons = False
    while valid_respons == False:
        final_trip = {"destination": [chosen_destination], "restaurant": [chosen_restaurant], "transprtation": [chosen_transportation], "entertainment": [chosen_entertainment]}

        for key, value in final_trip.items():
            print("")
            print(f"The desired {key} chosen was {value}")
            print("")

        def final_confirmation():

            input_choices_confirmation = input(f"Are you satisfied with your completed itinerary? ")
            if input_choices_confirmation == "yes":
                print("Great, it was my pleasure helping you plan your trip! Have fun.")
                valid_respons = True
                exit()
            elif input_choices_confirmation == "no":
                input_choices_confirmation = input("That's ok, which part of your trip would you like to edit? Please enter D for Destination, R for Restaurant, T for Transportation, E for Entertainment or A for All of it. ")
                if input_choices_confirmation == "D":
                    chosen_destination = choose_destination()
                elif input_choices_confirmation == "R":
                    chosen_restaurant = choose_restaurant()
                elif input_choices_confirmation == "T":
                    chosen_transportation = choose_transportation()
                elif input_choices_confirmation == "E":
                    chosen_entertainment = choose_entertainment()
                elif input_choices_confirmation == "A":
                    print("That's ok! Let's just start from the beginning.")
                    plan_itinerary()
                else:
                    print("I'm so sorry, I didnt catch that. Please enter D for Destination, R for Restaurant, T for Transportation, E for Entertainment or A for All of it.")
                    input_choices_confirmation = input("Which part of your trip would you like to edit? ")
            else:
                print("I'm so sorry, I didnt catch that. Please enter yes or no ")
                final_confirmation()

        final_confirmation()

plan_itinerary()

# --------------------  -------------------- -------------------- --------------------


best_football_team = input("Who is the best football team? ")

valid_respons = False

while valid_respons == False:

    if best_football_team == "Bears":
        print("Quarterback much?")
        valid_respons = True
    elif best_football_team == "Vikings":
        print("Loud noises!")
        valid_respons = True
    elif best_football_team == "Lions":
        print("They bad!")
        valid_respons = True
    elif best_football_team == "Packers":
        print("Best team in the world! Actually, the universe!")
        valid_respons = True
    else:
        print("They don't stand a chance!")
        valid_respons = True
