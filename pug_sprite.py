import time
from os import system

class Shape():
    def __init__(self, lines):
        self.lines = lines
    def add_spaces(self, spaces):
        new_lines = []
        for line in self.lines:
            new_lines.append(" " * spaces + line)
        greater_than_125 = False
        for line in new_lines:
            if len(line) > 125:
                greater_than_125 = True
        self.lines = new_lines
        return greater_than_125
    def remove_spaces(self, spaces):
        new_lines = []
        for line in self.lines:
            if line[:spaces] == " " * spaces:
                new_lines.append(line[spaces:])
        self.lines = new_lines
    def print_shape(self):
        for line in self.lines:
            print(line)

class Sprite():
    def __init__(self, shapes):
        self.shapes = shapes
    def change_all(self, amount_to_change):
        greater_than_125 = False
        for shape in self.shapes:
            if amount_to_change > 0:
                greater_than_125 = shape.add_spaces(amount_to_change)
            elif amount_to_change < 0:
                shape.remove_spaces(amount_to_change)
        return greater_than_125
    def cycle_print_shapes(self, list_of_indices, sleep_time):
        for index in list_of_indices:
            system("clear")
            self.shapes[index].print_shape()
            time.sleep(sleep_time)
    def print_a_shape(self, shape_index):
        shape_to_print = self.shapes[shape_index]
        for line in shape_to_print.lines:
            print(line)

def make_walk(sprite, play_ending):
    while True:
        sprite.cycle_print_shapes([0, 1, 0, 2], .05)
        if sprite.change_all(3):
            break
    if play_ending:
        sprite.cycle_print_shapes([3, 4, 3, 4], .2)
        system("clear")
        sprite.print_a_shape(5)

def get_new_shape(shapes):
    lines = ["", "", "", "", "", "", "", "", "", "", ""]
    for shape in shapes:
        if len(lines[-1]) > 0:
            longest_line = 0
            for line in lines:
                if len(line) > longest_line:
                    longest_line = len(line)
            desired_length = longest_line + 5
            for index in range(len(lines)):
                lines[index] = lines[index] + " " * (desired_length - len(lines[index]))
        for index in range(len(lines)):
            lines[index] = lines[index] + shape.lines[index]
    return Shape(lines)

def get_new_sprite(sprites):
    if len(sprites) == 1:
        return Sprite(sprites[0].shapes)
    elif len(sprites) > 1:
        shape1 = []
        shape2 = []
        shape3 = []
        for sprite in sprites:
            shape1.append(sprite.shapes[0])
            shape2.append(sprite.shapes[1])
            shape3.append(sprite.shapes[2])
        new_shapes = []
        new_shapes.append(get_new_shape(shape1))
        new_shapes.append(get_new_shape(shape2))
        new_shapes.append(get_new_shape(shape3))
        return Sprite(new_shapes)

if True: # pug shapes
    pug1 = Shape([
        "                  _______",
        "    ___          /\  /   \\",
        "   /   \        /  \/ O __\\",
        "  |  \_/       /      /   |",
        "   \__________/       |__/",
        "   |                  /",
        "   |                 /",
        "   |   /            /",
        "   |  /\________/| |",
        "   | |           | |",
        "   |_|           |_|"])
    pug2 = Shape([
        "   __             _______",
        " /    \          / \ |   \\",
        "|      |        /   \|- __\\",
        "|   \_/        /      /   |",
        " \____________/       |__/",
        "  \                   /",
        "  |                  /",
        "  |    /            /",
        "   \  /\________/\ \\",
        "    \ \\          \ \\",
        "     \_\\          \_\\"])
    pug3 = Shape([
        "                  _______",
        "                 /| /    \\",
        "       __       / |/  O __\\",
        "     / _/      /      /   |",
        "    |_________/       |__/",
        "    /                 /",
        "   |                 /",
        "   |   /            /",
        "   / _/\_________/ /",
        "  / /           / /",
        " /_/           /_/"])
    pug4 = Shape([
        "               ____________",
        "    ___       |  /      \  |",
        "   /   \       \/ O____O \/",
        "  |  \_/        / /    \\/",
        "   \___________/  \____/",
        "   |                  /",
        "   |                 /",
        "   |   /            /",
        "   |  /\________/| |",
        "   | |           | |",
        "   |_|           |_|"])
    pug5 = Shape([
        "               ____________",
        "    ___       |  /      \  |",
        "   /   \       \/ -____- \/",
        "  |  \_/        / /    \\/",
        "   \___________/  \____/",
        "   |                  /",
        "   |                 /",
        "   |   /            /",
        "   |  /\________/| |",
        "   | |           | |",
        "   |_|           |_|"])
    pug6 = Shape([
        "               ____________",
        "    ___       |  /      \  |",
        "   /   \       \/ O____O \/",
        "  |  \_/        / /    \\/",
        "   \___________/  \____/",
        "   |                  /",
        "   |                 /",
        "   |   /            /_____",
        "   |  /\________/\________|    ruff",
        "   | |",
        "   |_|"])
    pug = Sprite([pug1, pug2, pug3, pug4, pug5, pug6])

if True: # hog shapes
    hog1 = Shape(["", "", "", "", "", "", "", 
        "      \\\\\\\\\\\\\\\\",
        "     \\\\\\\\\\\\\\ o",
        "    \\\\\\\\\\\\\\\\   >",
        "      |     |"])
    hog2 = Shape(["", "", "", "", "", "", "", 
        "      \\\\\\\\\\\\\\\\",
        "     \\\\\\\\\\\\\\ -",
        "    \\\\\\\\\\\\\\\\   >",
        "      \\     \\"])
    hog3 = Shape(["", "", "", "", "", "", "", 
        "      \\\\\\\\\\\\\\\\",
        "     \\\\\\\\\\\\\\ o",
        "    \\\\\\\\\\\\\\\\   >",
        "      /     /"])
    hog4 = Shape(["", "", "", "", "", "", "", 
        "        \\\\|//",
        "      \\\\\\\\|////",
        "     \\\\\\ - - ///",
        "    \\\\\\\\  V  ////"])
    hog5 = Shape(["", "", "", "", "", "", "", 
        "      \\ \\ | / /",
        "  \\ \\ \\ \\ | / / / /",
        "  \\ \\ \\  v v  / / /",
        "\\ \\ \\ \\   V   / / / /"])
    hog6 = Shape(["", "", "", "", "", "", "", 
        "      \\ \\ | / /",
        "  \\ \\ \\ \\ | / / / /",
        "  \\ \\ \\  v v  / / /",
        "\\ \\ \\ \\   V   / / / /      huff"])
    hog = Sprite([hog1, hog2, hog3, hog4, hog5, hog6])

if True: # fish shapes
    fish1 = Shape(["", "", "", "",
        "|\    ______",
        "| \  /      \\",
        "|  \/     O  \\",
        "|             O",
        "|  /\    >   /",
        "| /  \______/",
        "|/"])
    fish2 = Shape(["", "", "", "",
        " |    ______",
        " |\  /      \\",
        " | \/     O  \\",
        " |            O",
        " | /\        /",
        " |/  \______/",
        " |"])
    fish3 = Shape(["", "", "", "",
        "  |   ______",
        "  |  /      \\",
        "  |\/     O  \\",
        "  |           <",
        "  |/\    <   /",
        "  |  \______/",
        "  |"])
    fish4 = Shape(["", "", "", "",
        "|\    _______     o",
        "| \  /       \       o",
        "|  \/    O  O \  o", 
        "|          O  |",
        "|  /\  >      />",
        "| /  \_______/",
        "|/"])
    fish5 = Shape(["", "", "", "",
        "|\    _______     o",
        "| \  /       \       o",
        "|  \/    -  - \  o", 
        "|          O  |",
        "|  /\  >      />",
        "| /  \_______/",
        "|/"])
    fish6 = Shape(["", "", "", "",
        "|\    _______     o",
        "| \  /       \       o",
        "|  \/    O  O \  o", 
        "|          O  |      blub blub",
        "|  /\  >      />",
        "| /  \_______/",
        "|/"])
    fish = Sprite([fish1, fish2, fish3, fish4, fish5, fish6])

if True: # snow shapes
    snow1 = Shape(["", 
        "      ___   O",
        "     /o o\\",
        "     \_V_/     /",
        "     / o \\    /",
        "   /(  o  )__/",
        "  /  \\___/",
        " /   /   \\",
        "    /     \\",
        "   (       )",
        "    \_____/"])
    snow2 = Shape(["", 
        "      ___",
        "     /o o\\",
        "     \_V_/    O",
        "     / o \\      /",
        "   /(  o  )____/",
        "  /  \\___/",
        " /   /   \\",
        "    /     \\",
        "   (       )",
        "    \_____/"])
    snow3 = Shape(["", 
        "      ___",
        "     /o o\\",
        "     \_V_/",
        "     / o \\       O",
        "   /(  o  )________",
        "  /  \\___/",
        " /   /   \\",
        "    /     \\",
        "   (       )",
        "    \_____/"])
    snow4 = Shape(["", 
        "      ___",
        "     /o o\\",
        "     \_V_/",
        "     / o \\",
        "   /(  o  )",
        "  /  \\___/\\",
        " /   /   \ \\",
        "    /     \ \\",
        "   (       ) \\",
        "    \_____/"])
    snow5 = Shape(["", 
        "      ___",
        "     /- -\\",
        "     \_V_/",
        "     / o \\",
        "   /(  o  )",
        "  /  \\___/\\",
        " /   /   \ \\",
        "    /     \ \\",
        "   (       ) \\",
        "    \_____/"])
    snow6 = Shape(["", 
        "      ___",
        "x    /O O\   jingle",
        "   + \_V_/     bells",
        " \   / o \   x",
        "  \/(  o  )   /",
        "     \\___/\  /",
        "  x  /   \ \/",
        "    /     \\    +",
        "   (       )",
        "    \_____/"])
    snow = Sprite([snow1, snow2, snow3, snow4, snow5, snow6])

def command_parade(sprites):
    new_sprite = get_new_sprite(sprites)
    if len(sprites) > 1:
        make_walk(new_sprite, False)
    else:
        make_walk(new_sprite, True)

command = input("\n> ").strip().lower()
system("clear")
commands = command.split()
sprites = []
for name in commands:
    if "pug" in name:
        sprites.append(pug)
    elif "hog" in name:
        sprites.append(hog)
    elif "fish" in name:
        sprites.append(fish)
    elif "snow" in name:
        sprites.append(snow)
command_parade(sprites)
