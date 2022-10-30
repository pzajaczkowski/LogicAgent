TER_LINES = 22
TER_COLS = 58

WHITE = 0
BLACK = 3
BLUE = 22
BLUE_DIM = 18
GREEN = 47
PURPLE = 58
RED = 197
YELLOW = 227
YELLOW_DIM = 7
ORANGE = 203
ORANGE_DIM = 131
MAGENTA = 202
MAGENTA_DIM = 54
LIME = 155
CYAN = 52
LIGHT_BLUE = 28

PLAYER = '℗'
WALL = '█'
STAR = '✦'
SPIKES = '✶'
BLANK = ' '
BLANKV1 = '⠀'
RIGHT_ARROW = '→'
LEFT_ARROW = '←'
DOWN_ARROW = '↓'
UP_ARROW = '↑'


menu_elements = ["PLAY", "DIFFICULTY", "CHANGE PLAYER SKIN", "EXIT"]
difficulty_elements = ["CURRENT = ", "EASY", "MEDIUM", "HARD", "RETURN"]
skins = ['℗', '@', '₳', '◊', '╪', '¶', '§']

empty_line = "                                                        "  # 56 x space (58-2)

all_elements = [menu_elements, difficulty_elements]

title = [
    r" ___       ________  ________  ___  ________           ",
    r"|\  \     |\   __  \|\   ____\|\  \|\   ____\          ",
    r"\ \  \    \ \  \|\  \ \  \___|\ \  \ \  \___|          ",
    r" \ \  \    \ \  \\\  \ \  \  __\ \  \ \  \             ",
    r"  \ \  \____\ \  \\\  \ \  \|\  \ \  \ \  \____        ",
    r"   \ \_______\ \_______\ \_______\ \__\ \_______\      ",
    r"    \|_______|\|_______|\|_______|\|__|\|_______|      ",
    r" ________  ________  _______   ________   _________    ",
    r"|\   __  \|\   ____\|\  ___ \ |\   ___  \|\___   ___\  ",
    r"\ \  \|\  \ \  \___|\ \   __/|\ \  \\ \  \|___ \  \_|  ",
    r" \ \   __  \ \  \  __\ \  \_|/_\ \  \\ \  \   \ \  \   ",
    r"  \ \  \ \  \ \  \|\  \ \  \_|\ \ \  \\ \  \   \ \  \  ",
    r"   \ \__\ \__\ \_______\ \_______\ \__\\ \__\   \ \__\ ",
    r"    \|__|\|__|\|_______|\|_______|\|__| \|__|    \|__| "]

dead_screen = [
    r" ________  _______   ________  ________                ",
    r"|\   ___ \|\  ___ \ |\   __  \|\   ___ \               ",
    r"\ \  \_|\ \ \   __/|\ \  \|\  \ \  \_|\ \              ",
    r" \ \  \ \\ \ \  \_|/_\ \   __  \ \  \ \\ \             ",
    r"  \ \  \_\\ \ \  \_|\ \ \  \ \  \ \  \_\\ \            ",
    r"   \ \_______\ \_______\ \__\ \__\ \_______\           ",
    r"    \|_______|\|_______|\|__|\|__|\|_______|           ",
    r" ________  ________  _______   ________   _________    ",
    r"|\   __  \|\   ____\|\  ___ \ |\   ___  \|\___   ___\  ",
    r"\ \  \|\  \ \  \___|\ \   __/|\ \  \\ \  \|___ \  \_|  ",
    r" \ \   __  \ \  \  __\ \  \_|/_\ \  \\ \  \   \ \  \   ",
    r"  \ \  \ \  \ \  \|\  \ \  \_|\ \ \  \\ \  \   \ \  \  ",
    r"   \ \__\ \__\ \_______\ \_______\ \__\\ \__\   \ \__\ ",
    r"    \|__|\|__|\|_______|\|_______|\|__| \|__|    \|__| "
]
