# enums.py
from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class GameState(Enum):
    STARTING = 1
    RUNNING = 2
    PAUSED = 3
    GAMEOVER = 4
