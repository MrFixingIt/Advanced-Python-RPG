"""
Main Stories

(5 points): As a data analyst, I want to make at least five commits on GitHub with descriptive messages.  
(2.5 points): As a user, I want an engaging story to be told using print() statements.  
(2.5 points): As a data analyst, I want to create a hero variable and set it equal to a Dictionary with the following keys and values. NOTE: The structure below indicates the name of the key on the left side of the colon and the value on the right side of the colon. 
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

(2.5 points): As a data analyst, I want to create THREE enemy variables and set each equal to a Dictionary with the following keys and values. NOTE: The structure below indicates the name of the key on the left side of the colon and the value on the right side of the colon. 
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

(5 points): As a user, I want my Hero and Enemy's attack to be chosen at random. 
(5 points): As a user, I want my Hero or Enemy's health to decrease based on the power of the successful attack. 
(2.5 points): As a user, I want the results of each attack to be printed to the terminal.
(5 points): As a user, I want the Hero and Enemy to continue attacking each other until one's health reaches zero.  
(5 points): As a user, I want to be able to “loot” defeated enemies by adding the Enemy's equipment set to the Hero's equipment Set
(5 points): As a data analyst, I want the game to conclude when the Hero's health reaches 0, or when all three Enemies have been defeated.   
(2.5 points): As a data analyst, I want to create a run_game() function, which calls my other functions in a logical order to determine the game's flow. 
(5 points): As a data analyst, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!  

Bonus Stories
(5 points): As a user, I want to “loot” defeated enemies by adding the Enemy's gold, silver, and copper coins to the appropriate value in the Hero's coin Dictionary.

(7.5 points): As a user, I want to increase my Hero's level after defeating an Enemy, which will include: 
Incrementing my Hero's level by 1 
Adding a new attack of my choosing to my Hero's Attack Tuple. 
Checklist

Run through the Setup Steps and get your project ready to begin work.
Review the Resources outlined below - be sure to have relevant documentation and references open while you develop!
NOTE:  Make sure to TEST all of your code as you go along! This becomes more critical as your projects grow in size and complexity.

Setup Steps
Create a GitHub repository on GitHub. Remember to use a Python .gitignore and add a README file! 
Clone your repository down to your computer
Create your project in Visual Studio Code and move the invisible .git folder and README file to the folder where your project is located. 
Make a test commit and check your repository to be sure the content has updated! 
Begin by creating your Hero and Enemy dictionary variables, using the following screenshots as a reference.  Feel free to get creative with your Hero & Enemy values to create your own unique RPG experience! 
Start coding the program first by going from the top of the user stories and working down. Decide how you will: 
Randomly select a  Hero's attack
Randomly select an Enemy's attack 
Decrement the Hero and Enemy's health accordingly 
Repeat the process until the Hero or Enemy loses all of their health 
Once you are able to have your Hero and Enemy attack one another, start thinking about how you will handle the post-battle functionality, including: 
Printing a message declaring the winner
“Looting” the defeated enemy's equipment
Repeating the same battle process for the other two enemies 
Be sure to test your code as you complete each function! 


"""