import time
from os import system

if True: # pug
    head_side = [
        "    _______  ",
        "   /\  /   \ ",
        "  /  \/ o __\\",
        " /       /  |",
        "/       |__/ "]
    head_speak = [
        "    _______  ",
        "   /\  /   \ ",
        "  /  \/ o __\\",
        " /       / / ",
        "/       |__\ "]
    head_hat = [
        "   ____O____ ",
        "  /_________\\",
        "  /  \/ o __\\",
        " /       /  |",
        "/       |__/ "]
    head_front = [
        " ___________ ",
        "|  /     \  |",
        " \/ o___o \/ ",
        " /  /   \ /  ",
        "/   \___//   "]
    head_tilt_right = [
        " / \_____    ",
        "/_/  o   \__ ",
        "  / ___ o \ |",
        " / /   \  /\|",
        "/  \___/ /   "]
    head_tilt_left = [
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
    legs_straight = [
        "|  _/\_______| |   ",
        "| |          | |   ",
        "|_|          |_|   "]
    legs_front = [
        " \  /\________\ \  ",
        "  \ \          \ \ ",
        "   \_\          \_\\"]
    legs_back = [
        " \  /\_______/ /   ",
        " / /        / /    ",
        "/_/        /_/     "]
    tail_normal = [
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
    bone = "8==8"

current_head = head_side
current_legs = legs_straight
current_tail = tail_normal
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

def print_pug_with_bone(start_index, pause=0):
    pug = assemble_pug(current_head, current_legs, current_tail, current_eyes, current_spaces, current_flip)
    line_to_change = pug[3]
    if len(line_to_change) > start_index:
        line_to_change = line_to_change[:start_index] + bone + line_to_change[(start_index+4):]
    else:
        spaces_to_add = start_index - len(line_to_change)
        line_to_change = line_to_change + (" " * spaces_to_add) + bone
    pug[3] = line_to_change
    system("clear")
    for line in pug:
        print(line)
    time.sleep(pause)

def blink():
    global current_eyes
    if current_eyes == "open":
        print_pug(pause=.2)
        current_eyes = "closed"
        print_pug(pause=.2)
        current_eyes = "open"
        print_pug(pause=.2)
    elif current_eyes == "closed":
        print_pug(pause=.2)
        current_eyes = "open"
        print_pug(pause=.2)
        current_eyes = "closed"
        print_pug(pause=.2)

def wag():
    global current_tail
    if current_tail == tail_normal:
        tails = [tail_big, tail_normal, tail_small, tail_normal]
    elif current_tail == tail_big:
        tails = [tail_normal, tail_small, tail_normal, tail_big]
    elif current_tail == tail_small:
        tails = [tail_normal, tail_big, tail_normal, tail_small]
    for tail in tails:
        current_tail = tail
        print_pug(pause=.1)

def walk(spaces=None, start_index=None):
    global current_spaces, current_legs
    if spaces:
        spaces_moved = 0
        current_legs = legs_straight
        print_pug(.1)
        if spaces > 0:
            jump_spaces = 1
        else:
            jump_spaces = -1
            spaces = spaces * -1
        while spaces_moved < spaces:
            for leg in [legs_front, legs_straight, legs_back, legs_straight]:
                current_legs = leg
                assemble_pug(current_head, current_legs, current_tail, current_eyes, (current_spaces + jump_spaces), current_flip)
                print_pug(.1)
                spaces_moved += 1
                if reached_end or spaces_moved >= spaces:
                    break
        current_legs = legs_straight
    elif start_index: # walk to item
        pug = assemble_pug(current_head, current_legs, current_tail, current_eyes, current_spaces, current_flip)
        if len(pug[3]) < start_index: # walk right
            spaces = start_index - len(pug[3])
            jump_spaces = 1
        else: # walk left
            end_index = start_index + 4
            spaces = len(pug[3]) - 23 - end_index
            if spaces < 0:
                spaces = spaces * -1
            jump_spaces = -1
        spaces_moved = 0
        current_legs = legs_straight
        print_pug_with_bone(start_index, .1)
        while spaces_moved < spaces:
            for leg in [legs_front, legs_straight, legs_back, legs_straight]:
                current_legs = leg
                assemble_pug(current_head, current_legs, current_tail, current_eyes, (current_spaces + jump_spaces), current_flip)
                print_pug_with_bone(start_index, .1)
                spaces_moved += 1
                if reached_end or spaces_moved >= spaces:
                    break
        current_legs = legs_straight

def fetch(start_index, direction):
    global current_flip, current_head
    previous_head = current_head
    print_pug_with_bone(start_index)
    current_head = head_side
    if direction == "right":
        current_flip = False
    if direction == "left":
        current_flip = True
    walk(start_index=start_index)
    current_head = head_speak
    print_pug_with_bone(start_index, .25)
    print_pug(.25)
    current_head = head_side
    print_pug(.25)
    current_head = head_front
    print_pug(.25)
    wag()
    current_head = previous_head
                
def speak(speech):
    global current_head
    previous_head = current_head
    pug = assemble_pug(head_speak, current_legs, current_tail, current_eyes, current_spaces, current_flip)
    pug[3] = pug[3] + "  " + speech
    system("clear")
    for line in pug:
        print(line)
    time.sleep(1.5)
    current_head = previous_head

def command_loop():
    global current_head, current_flip
    print_pug()
    command = input("\n1. Wag tail\n2. Speak\n3. Blink\n4. Turn head\n5. Tilt head\n6. Walk\n7. Walk backwards\n8. Fetch\n\n").lower().strip()
    if command == "1": # wag tail
        wag()
    elif command == "2": # speak
        speak("ruff")
    elif command == "3": # blink
        blink()
    elif command == "4": # turn head
        if current_head == head_side:
            current_head = head_front
        else:
            current_head = head_side
    elif command == "5": # tilt head
        if current_head == head_tilt_right:
            current_head = head_tilt_left
        else:
            current_head = head_tilt_right
    elif command == "6": # walk
        if current_spaces < 50:
            current_flip = False
            walk(spaces=50)
        else:
            current_flip = True
            walk(spaces=-50)
    elif command == "7": # walk backwards
        if current_spaces < 50:
            current_flip = True
            walk(spaces=50)
        else:
            current_flip = False
            walk(spaces=-50)
    elif command == "8": # fetch
        if current_spaces <= 1:
            fetch(50, "right")
        else:
            fetch(1, "left")
            walk(spaces=-10)

def delay_print(output):
    pace = .03
    for char in output:
        print(char, end="", flush=True)
        time.sleep(pace)
        if pace > .005:
           pace = pace - .001
    print("")

def get_input(output): # returns processed input
    delay_print(output)
    user_input = input(" > ").strip().lower()
    while True:
        if user_input:
            return user_input
        else:
            user_input = input(" > ")

def go_to_game_bone(movement, index, dir):
    global current_flip
    while True:
        if movement == "r":
            if dir == "right":
                fetch(start_index=index, direction=dir)
                break
            else:
                current_flip = True
        elif movement == "l":
            if dir == "left":
                fetch(start_index=index, direction=dir)
                break
            else:
                current_flip = False
        movement = get_input("")


# begin game
current_head = head_front
print_pug()
name = get_input("\nhere's a pug! what would you like to name him?")
print_pug(.75)
# first bone
print_pug_with_bone(50, .3)
current_head = head_side
print_pug_with_bone(50)
movement = get_input("\n" + name + " sees a bone! to move " + name + ", enter 'l' for left or 'r' for right.")
go_to_game_bone(movement, 50, "right")
current_head = head_tilt_right
print_pug()
word = get_input("\nthis was a magic bone! " + name + " now has a message for you. enter 'speak' to make " + name + " talk.")
while True:
    if word == "speak":
        speak("ruff!")
        break
    else:
        word = get_input("")
print_pug()
delay_print("\nlooks like " + name + " forgot that we don't speak pug.")
translate = get_input("you will have to ask him to translate. enter 'ruff bark bark' to remind him.")
while True:
    if translate == "ruff bark bark":
        speak("the world is in danger!")
        break
    else:
        if current_head == head_tilt_right:
            current_head = head_tilt_left
        else:
            current_head = head_tilt_right
        print_pug()
        translate = get_input("\nhe didn't understand. enter 'ruff bark bark'.")
print_pug
delay_print("\noh my goodness! 'the world is in danger'?? that's not good news!")
delay_print("it's up to you and " + name + " now! what are you going to do?")
# second bone
print_pug_with_bone(5)
print("\noh my goodness! 'the world is in danger'?? that's not good news!")
print("it's up to you and " + name + " now! what are you going to do?")
movement = get_input("")
go_to_game_bone(movement, 5, "left")
delay_print("\nwhat?! another magic bone?! let's see what this one says.")
time.sleep(1)
current_flip = False
speak("what's a pug's favourite thing?")
fave = get_input("\nit must be a clue! what do you think is a pug's favourite thing?")
num_guesses = 0
while num_guesses < 4:
    num_guesses += 1
    if "treat" in fave or "food" in fave:
        current_head = head_front
        wag()
        break
    elif num_guesses > 2:
        fave = get_input("here's a hint: it eats it!")
    else:
        fave = get_input("hmm, guess again!")
if num_guesses > 4:
    delay_print("\nthe answer was 'treat'! (don't worry, you'll get it next time)")
else:
    delay_print("\ngreat job, you got it!")
delay_print("so what's next?")
# waiting for third bone
time.sleep(1)
wag()
wag()
wag()
current_head = head_speak
wag()
wag()
delay_print("\noh, " + name + " is a sneaky little pug. he wants another treat before he looks for the next clue!")
feed = get_input("enter 'feed' to give him a treat.")
while True:
    if feed == "feed":
        fetch(50, "right")
        break
    else:
        feed = get_input("")
speak("go to north pole")
delay_print("\nthis is getting exciting! but i'll bet it's cold up there. let's give " + name + " a hat.")
time.sleep(.75)
current_head = head_hat
print_pug()
print("\nthis is getting exciting! but i'll bet it's cold up there. let's give " + name + " a hat.")
delay_print("ok! let's go!")
time.sleep(1.5)
# going to north pole
system("clear")
time.sleep(1)
print_pug(1)
blink()
wag()
blink()
print_pug_with_bone(1)
movement = get_input("")
go_to_game_bone(movement, 1, "left")
current_head = head_front
print_pug()
delay_print("\noh no! the wind stole " + name + "'s hat. we'd better go back home before we hear the clue, because " + name + " is getting cold.")
time.sleep(1)
system("clear")
time.sleep(1)
current_flip = False
speak("ruff!")
translate = get_input("\noh no, the cold must have made him forget to translate for us!")
num_guesses = 0
while num_guesses < 4:
    num_guesses += 1
    if translate == "ruff bark bark":
        wag()
        break
    elif num_guesses > 2:
        translate = get_input("try reminding " + name + " to translate.")
    else:
        translate = get_input("he didn't understand you!")
if num_guesses >4:
    delay_print("i'll remind him for you. " + name + ", RUFF BARK BARK!")
else:
    delay_print("\ngreat! let's hear what he's got.")
time.sleep(.5)
speak("it's naptime")
delay_print("\nok then. ")