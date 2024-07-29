# Pong Game in Python

This project is a simple implementation of the classic Pong game using Python's `turtle` module. The game simulates the classic arcade Pong game where two players control paddles to hit a ball back and forth across the screen.

## Features

- Two-player game
- Paddle movement controls
- Ball movement with collision detection
- Scoring system

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. This project requires Python 3.x. You can download Python from the official website: [python.org](https://www.python.org/downloads/).

### Installation

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/pong-game-python.git
```

### Run the game
```bash
python pong_game.py
```

## Game Controls

### Right Paddle:
- **Move Up:** Press the "Up" arrow key
- **Move Down:** Press the "Down" arrow key

### Left Paddle:
- **Move Up:** Press the "W" key
- **Move Down:** Press the "S" key

## Game Rules

- The ball bounces off the top and bottom walls.
- The ball bounces off the paddles.
- When the ball passes the right paddle, the left player scores a point.
- When the ball passes the left paddle, the right player scores a point.
- The game does not currently have a win condition; it's purely for fun.
