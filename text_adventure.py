import time
import random
import lists  # lists with some names
# gets a place randomly out of a list
place = random.choice(lists.places)
# gets a random weapon for the hero
weapon = random.choice(lists.weapons)
# gets the boss bound to the place
boss = lists.bosses[(lists.places.index(place))]
# gets the monster bound to the place
monster = lists.monsters[(lists.places.index(place))]
# boss door key
key = False
# healthpoints
hp = 100
# if visited Passage2Way2
psg2way2visited = False
# if visited Passage2Way3
psg2way3visited = False


# delay between printings
def pause_print(string):
    print(string)
    time.sleep(2)


# plays intro
def intro():
    pause_print("Your sister has a deadly illness.\n")
    pause_print("A rare medical herb is required for her cure.\n")
    pause_print(f"legends says that this herb is being guarded by {boss}\n")
    pause_print(f"you decide to set off to {place} to get this herb \n")
    pause_print(f"so you grabbed your family's {weapon} and set on the"
                " journey\n")
    pause_print("you dont have enough money but luckly you paid your"
                " last cent to make an old fisherman borrow you his boat \n")
    pause_print(f"You make your first step into {place} then suddenly"
                " you lost your conscious\n")
    pause_print("you wake up and find yourself in front of some stairs"
                " leading underground\n")
    pause_print("you go down the stairs and found two passageways")
    pass1()


# first passages screen
def pass1():
    passage = input("which passage way to enter| 1/2:")
    if passage == '1':
        pause_print("Its a deadend")
        pass1()
    elif passage == '2':
        pause_print("You hear something, you look behind and find that "
                    f"you are being attacked by a {monster}")
        normal_fight_1(hp, 25)
        pause_print(f"after defeating the {monster} you find yourself in"
                    "front of 3 passageways")
        pass2(key, psg2way2visited, psg2way3visited)
    else:
        pause_print("Where is this ?")
        pass1()


# second passages screen
def pass2(key, psg2way2visited, psg2way3visited):
    passage = input("which passage way to enter| 1/2/3:")
    if passage == '1':
        if key is False:
            pause_print("This passage has a huge locked door."
                        "Maybe i should look around for the key")
            pass2(key, psg2way2visited, psg2way3visited)
        elif key is True:
            pause_print(f"This passage is huge.This must be"
                        f" {boss}'s room")
            pause_print(f"You can see {boss} laying in a corner.\n"
                        "You search for the herb.\n")
            pause_print(f"You can see it beside {boss}.\n"
                        "You try to sneak to get it.\n")
            pause_print(f"Suddenly , {boss} opens his eyes and looks"
                        "at you.\n This is the final fight.")
            boss_fight(hp, 150)
    elif passage == '2':
        if psg2way2visited is False:
            pause_print("You hear something, you look behind and find that "
                        f"you are being attacked by a {monster}")
            normal_fight_2(hp, 25)
            pause_print("Its a deadend")
            psg2way2visited = True
            pass2(key, psg2way2visited, psg2way3visited)
        elif psg2way2visited is True:
            pause_print("Its a deadend")
            pass2(key, psg2way2visited, psg2way3visited)
    elif passage == '3':
        if psg2way3visited is False:
            pause_print("You hear something, you look behind and find that "
                        f"you are being attacked by a {monster} but its a bit"
                        "bigger than usual")
            normal_fight_2(hp, 50)
            pause_print("Tou found a big golden key")
            key = True
            psg2way3visited = True
            pass2(key, psg2way2visited, psg2way3visited)
        elif psg2way3visited is True:
            pause_print("There is nothing here")
            pass2(key, psg2way2visited, psg2way3visited)
    else:
        pause_print("Where is this ?")
        pass2(key, psg2way2visited, psg2way3visited)


# fighting screen for passages 1
def normal_fight_1(hp, cur_monster_hp):
    while cur_monster_hp > 0 and hp > 0:
        chance = random.randint(0, 9)
        attack = input(f"Your hp:{hp}|Monster hp:{cur_monster_hp}|"
                       "Fight or Run?| F/R:").lower()
        if attack == 'f':
            if cur_monster_hp <= 1:
                chance = 1
            pause_print(f"You attack using {weapon}")
            if chance <= 1:
                pause_print("You managed to kill it with one shot")
                break
            elif chance <= 5:
                dmg = random.randint(0, 20)
                cur_monster_hp -= dmg
                pause_print(f"You managed to deal:{dmg} damage to"
                            "it without getting hit")
            elif chance > 5:
                dmg2monster = random.randint(0, 20)
                dmg2me = random.randint(0, 15)
                cur_monster_hp -= dmg2monster
                hp -= dmg2me
                pause_print(f"You managed to deal:{dmg2monster} damage to it "
                            f"\nwhile it dealt:{dmg2me} damage to you")
        elif attack == "r":
            if chance <= 1:
                pause_print("You managed to run")
                pass1()
            elif chance <= 5:
                pause_print(f"You failed at running from it")
            elif chance > 5:
                dmg2me = random.randint(0, 15)
                hp -= dmg2me
                pause_print(f"You failed at running and the "
                            f"{monster} dealt {dmg2me} damage to you")
        else:
            pause_print("I cant do that")
    if cur_monster_hp <= 0:
        pause_print(f"You defeated {monster}")
    elif hp <= 0:
        game_over()


# fighting screen for passages 2
def normal_fight_2(hp, cur_monster_hp):
    while cur_monster_hp > 0 and hp > 0:
        chance = random.randint(0, 9)
        attack = input(f"Your hp:{hp}|Monster hp:{cur_monster_hp}"
                       "|Fight or Run?| F/R:").lower()
        if attack == 'f':
            if cur_monster_hp <= 1:
                chance = 1
            pause_print(f"You attack using {weapon}")
            if chance <= 1:
                pause_print("You managed to kill it with one shot")
                break
            elif chance <= 5:
                dmg = random.randint(0, 20)
                cur_monster_hp -= dmg
                pause_print(f"You managed to deal:{dmg} "
                            "damage to it without getting hit")
            elif chance > 5:
                dmg2monster = random.randint(0, 20)
                dmg2me = random.randint(0, 15)
                cur_monster_hp -= dmg2monster
                hp -= dmg2me
                pause_print(f"You managed to deal:{dmg2monster} damage to it"
                            f"\nwhile it dealt:{dmg2me} damage to you")
        elif attack == "r":
            if chance <= 1:
                pause_print("You managed to run")
                pass2(key, psg2way2visited, psg2way3visited)
            elif chance <= 5:
                pause_print(f"You failed at running from it")
            elif chance > 5:
                dmg2me = random.randint(0, 15)
                hp -= dmg2me
                pause_print(f"You failed at running and the"
                            f"{monster} dealt {dmg2me} damage to you")
        else:
            pause_print("I cant do that")
    if cur_monster_hp <= 0:
        pause_print(f"You defeated {monster}")
    elif hp <= 0:
        game_over()


# boss fighting screen
def boss_fight(hp, cur_monster_hp):
    while cur_monster_hp > 0 and hp > 0:
        chance = random.randint(0, 9)
        attack = input(f"Your hp:{hp}|{boss} hp:{cur_monster_hp}"
                       "|Fight or Run?| F/R:").lower()
        if attack == 'f':
            if cur_monster_hp <= 1:
                chance = 1
            pause_print(f"You attack using your {weapon}")
            if chance <= 5:
                dmg = random.randint(0, 15)
                cur_monster_hp -= dmg
                pause_print(f"You managed to deal:{dmg} "
                            "damage to it without getting hit")
            elif chance > 5:
                dmg2monster = random.randint(0, 15)
                dmg2me = random.randint(10, 25)
                cur_monster_hp -= dmg2monster
                hp -= dmg2me
                pause_print(f"You managed to deal:{dmg2monster} damage to it"
                            f"\nwhile it dealt:{dmg2me} damage to you")
        elif attack == "r":
            pause_print("You can't run")
            boss_fight(hp, cur_monster_hp)
        else:
            pause_print("I cant do that")
    if cur_monster_hp <= 0:
        pause_print("You get the herb and cure your sister")
        game_over()
    elif hp <= 0:
        game_over()


# game over screen
def game_over():
    pause_print("Game Over")
    new_game = input("New game?| Y/N: ").lower()
    if new_game == "y":
        pause_print("Starting new game...")
        intro()
    elif new_game == "n":
        pause_print("Closing game....")
        sys.close()
    else:
        pause_print("What is this?")
        game_over()


intro()  # Starts game
