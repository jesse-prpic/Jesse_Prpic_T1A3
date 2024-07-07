# Term 1 Assignment 3 - Terminal Application
# Six-Letter Word Game

## Overview
A terminal application inspired by the game "WORDLE".
This infrastructure will interact with different features and data.
Throughout the project I will demonstrate my skills by showcasing this through technical knowledge.

## Objective 
It allows the player to guess a six-letter word over a duration of 8 guesses - with the scoring model being whether they win and guess the word under 8 guesses or lose by not guessing the word.
Once the player guesses the word or they fail at doing so, this will be put into a scoreboard to show their successes and loses.

## Features
The features that I have displayed are;

### Menu Operations
- Having multiple options when the player starts to either play, add player, see scoreboard and also to exit the game

### Add Player
- Before each game starts, you are able to either start the game and play using an existing player, or you are able to add a player.
- This will allow each player to put in their name, select their name and play with the results being put on the scoreboard through a percentile, being able to see each players score.

### 2500 WORDS 
- This game offers 2500 of all the words in the english language, with having that many words the game can last for thousands of rounds without the same word being chosen again.
- Only the words in the sixletterwords.txt file will be valid.

### Instructions
- Before playing each game, it is important that players understand the rules as this will provide tips for the player on the positioning of the previous words they have guessed.

### Color Indicators
- Green: To display that the letter of the word that you have chosen is correct position.
- Yellow: To display that the letter of the word that you have chosen is in the word, however not in the correct position.
- White: To display the letter is not in the word.

### Guessing Panel
- A panel has been created to show the player how the letters are places, the color they indicate and how many attempts they will have left.
    - This creates a feature for the player to visualise the game in a more appealing way

![alt text](<data/Guessing Panel.png>)

### Scoreboard
- Scoring will be done is two ways;
    - Percentage;
        - How successful the player has been with getting the word
    - Win or lose
        - How many times someone has won or lost the game


## Implementation Plan

### Project Management Board - Trello
Project management is important amongst all industries, however this is particularly important when there is an important deadline and if you are working in a team.
Project management board are a great way for yourself and the team to be accountable in what steps people are doing to be sure they achieve the end result.

Its great to start at the beginning of the project and the utilise it throughout and add to it if necessary.

I used Trello to do mine, please see below to check it out.

Trello Board
![alt text](<data/TRELLO_BOARD.png>)

### Flowchart
A flowchart is important to contexualise what is happening with the actual code of the terminal application and have a visual conetation to this.

Throughout this implementation plan I have made a flowchart conceptualising this where you can see it below.

#### FLOW CHART LEGENDS:
- Circle: Start / Stop
- Square: Functions
- Triangle: Print
- Elongated Hexagon: Exit/Break
- Star: Loop
- Right-Leaning Parallelagram: If conditions
- Left-Leaning Parallelagram: Elif conditions
- Diamond: Else conditions
- Arrow: Flow

![alt text](<data/Flowchart.png>)

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fboard%2FZgTfT6PwpQSEgNo92No7bX%2FSIX-LETTER-WORD-GAME%3Fnode-id%3D0-1%26t%3DIiUX5zujBBSg9R3k-1" allowfullscreen></iframe>



## Help Documentation

The "Word Game" is a terminal application based game where players guess a hidden six-letter word within a limited number of attempts, this includes several features:
- player management
- scoreboard tracking
- color feedback for each guess

Instructions to start playing the game
- Select "Start New Game" from the menu
- Choose a player form the existing list or add a new player
- Instruction on the game will be displayed

The game play
- Guess a 6 letter word - make sure this is on CAPS LOCK
- Each guess will result in a color
    - Green, Yellow and White - These will indicate whether the letter is in the correct position, or that the letter is in the wrong positon - otherwise the letter is not in the word, respective allocation to the indicators.

The Scoreboard
- Displays players game statistics whether they have won or lost and will have a percentile

Once all dependencies are installed, you will need the following code to interact with the terminal application

"python3 src/lets_play.py"

### Installation

Clone the respository
- This is necessary for users who want to install and run "Word Game"

Code 
"git clone https://github.com/

Change Directory to the folder containing the application

Install dependencies
"pip install -r requirements.txt"


If dependencies do not work, please see the below on the dependencies and their requirements

#### Dependencies and requirements

python 3.6 or higher

Most people will have Python already installed; however great to check:

To check
python3 --version

If you do not have python3 installed, please see the following link to install dependant on your operating system:
https://wsvincent.com/install-python/#install-python-on-macos

_______________

colorama v0.4.6

To install
"pip install colorama"

_______________

pep8

To install
"pip install pep8"
To upgrade
"pip install --upgrade pep8

If needing to uninstall
"pip uninstall pep8"

_______________

autopep8

Install
pip install --upgrade autopep8


## Resources

- w3school
https://www.w3schools.com/python/default.asp

- Medium
https://medium.com/pythons-gurus/a-beginners-guide-on-how-to-build-a-simple-python-application-with-a-command-line-interface-6d7fb187789b

- PyPi
https://pypi.org

### Other noted resources
- Trello
- Figma / Draw.io
- Codecademy
- Class recording

## For more information
For more information on this project, you can find this through my Github repository https://github.com/jesse-prpic/JessePrpicPortfolioSite

## Project Author
Jesse Prpic

## Source Controls
As of submitting this project there has been 29