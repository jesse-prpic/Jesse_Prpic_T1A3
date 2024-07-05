# Term 1 Assignment 3 - Terminal Application
# Six-Letter Word Game

## Overview
A terminal application inspired by the game "WORDLE".
This infrastructure will interact with different features and data.

## Objective 
It allows the player to guess a six-letter word over a duration of 8 guesses - with the scoring model being whether they win and guess the word under 8 guesses or lose by not guessing the word.
Once the player guesses the word or they fail at doing so, this will be put into a scoreboard to show their successes and loses.

## Features
The features that I have displayed are;

### Color Indicators
- Green: To display that the letter of the word that you have chosen is correct position.
- Yellow: To display that the letter of the word that you have chosen is in the word, however not in the correct position.
- White: To display the letter is not in the word.

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

┏══════════════════════════════════════┓
║    L     E     T     T     E     R   ║
║    _     _     _     _     _     _   ║
║    _     _     _     _     _     _   ║
║    _     _     _     _     _     _   ║
║    _     _     _     _     _     _   ║
║    _     _     _     _     _     _   ║
║    _     _     _     _     _     _   ║
║    _     _     _     _     _     _   ║
┗══════════════════════════════════════┛

### Scoring
- Scoring will be done is two ways;
    - Percentage;
        - How successful the player has been with getting the word
    - Win or lose
        - How many times someone has won or lost the game

### Add player
- Having the ability to be able to do it in hard mode, instead of the player being able to guess any word, they will either need to;
    - If there is a letter that has been used and it is grey, they are unable to use it again
    - If there is a letter that is green or blue, they are needing to use this letter.
        - the objective of this is for the user to not be able to use a filler word.


## Implementation Plan

### Trello
This should outline:
- Implemented and a checklist of tasks for each feature
- Implementation of different features, or checklist items within a feature
- Provide a deadline, duration or time indicator for each feature or checklist/checklist-item

### Flowchart

###

## Help Documentation

### Steps to installe the application
#### Dependencies and requirements

#### Any command line arguments made for the application