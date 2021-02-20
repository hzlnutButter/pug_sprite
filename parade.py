import time
from os import system

class Shape():
    def __init__(self, lines):
        self.lines = lines
    def adjust_spaces(self, spaces):
        new_lines = []
        greater_than_125 = False
        if spaces > 0:
            for line in self.lines:
                new_lines.append(" " * spaces + line)
            for line in new_lines:
                if len(line) > 125:
                    greater_than_125 = True
        elif spaces < 0:
            for line in self.lines:
                new_line = ""
                for x in range(spaces * -1):
                    if line[x] == " ":
                        new_line = line[x + 1]
                    else:
                        break
                new_lines.append(new_line)
        self.lines = new_lines
        return greater_than_125
    def print_shape(self):
        for line in self.lines:
            print(line)
    def reverse_shape(self, move_to_right=False):
        new_lines = []
        for line in self.lines:
            new_line = ""
            for char in line:
                if char in "\ " and char != " ":
                    char = "/"
                elif char == "/":
                    char = "\ "[0]
                elif char == ">":
                    char = "<"
                elif char == "<":
                    char = ">"
                elif char == "(":
                    char = ")"
                elif char == ")":
                    char = "("
                new_line = char + new_line
            if move_to_right:
                spaces = 125 - len(new_line)
                new_line = " " * spaces + new_line
            new_lines.append(new_line)
        self.lines = new_lines
        return self.lines
    def advance_both_shapes(self, spaces, previous_movements):
        previous_added_spaces = spaces * previous_movements
        new_lines = []
        for line in self.lines:
            if line:
                if line[(27 + previous_added_spaces):(27 + previous_added_spaces + spaces * 2)] == " " * (spaces * 2):
                    p1 = " " * spaces + line[:(27 + previous_added_spaces)]
                    p2 = line[(27 + previous_added_spaces + spaces * 2):]
                    p3 = " " * spaces
                    new_lines.append(p1 + p2 + p3)
                else:
                    return False
        self.lines = new_lines

class Sprite():
    def __init__(self, shapes):
        self.shapes = shapes
    def change_all(self, spaces):
        greater_than_125 = False
        for shape in self.shapes:
            greater_than_125 = shape.adjust_spaces(spaces)
        return greater_than_125
    def cycle_print_shapes(self, indexes=[0, 1, 0, 2], sleep_time=.075):
        for index in indexes:
            system("clear")
            self.shapes[index].print_shape()
            time.sleep(sleep_time)
    def print_a_shape(self, shape_index):
        (self.shapes[shape_index]).print_shape()
    def walk_LR(self, play_ending=False):
        while True:
            self.cycle_print_shapes()
            if self.change_all(3):
                break
        if play_ending:
            self.cycle_print_shapes(indexes=[3, 4, 3, 4], sleep_time=.2)
            system("clear")
            self.print_a_shape(5)
    def reverse_sprite(self, move_to_right=False):
        new_shapes = []
        for shape in self.shapes:
            if move_to_right:
                shape.reverse_shape(move_to_right=True)
            else:
                shape.reverse_shape()
            new_shapes.append(shape)
        self.shapes = new_shapes
    def advance_both_sprites(self, spaces, previous_movements):
        new_shapes = []
        for shape in self.shapes:
            if shape.advance_both_shapes(spaces, previous_movements) == False:
                return False
            new_shapes.append(shape)
    def dance(self, spaces=3):
        system("clear")
        self.shapes[0].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[3].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[0].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[0].adjust_spaces(3)
        self.shapes[0].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[1].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[2].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[1].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[0].adjust_spaces(3)
        self.shapes[0].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[1].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[2].adjust_spaces(3)
        self.shapes[2].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[3].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[4].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[3].print_shape()
        time.sleep(.3)
        system("clear")
        self.shapes[5].print_shape()

if True: # pug shapes
    pug1 = Shape([
        "                  _______  ",
        "    ___          /\  /   \ ",
        "   /   \        /  \/ O __\\",
        "  |  \_/       /      /   |",
        "   \__________/       |__/ ",
        "   |                  /    ",
        "   |                 /     ",
        "   |   /            /      ",
        "   |  /\________/| |       ",
        "   | |           | |       ",
        "   |_|           |_|       "])
    pug2 = Shape([
        "   __             _______  ",
        " /    \          / \ |   \ ",
        "|      |        /   \|- __\\",
        "|   \_/        /      /   |",
        " \____________/       |__/ ",
        "  \                   /    ",
        "  |                  /     ",
        "  |    /            /      ",
        "   \  /\________/\ \       ",
        "    \ \           \ \      ",
        "     \_\           \_\     "])
    pug3 = Shape([
        "                  _______  ",
        "                 /| /    \ ",
        "       __       / |/  O __\\",
        "     / _/      /      /   |",
        "    |_________/       |__/ ",
        "    /                 /    ",
        "   |                 /     ",
        "   |   /            /      ",
        "   / _/\_________/ /       ",
        "  / /           / /        ",
        " /_/           /_/         "])
    pug4 = Shape([
        "               ____________        ",
        "    ___       |  /      \  |       ",
        "   /   \       \/ O____O \/        ",
        "  |  \_/        / /    \\/          ",
        "   \___________/  \____/           ",
        "   |                  /            ",
        "   |                 /             ",
        "   |   /            /              ",
        "   |  /\________/| |               ",
        "   | |           | |               ",
        "   |_|           |_|               "])
    pug5 = Shape([
        "               ____________        ",
        "    ___       |  /      \  |       ",
        "   /   \       \/ -____- \/        ",
        "  |  \_/        / /    \\/          ",
        "   \___________/  \____/           ",
        "   |                  /            ",
        "   |                 /             ",
        "   |   /            /              ",
        "   |  /\________/| |               ",
        "   | |           | |               ",
        "   |_|           |_|               "])
    pug6 = Shape([
        "               ____________        ",
        "    ___       |  /      \  |       ",
        "   /   \       \/ O____O \/        ",
        "  |  \_/        / /    \\/          ",
        "   \___________/  \____/           ",
        "   |                  /            ",
        "   |                 /             ",
        "   |   /            /_____         ",
        "   |  /\________/\________|    ruff",
        "   | |                             ",
        "   |_|                             "])
    pug = Sprite([pug1, pug2, pug3, pug4, pug5, pug6])
if True: # hog shapes
    hog1 = Shape(["", "", "", "", "", "", "", 
        "      \\\\\\\\\\\\\\\\  ", # 16 char per row
        "     \\\\\\\\\\\\\\ o  ",
        "    \\\\\\\\\\\\\\\\   >",
        "      |     |   "])
    hog2 = Shape(["", "", "", "", "", "", "", 
        "      \\\\\\\\\\\\\\\\  ",
        "     \\\\\\\\\\\\\\ -  ",
        "    \\\\\\\\\\\\\\\\   >",
        "      \\     \\   "])
    hog3 = Shape(["", "", "", "", "", "", "", 
        "      \\\\\\\\\\\\\\\\  ",
        "     \\\\\\\\\\\\\\ o  ",
        "    \\\\\\\\\\\\\\\\   >",
        "      /     /   "])
    hog4 = Shape(["", "", "", "", "", "", "", 
        "        \\\\|//                  ",
        "      \\\\\\\\|////                ",
        "     \\\\\\ - - ///               ",
        "    \\\\\\\\  V  ////              "])
    hog5 = Shape(["", "", "", "", "", "", "", 
        "      \\ \\ | / /                ",
        "  \\ \\ \\ \\ | / / / /            ",
        "  \\ \\ \\  v v  / / /            ",
        "\\ \\ \\ \\   V   / / / /          "])
    hog6 = Shape(["", "", "", "", "", "", "", 
        "      \\ \\ | / /                ",
        "  \\ \\ \\ \\ | / / / /            ",
        "  \\ \\ \\  v v  / / /            ",
        "\\ \\ \\ \\   V   / / / /      huff"])
    hog = Sprite([hog1, hog2, hog3, hog4, hog5, hog6])
if True: # fish shapes
    fish1 = Shape(["", "", "", "",
        "|\    ______   ",
        "| \  /      \  ",
        "|  \/     O  \ ",
        "|             O",
        "|  /\    >   / ",
        "| /  \______/  ",
        "|/             "])
    fish2 = Shape(["", "", "", "",
        " |    ______   ",
        " |\  /      \  ",
        " | \/     O  \ ",
        " |            O",
        " | /\        / ",
        " |/  \______/  ",
        " |             "])
    fish3 = Shape(["", "", "", "",
        "  |   ______   ",
        "  |  /      \  ",
        "  |\/     O  \ ",
        "  |           <",
        "  |/\    <   / ",
        "  |  \______/  ",
        "  |            "])
    fish4 = Shape(["", "", "", "",
        "|\    _______     o           ",
        "| \  /       \       o        ",
        "|  \/    O  O \  o            ", 
        "|          O  |               ",
        "|  /\  >      />              ",
        "| /  \_______/                ",
        "|/                            "])
    fish5 = Shape(["", "", "", "",
        "|\    _______     o           ",
        "| \  /       \       o        ",
        "|  \/    -  - \  o            ", 
        "|          O  |               ",
        "|  /\  >      />              ",
        "| /  \_______/                ",
        "|/                            "])
    fish6 = Shape(["", "", "", "",
        "|\    _______     o           ",
        "| \  /       \       o        ",
        "|  \/    O  O \  o            ", 
        "|          O  |      blub blub",
        "|  /\  >      />              ",
        "| /  \_______/                ",
        "|/                            "])
    fish = Sprite([fish1, fish2, fish3, fish4, fish5, fish6])
if True: # snow shapes
    snow1 = Shape(["", 
        "      ___   O      ",
        "     /o o\         ",
        "     \_V_/     /   ",
        "     / o \    /    ",
        "   /(  o  )__/     ",
        "  /  \\___/         ",
        " /   /   \         ",
        "    /     \        ",
        "   (       )       ",
        "    \_____/        "])
    snow2 = Shape(["", 
        "      ___          ",
        "     /o o\         ",
        "     \_V_/    O    ",
        "     / o \      /  ",
        "   /(  o  )____/   ",
        "  /  \\___/         ",
        " /   /   \         ",
        "    /     \        ",
        "   (       )       ",
        "    \_____/        "])
    snow3 = Shape(["", 
        "      ___          ",
        "     /o o\         ",
        "     \_V_/         ",
        "     / o \       O ",
        "   /(  o  )________",
        "  /  \\___/         ",
        " /   /   \         ",
        "    /     \        ",
        "   (       )       ",
        "    \_____/        "])
    snow4 = Shape(["", 
        "      ___           ",
        "     /o o\          ",
        "     \_V_/          ",
        "     / o \          ",
        "   /(  o  )         ",
        "  /  \\___/\         ",
        " /   /   \ \        ",
        "    /     \ \       ",
        "   (       ) \      ",
        "    \_____/         "])
    snow5 = Shape(["", 
        "      ___           ",
        "     /- -\          ",
        "     \_V_/          ",
        "     / o \          ",
        "   /(  o  )         ",
        "  /  \\___/\         ",
        " /   /   \ \        ",
        "    /     \ \       ",
        "   (       ) \      ",
        "    \_____/         "])
    snow6 = Shape(["", 
        "      ___           ",
        "x    /O O\   jingle ",
        "   + \_V_/     bells",
        " \   / o \   x      ",
        "  \/(  o  )   /     ",
        "     \\___/\  /      ",
        "  x  /   \ \/       ",
        "    /     \    +    ",
        "   (       )        ",
        "    \_____/         "])
    snow = Sprite([snow1, snow2, snow3, snow4, snow5, snow6])

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

def get_backwards_sprite(sprite):
    shapes = []
    for shape in sprite.shapes:
        shape.reverse_shape()
        shapes.append(shape)
    return Sprite(shapes)

def parade(sprites):
    if len(sprites) == 1:
        sprites[0].walk_LR(play_ending=True)
    else:
        (get_new_sprite(sprites)).walk_LR()

def confrontation(L_sprite, R_sprite): # make this work for composite sprites
    if L_sprite == R_sprite:
        new_L_shapes = []
        for shape in L_sprite.shapes:
            new_L_lines = []
            for line in shape.lines:
                new_L_lines.append(line)
            new_L_shapes.append(Shape(new_L_lines))
        new_L_sprite = Sprite(new_L_shapes)
        R_sprite.reverse_sprite(move_to_right=True)
        new_sprite = get_new_sprite([new_L_sprite, R_sprite])
    else:
        R_sprite.reverse_sprite(move_to_right=True)
        new_sprite = get_new_sprite([L_sprite, R_sprite])
    previous_movements = 0
    while True:
        new_sprite.cycle_print_shapes()
        if new_sprite.advance_both_sprites(3, previous_movements) == False:
            break
        previous_movements += 1
    system("clear")
    new_sprite.print_a_shape(0)

# while True:
#     command = input("\n> ").strip().lower().split()
#     system("clear")
#     sprites = []
#     for name in command:
#         if "pug" in name:
#             sprites.append(Sprite(pug.shapes))
#         elif "hog" in name:
#             sprites.append(Sprite(hog.shapes))
#         elif "fish" in name:
#             sprites.append(Sprite(fish.shapes))
#         elif "snow" in name:
#             sprites.append((Sprite(snow.shapes)))
#     parade(sprites)