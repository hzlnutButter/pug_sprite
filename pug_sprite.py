import time
from os import system

pug1 = [
"                         ________",
"    ___                 /\  /    \\",
"   /   \               /  \/  O __\\",
"  |  \_/              /       /   |",
"   \_________________/        |__/",
"   |                          /",
"   |                         /",
"   |                        /",
"   |   /                   /",
"   |  /\_______________/| |",
"   | |                  | |",
"   |_|                  |_|"]

pug2 = [
"                         ________",
"    ___                 /\  /    \\",
"   /   \               /  \/  O __\\",
"  |  \_/              /       /   |",
"   \_________________/        |__/",
"   |                          /",
"   |                         /",
"   |                        /",
"   |    /                  /",
"    \  /\_______________/\ \\",
"     \ \\                  \ \\",
"      \_\\                  \_\\"]

pug3 = [
"                         ________",
"    ___                 /\  /    \\",
"   /   \               /  \/  O __\\",
"  |  \_/              /       /   |",
"   \_________________/        |__/",
"   |                          /",
"   |                         /",
"   |                        /",
"   |     /                 /",
"   / ___/\______________/ /",
"  / /                  / /",
" /_/                  /_/"]

def print_sprite(sprite, spaces):
    new_sprite = []
    for line in sprite:
        new_sprite.append((" " * spaces) + line)
    for line in new_sprite:
        print(line)
    time.sleep(.1)
    system("clear")
    if len(new_sprite[3]) >=70:
        return
    return new_sprite

def walk_LR(pug1, pug2, pug3):
    while True:
        pug1 = print_sprite(pug1, 2)
        if pug1 is None:
            break
        pug2 = print_sprite(pug2, 4)
        if pug2 is None:
            break
        pug1 = print_sprite(pug1, 2)
        if pug1 is None:
            break
        pug3 = return_val = print_sprite(pug3, 4)
        if pug3 is None:
            break

walk_LR(pug1, pug2, pug3)