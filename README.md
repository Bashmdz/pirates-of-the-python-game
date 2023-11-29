# Pirates of the Python

## Contents

* [User Experience (UX)](#user-experience-ux)
  * [User Goals](#user-goals)

* [Design](#design)
  * [Flowchart](#flowchart)

* [How to Play](#how-to-play)

* [Features](#features)
  * [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)

* [Deployment & Local Deployment](#deployment--local-development)

* [Testing](#testing)

* [Credits](#credits)


## User Experience (UX)

### Initial Discussion

- This program is a pirate-themed version of the classic Battleship game called "Pirates of the Python.".

#### User Goals

-  In this game, the user's goal is to strategically choose coordinates and sink the computer's battleships before the computer sinks user's ships. It's a playful twist on the classic Battleship game.

## Design

#### Flowchart

![PiratesOfThePython-flowchart](README-images/flowchart.png)

## How to Play

"Pirates of the Python" follows the classic gameplay of the game "Battleship." At the main menu, the user can choose to start the game, display rules, or exit the game. Once the game begins, a set of randomly generated ships will be displayed for the user and the computer. The user will also see a blank board for reference.

During the user's turn, they will choose a row and a column. The grid will be updated to reflect hits ('!') or misses ('X'). The first to sink all the opponent's battleships wins the game. After the game, the user has the option to play again.

Live version of the game can be found here: [Pirates of the Python](https://pirates-of-the-python-908715cee4da.herokuapp.com/)

## Features

Additionally, players can personalize their experience by choosing a pirate name. They also have the flexibility to set the grid size between 3 and 8 for added customization.

### Start Screen

At the start of the game, players are greeted with the "Pirates of the Python" logo set against a pirate-themed background. Below the logo, a menu offers the following options:


1. Display Rules
2. Start Game
3. Exit Game

 ![Start-Screen1](README-images/main-screen.png)

### Display Rules

Display Rules when user choose 1.

![Game-Rules](README-images/display-rules.png)

### Start Game

Start Game when user choose 2

![Start-Game](README-images/start-game.png)

### Choosing Grid Size

Let user choose Grid size for the game, and show the board.

![Grid-Size](README-images/choose-grid-size.png)

![Show-Board](README-images/show-board.png)

### Choosing Row & Column

Let user choose column & row and show results on board.

![Row-Column-Choice](README-images/choose-row-colum-&-show-results.png)

### Draw - Attempts used

Result a draw, if user uses all attempts.

![User-Win](README-images/draw.png)

### User Wins

Result a win, if user hit all computer battleships.

![User-Win](README-images/win.png)

### Computer Wins

Result a lose, if computer wins.

![User-Win](README-images/lose.png)

#### Future Implementations

I might incorporate a scoring system for the player and potentially allow them to manually choose the positions of their battleships.

## Technologies Used

### Languages and Python Packages/Libraries Used

### Frameworks and Programs Used

## Deployment

## Testing

### Validation Checks

## Bugs

### Resolved Bugs

### Unresolved Bugs

## Credits

## Acknowledgements