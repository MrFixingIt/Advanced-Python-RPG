# Advanced-Python-RPG

This is a project I put together for fun that was influenced by League of Legends and World of Warcraft. Below are the guidelines for this project.

1. As a user, I want an engaging story to be told using print() statements. 

2. As a data analyst, I want to create a hero variable and set it equal to a Dictionary with the following keys and values. (name:Value)
    hero: Dictionary 
    name: String 
    level: Integer 
    health: Integer 
    equipment: Set of Strings 
    attacks: Tuple of Tuples (each Tuple will have (attack_name: String, attack_power: Integer) 
    coins: Dictionary 
    copper: Integer 
    silver: Integer 
    gold: Integer 

3. As a data analyst, I want to create THREE enemy variables and set each equal to a Dictionary with the following keys and values. NOTE: The structure below indicates the name of the key on the left side of the colon and the value on the right side of the colon. (name:Value)
    enemy: Dictionary 
    name: String 
    level: Integer 
    health: Integer 
    equipment: Set of Strings 
    attacks: Tuple of Tuples (each Tuple will have (attack_name: String, attack_power: Integer) 
    coins: Dictionary 
    copper: Integer 
    silver: Integer 
    gold: Integer 

4. As a user, I want my Hero and Enemy’s attack to be chosen at random. 

5. As a user, I want my Hero or Enemy’s health to decrease based on the power of the successful attack. 

6. As a user, I want the results of each attack to be printed to the terminal.

7. As a user, I want the Hero and Enemy to continue attacking each other until one's health reaches zero. 

8. As a user, I want to be able to “loot” defeated enemies by adding the Enemy’s equipment set to the Hero’s equipment Set

9. As a data analyst, I want the game to conclude when the Hero’s health reaches 0, or when all three Enemies have been defeated.   

10. As a data analyst, I want to create a run_game() function, which calls my other functions in a logical order to determine the game’s flow. 

11. As a data analyst, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!  

12. As a user, I want to “loot” defeated enemies by adding the Enemy’s gold, silver, and copper coins to the appropriate value in the Hero’s coin Dictionary.

13. As a user, I want to increase my Hero’s level after defeating an Enemy, which will include: 
    Incrementing my Hero’s level by 1 
    Adding a new attack of my choosing to my Hero's Attack Tuple. 
