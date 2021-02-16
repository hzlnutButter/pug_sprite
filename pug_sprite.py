import time
from os import system

class Shape():
    def __init__(self, lines):
        self.lines = lines
    def add_spaces(self, spaces):
        new_lines = []
        for line in self.lines:
            new_lines.append(" " * spaces + line)
        greater_than_70 = False
        for line in new_lines:
            if len(line) > 70:
                greater_than_70 = True
        self.lines = new_lines
        return greater_than_70
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
        greater_than_70 = False
        for shape in self.shapes:
            if amount_to_change > 0:
                greater_than_70 = shape.add_spaces(amount_to_change)
            elif amount_to_change < 0:
                shape.remove_spaces(amount_to_change)
        return greater_than_70
    def cycle_print_shapes(self, list_of_indices, sleep_time):
        for index in list_of_indices:
            system("clear")
            self.shapes[index].print_shape()
            time.sleep(sleep_time)

if True: # define shapes

    pug1 = [
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
    "   |_|           |_|"]

    pug2 = [
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
    "     \_\\          \_\\"]

    pug3 = [
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
    " /_/           /_/"]

    hog1 = [
    "",
    "      \\\\\\\\\\\\\\\\",
    "     \\\\\\\\\\\\\\ o",
    "    \\\\\\\\\\\\\\\\   >",
    "      |     |"]

    hog2 = [
    "",
    "      \\\\\\\\\\\\\\\\",
    "     \\\\\\\\\\\\\\ -",
    "    \\\\\\\\\\\\\\\\   >",
    "      \\     \\"]

    hog3 = [
    "",
    "      \\\\\\\\\\\\\\\\",
    "     \\\\\\\\\\\\\\ o",
    "    \\\\\\\\\\\\\\\\   >",
    "      /     /"]

    hog4 = [
    "",
    "        \\\\|//",
    "      \\\\\\\\|////",
    "     \\\\\\ - - ///",
    "    \\\\\\\\  V  ////"]

    hog5 = [
    "",
    "      \\ \\ | / /",
    "  \\ \\ \\ \\ | / / / /",
    "  \\ \\ \\  v v  / / /",
    "\\ \\ \\ \\   V   / / / /"]

pug_shape1 = Shape(pug1)
pug_shape2 = Shape(pug2)
pug_shape3 = Shape(pug3)
pug = Sprite([pug_shape1, pug_shape2, pug_shape3])

def make_pug_walk():
    while True:
        pug.cycle_print_shapes([0, 1, 0, 2], .1)
        if pug.change_all(3):
            break

hog_shape1 = Shape(hog1)
hog_shape2 = Shape(hog2)
hog_shape3 = Shape(hog3)
hog_shape4 = Shape(hog4)
hog_shape5 = Shape(hog5)
hedgehog = Sprite([hog_shape1, hog_shape2, hog_shape3, hog_shape4, hog_shape5])

def make_hog_walk():
    while True:
        hedgehog.cycle_print_shapes([0, 1, 0, 2], .1)
        if hedgehog.change_all(3):
            break
    hedgehog.cycle_print_shapes([3, 4, 3, 4], .2)
    print(" " * 60 + "huff")

make_hog_walk()
make_pug_walk()