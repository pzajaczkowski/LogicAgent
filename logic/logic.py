import pygame

from logic.level import *
from logic.statemenu import StateMenu
from logic.stategame import StateGame

TER_LINES = 22
TER_COLS = 58


class Logic:

    _difficulty = 1  # 0 - easy 1 - normal 2 - hard
    _player_skin = 0  # 0 - default
    _selected_level = 0

    def __init__(self, gui):
        self._state = 10  # initial state = menu
        self._levels = []
        self._load_levels()
        self._gui = gui

    def loop(self):
        pygame.init()
        state_menu = StateMenu(self._gui)
        while self._state != 3:
            new_state = 10  # Menu
            match self._state:
                case 10:  # Menu
                    new_state = state_menu.loop_menu()
                case 0:  # Play
                    self._selected_level = state_menu.loop_level(self._levels)
                    state_game = StateGame(self._gui, self._difficulty, self._levels[self._selected_level], self._player_skin)
                    state_game.loop()
                case 1:  # Difficulty
                    self._difficulty = state_menu.loop_difficulty(self._difficulty)
                case 2:  # Player skin
                    self._player_skin = state_menu.loop_skin(self._player_skin)
                case 3:  # Exit
                    return
            self._state = new_state

    def _load_levels(self):
        self._levels = getlevels()
