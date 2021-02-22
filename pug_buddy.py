import time
from os import system

if True: # pug
    head_R = [
        "    _______  ",
        "   /\  /   \ ",
        "  /  \/ o __\\",
        " /       /  |",
        "/       |__/ "]
    head_speak = [
        "    _______  ",
        "   /\  /   \ ",
        "  /  \/ o __\\",
        " /       / /",
        "/       |__\ "]
    head_F = [
        " ___________ ",
        "|  /     \  |",
        " \/ o___o \/ ",
        " /  /   \ /  ",
        "/   \___//   "]
    head_TR = [
        " / \_____    ",
        "/_/  o   \__ ",
        "  / ___ o \ |",
        " / /   \  /\|",
        "/  \___/ /   "]
    head_TL = [
        "    _____/ \ ",
        " __/   o  \_\\",
        "| /o ___  |  ",
        "|/  /   \ |  ",
        "/   \___//   "]
    body = [
        "|_________",
        "|                 /",
        "|                / ",
        "|    /          /  "]
    legs_S = [
        "|  _/\_______| |   ",
        "| |          | |   ",
        "|_|          |_|   "]
    legs_R = [
        " \  /\________\ \  ",
        "  \ \          \ \ ",
        "   \_\          \_\\"]
    legs_L = [
        " \  /\_______/ /   ",
        " / /        / /    ",
        "/_/        /_/     "]
    tail_M = [
        "          ",
        "  ___     ",
        " /   \    ",
        "|  \_/    "]
    tail_big = [
        "   ____   ",
        " /      \ ",
        "|        |",
        "|     \_/ ",]
    tail_small = [
        "          ",
        "          ",
        "  __      ",
        " / _/     "]

current_head = head_R
current_legs = legs_S
current_tail = tail_M
current_eyes = "open"
current_spaces = 0
current_flip = False
reached_end = True

def assemble_pug(head, legs, tail, eyes, spaces, flip, body=body):
    global current_head, current_legs, current_tail, current_eyes, current_spaces, current_flip, reached_end
    current_head = head
    current_legs = legs
    current_tail = tail
    current_eyes = eyes
    current_flip = flip
    pug = []
    # parts assembly
    if eyes != "open":
        new_head = []
        for line in head:
            new_head.append(line.replace("o", "-"))
        head = new_head
    for i in range(4):
        pug.append(tail[i] + head[i])
    pug.append(body[0] + head[4])
    for line in body[1:]:
        pug.append(line)
    for line in legs:
        pug.append(line)
    # equalize lengths
    longest_line = 0
    for line in pug:
        if len(line) > longest_line:
            longest_line = len(line)
    new_pug = []
    for line in pug:
        line = line + " " * (longest_line - len(line))
        new_pug.append(line)
    pug = new_pug
    # flip
    if flip:
        new_pug = []
        for line in pug:
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
            new_pug.append(new_line)
        pug = new_pug
    # add spaces
    if spaces > 0:
        current_spaces = spaces
        for line_index in range(len(pug)):
            pug[line_index] = " " * spaces + pug[line_index]
        reached_end = False
    # remove spaces
    elif spaces < 0:
        furthest_space = 0
        for i in range(-1 * spaces):
            all_spaces = True
            for line_index in range(len(pug)):
                try:
                    if (pug[line_index])[i] != " ":
                        all_spaces = False
                except Exception:
                    all_spaces = False
            if all_spaces:
                furthest_space += 1
        for line_index in range(len(pug)):
            pug[line_index] = (pug[line_index])[furthest_space:]
        if furthest_space < (spaces * -1):
            reached_end = True
        current_spaces = furthest_space
    return pug

def print_pug(pause=0):
    system("clear")
    pug = assemble_pug(current_head, current_legs, current_tail, current_eyes, current_spaces, current_flip)
    for line in pug:
        print(line)
    time.sleep(pause)

def turn_head():
    global current_head
    if current_head == head_R:
        current_head = head_F
    else:
        current_head = head_R

def tilt_head():
    global current_head
    if current_head == head_TR:
        current_head = head_TL
    else:
        current_head = head_TR

def change_eyes():
    global current_eyes
    if current_eyes == "open":
        current_eyes = "closed"
    else:
        current_eyes = "open"

def change_tail(tail):
    global current_tail
    if tail == "small":
        current_tail = tail_small
    elif tail == "big":
        current_tail = tail_big
    elif tail == "m":
        current_tail = tail_M

def change_legs(legs):
    global current_legs
    if legs == "r":
        current_legs = legs_R
    elif legs == "l":
        current_legs = legs_L
    elif legs == "s":
        current_legs = legs_S

def flip():
    global current_flip
    if current_flip:
        current_flip = False
    else:
        current_flip = True

def jump(spaces):
    assemble_pug(current_head, current_legs, current_tail, current_eyes, (current_spaces + spaces), current_flip)
    return reached_end

def walk(spaces, pause=.1):
    global current_spaces
    spaces_moved = 0
    change_legs("s")
    print_pug(pause)
    if spaces > 0:
        jump_spaces = 1
    else:
        jump_spaces = -1
        spaces = spaces * -1
    while spaces_moved < spaces:
        for leg in ["r", "s", "l", "s"]:
            change_legs(leg)
            reached_end = jump(jump_spaces)
            print_pug(pause)
            spaces_moved += 1
            if reached_end or spaces_moved >= spaces:
                break
    change_legs("s")

def wag(num_times):
    global current_tail
    if current_tail == tail_M:
        tails = ["big", "m", "small", "m"]
    elif current_tail == tail_big:
        tails = ["m", "small", "m", "big"]
    elif current_tail == tail_small:
        tails = ["m", "big", "m", "small"]
    for x in range(num_times):
        for tail in tails:
            change_tail(tail)
            print_pug(pause=.1)

def speak(speech="ruff"):
    global current_head
    previous_head = current_head
    pug = assemble_pug(head_speak, current_legs, current_tail, current_eyes, current_spaces, current_flip)
    disp1 = ""
    disp2 = ""
    for char in speech:
        disp1 += (char + " ")
        disp2 += (char + "  ")
    iterations = [pug[3], (pug[3] + " " + speech), (pug[3] + "  " + speech), (pug[3] + "   " + disp1), (pug[3] + "    " + disp2)]
    for it in iterations:
        pug[3] = it
        system("clear")
        for line in pug:
            print(line)
        time.sleep(.2)
    time.sleep(1)
    current_head = previous_head

while True:
    print_pug()
    command = input("\n1. Wag tail\n2. Speak\n3. Blink\n4. Turn head\n5. Tilt head\n6. Turn around\n7. Teleport\n8. Walk\n9. Walk backwards\n\n").lower().strip()
    if command == "1": # wag tail
        wag(2)
    elif command == "2": # speak
        speak()
    elif command == "3": # blink
        change_eyes()
        print_pug(pause=.2)
        change_eyes()
    elif command == "4": # turn head
        turn_head()
    elif command == "5": # tilt head
        tilt_head()
    elif command == "6": # turn around
        flip()
    elif command == "7": # teleport
        spaces = input("How many spaces? (negative to move left) ")
        try:
            jump(int(spaces))
        except Exception:
            continue
    elif command == "8": # walk
        spaces = input("How many spaces? (negative to move left) ")
        if "-" in spaces and not current_flip:
            flip()
        elif "-" not in spaces and current_flip:
            flip()
        try:
            walk(int(spaces))
        except Exception:
            continue
    elif command == "9":
        spaces = input("How many spaces? (negative to move left) ")
        if "-" in spaces and  current_flip:
            flip()
        elif "-" not in spaces and not current_flip:
            flip()
        try:
            walk(int(spaces))
        except Exception:
            continue