#import section
import keyboard
import sys
from time import sleep
#glossary
occupied = "\033[31m   CAN'T MOVE HERE BECAUSE THIS PLACE IS OCCUPIED! \033[00m"

num_of_soldiers = 0
num_of_towers = 0
selectable_list = []
whose_turn = 1
def main_menu():
    global whose_turn
    options = ["Buy", "Soldiers", "Towers", "End Turn", "Exit" ]
    selected = 0
    options_str = "  "
    for i in range(5):
        if selected == i:
            options_str += "\033[42m" + options[i]  + "\033[00m" + "   "
        else:
            options_str += options[i] + "   "
    row_text[22] = options_str
    print_map()
    while True:
        keyp = ""
        keyp = keyboard.read_key()
        for i in range(150):
            keyboard.block_key(i)
        if keyp == "enter":
            if selected == 1: # chosed soldier
                if len(player_list[whose_turn - 1].soldier_list) > 0:
                    unit_selection()
                else:
                    row_text[22] = "     YOU DON'T HAVE ANY SOLDIERS"
                    print_map()
                    sleep(1)
                    row_text[22] = options_str
                    print_map()
            elif selected == 2: # chosed tower
                if len(player_list[whose_turn - 1].tower_list) > 0:
                    tower_selection()
                else:
                    row_text[22] = "     YOU DON'T HAVE ANY TOWERS"
                    print_map()
                    sleep(1)
                    row_text[22] = options_str
                    print_map()
            elif selected == 0: # chosed buy
                sleep(0.1)
                buy()
            elif selected == 4: # chosed exit
                quit()
            elif selected == 3: #chosed end turn
                if whose_turn == 1:
                    whose_turn = 2
                elif whose_turn == 2:
                    whose_turn = 1
                    for player in player_list:
                        player.gold += player.check_income()
                for i in player_list:
                    for u in i.soldier_list:
                        u.move_used = False
                        u.attack_used = False
                    for o in i.tower_list:
                        o.attack_used = False
                sleep(0.2)

        elif keyp == "up":
            selected -=1

        elif keyp == "down":
            selected += 1
        elif keyp == "right":
            selected += 1
        elif keyp == "left":
            selected -= 1
        if selected >= len(options):
            selected = 0
        elif selected < 0:
            selected = len(options) - 1
        options_str = "  "
        for i in range(5):
            if selected == i:
                options_str += "\033[42m" + options[i]  + "\033[00m" + "   "
            else:
                options_str += options[i] + "   "

        row_text[22] = options_str
        print_map()
        sleep(0.2)
        for i in range(150):
            keyboard.unblock_key(i)


def move_attack(actor):  #promting choice of action
    options = []
    if actor.move_used == False:
        options.append("Move")
    if actor.attack_used == False:
        options.append("Attack")
    if len(options) == 0:
        row_text[22] = "\033[91m    THIS UNIT HAD TURN ALREADY \033[0m"
        print_map()
        sleep(1)
    selected = 0
    options_str = "  "
    if len(options) > 0:
        for i in range(len(options)):
            if selected == i:
                options_str += "\033[42m" + options[i]  + "\033[00m" + "   "
            else:
                options_str += options[i] + "   "
        row_text[22] = options_str
    print_map()
    sleep(0.2)
    for i in range(150):
        keyboard.unblock_key(i)
    if len(options) == 0:
        for i in range(150):
            keyboard.block_key(i)

    while len(options) > 0:
        options = []
        if actor.move_used == False:
            options.append("Move")
        if actor.attack_used == False:
            options.append("Attack")
        if len(options) == 1:
            selected = 0
        print_map()
        keyp3 = ""
        keyp3 = keyboard.read_key()
        for i in range(150):
            keyboard.block_key(i)
        if keyp3 == "enter":
            if options[selected] == "Move":
                options_str = ""
                row_text[22] = options_str
                movement(actor)
                if actor.move_used == True and actor.attack_used == True:
                    row_text[22] = "     CHOOSE YOUR UNIT     "
                    for i in range(150):
                        keyboard.unblock_key(i)
                    break          
            if options[selected] == "Attack":
                options_str = ""
                row_text[22] = options_str
                unit_selection_attack(actor) 
                if actor.move_used == True and actor.attack_used == True:
                    for i in range(150):
                        keyboard.unblock_key(i)
                    row_text[22] = "     CHOOSE YOUR UNIT     "
                    break   

                sleep(0.2)
        elif keyp3 == "esc":
            row_text[22] = "     CHOSE YOUR UNIT     "
            for i in range(150):
                keyboard.unblock_key(i)
            break
        elif keyp3 == "up":
            selected -=1
        elif keyp3 == "down":
            selected += 1
        elif keyp3 == "right":
            selected += 1
        elif keyp3 == "left":
            selected -= 1
        if selected >= len(options):
            selected = 0
        elif selected < 0:
            selected = len(options) - 1
        options_str = "  "
        options = []
        if actor.move_used == False:
            options.append("Move")
        if actor.attack_used == False:
            options.append("Attack")
        if len(options) == 1:
            selected = 0
        for i in range(len(options)):
            if selected == i:
                options_str += "\033[42m" + options[i]  + "\033[00m" + "   "
            else:
                options_str += options[i] + "   "

        row_text[22] = options_str
        print_map()
        sleep(0.2)
        for i in range(150):
            keyboard.unblock_key(i)
        
    if len(options) == 0:
        row_text[22] = "\033[91m    THIS UNIT HAD TURN ALREADY \033[0m"
        sleep(0.2)
        row_text[22] = "\033[91m    CHOOSE YOUR UNIT \033[0m"
        for i in range(150):
            keyboard.unblock_key(i) 


def buy():  #promting choice of what to buy
    options = ["Soldier  300$", "Tower  700$", "Economy Building  500$"]
    selected = 0
    options_str = "  "
    for i in range(len(options)):
        if selected == i:
                options_str += "\033[42m" + options[i]  + "\033[00m" + "   "
        else:
                options_str += options[i] + "    "
    row_text[22] = options_str
    print_map()
    while True:
        sleep(0.1)
        for i in range(150):
            keyboard.unblock_key(i)
        options = ["Soldier  300$", "Tower  700$", "Economy Building  500$"]
        options_str = "  "
        for i in range(len(options)):
            if selected == i:
                    options_str += "\033[42m" + options[i]  + "\033[00m" + "   "
            else:
                    options_str += options[i] + "    "
        row_text[22] = options_str
        print_map()
        keyp3 = ""
        keyp3 = keyboard.read_key()
        for i in range(150):
            keyboard.block_key(i)
        if keyp3 == "enter":
            if options[selected] == "Soldier  300$":
                sleep(0.1)
                if player_list[whose_turn-1].gold >= 300:
                    buy_soldier()
                else:
                    row_text[22] = "   YOU DON'T HAVE ENOUGH MONEY"
                    print_map()
                    sleep(1)
                #for i in range(150):
                 #   keyboard.unblock_key(i)
                break          
            if options[selected] == "Tower  700$":
                sleep(0.1)
                if player_list[whose_turn-1].gold >= 700:
                    buy_tower()
                else:
                    row_text[22] = "   YOU DON'T HAVE ENOUGH MONEY"
                    print_map()
                    sleep(1)
                #for i in range(150):
                 #   keyboard.unblock_key(i)
                break     
        elif keyp3 == "esc":
            break
        elif keyp3 == "up":
            selected -=1
        elif keyp3 == "down":
            selected += 1
        elif keyp3 == "right":
            selected += 1
        elif keyp3 == "left":
            selected -= 1
        if selected >= len(options):
            selected = 0
        elif selected < 0:
            selected = len(options) - 1
        options_str = "  "
        for i in range(len(options)):
            if selected == i:
                options_str += "\033[42m" + options[i]  + "\033[00m" + "   "
            else:
                options_str += options[i] + "    "
        row_text[22] = options_str
        print_map()
        sleep(0.2)


def buy_soldier():
    global num_of_soldiers
    if whose_turn == 1:
        if len(player_list[whose_turn - 1].soldier_list) >= 6:
            row_text[22] = "   TOO MANY SOLDIERS!!"
            print_map()
            sleep(1)     
        else:       
            if is_free("I", 3):
                globals()[f"soldier{num_of_soldiers}"] = Soldier(whose_turn, 10, 2, "I", 3)
                set_object("I", 3, globals()[f"soldier{num_of_soldiers}"])
                num_of_soldiers += 1
                player_list[whose_turn-1].gold -= 300
            elif is_free("J", 3):
                globals()[f"soldier{num_of_soldiers}"] = Soldier(whose_turn, 10, 2, "J", 3)
                set_object("J", 3, globals()[f"soldier{num_of_soldiers}"])
                num_of_soldiers += 1     
                player_list[whose_turn-1].gold -= 300
            elif is_free("H", 3):
                globals()[f"soldier{num_of_soldiers}"] = Soldier(whose_turn, 10, 2, "H", 3)
                set_object("H", 3, globals()[f"soldier{num_of_soldiers}"])
                num_of_soldiers += 1  
                player_list[whose_turn-1].gold -= 300  
            elif is_free("K", 3):
                globals()[f"soldier{num_of_soldiers}"] = Soldier(whose_turn, 10, 2, "K", 3)
                set_object("K", 3, globals()[f"soldier{num_of_soldiers}"])
                num_of_soldiers += 1  
                player_list[whose_turn-1].gold -= 300
            else:
                row_text[22] = "   YOU DON'T HAVE ENOUGH SPACE!!"
                print_map()
                sleep(1)
    elif whose_turn == 2:
        if len(player_list[whose_turn - 1].soldier_list) >= 6:
            row_text[22] = "   TOO MANY SOLDIERS!!"
            print_map()
            sleep(1)     
        else:       
            if is_free("I", 24):
                globals()[f"soldier{num_of_soldiers}"] = Soldier(whose_turn, 10, 2, "I", 24)
                set_object("I", 24, globals()[f"soldier{num_of_soldiers}"])
                num_of_soldiers += 1
                player_list[whose_turn-1].gold -= 300
            elif is_free("J", 24):
                globals()[f"soldier{num_of_soldiers}"] = Soldier(whose_turn, 10, 2, "J", 24)
                set_object("J", 24, globals()[f"soldier{num_of_soldiers}"])
                num_of_soldiers += 1   
                player_list[whose_turn-1].gold -= 300  
            elif is_free("H", 24):
                globals()[f"soldier{num_of_soldiers}"] = Soldier(whose_turn, 10, 2, "H", 24)
                set_object("H", 24, globals()[f"soldier{num_of_soldiers}"])
                num_of_soldiers += 1  
                player_list[whose_turn-1].gold -= 300  
            elif is_free("K", 24):
                globals()[f"soldier{num_of_soldiers}"] = Soldier(whose_turn, 10, 2, "K", 24)
                set_object("K", 3, globals()[f"soldier{num_of_soldiers}"])
                num_of_soldiers += 1 
                player_list[whose_turn-1].gold -= 300 
            else:
                row_text[22] = "   YOU DON'T HAVE ENOUGH SPACE!!"
                print_map()
                sleep(1)

def buy_tower():
    global num_of_towers
    global selectable_list
    if whose_turn == 1:
        if len(player_list[whose_turn - 1].tower_list) >= 6:
            row_text[22] = "   TOO MANY TOWERS!!"
            print_map()
            sleep(1)   
        else:
            for x in list(map(chr, range(65, 65 + map_size[0]))):
                for y in range(0, map_size[1] // 2):
                    if is_free(x,y): 
                        set_object(x, y, Selectable(x, y))
            selected = 0
            selectable_list[selected].selected = True
            row_text[22] = "     SELECT PLACE WHERE YOU WANT TO PUT YOUR TOWER     "
            print_map()
            sleep(0.2)
            while True:
                row_text[22] = "     SELECT PLACE WHERE YOU WANT TO PUT YOUR TOWER     "
                keyp2 = ""
                #keyp2 = keyboard.read_hotkey()
                #print(keyp2)
                """if keyp2 == "enter":
                        move_attack(options[selected])
                        for i in range(150):
                            keyboard.block_key(i)
                        options = []
                        for i in player_list[whose_turn - 1].soldier_list:
                            options.append(i)
                        selected = 0"""
                if keyboard.is_pressed("enter"):
                    choosed_x = selectable_list[selected].x
                    choosed_y = selectable_list[selected].y
                    for i in selectable_list:
                        i.selected = False
                    for i in selectable_list:
                        set_object(i.x, i.y, " ")
                    selectable_list = []
                    if is_free_area(choosed_x, choosed_y, 2, 2):
                        player_list[whose_turn-1].gold -= 700
                        set_object(choosed_x, choosed_y, Tower(whose_turn, x=choosed_x, y=choosed_y))
                    else:
                        row_text[22] = "   NOT ENOUGH SPACE FOR TOWER!!!"
                        print_map()
                        sleep(1)
                    break
                elif keyboard.is_pressed("esc"):
                    for i in selectable_list:
                        i.selected = False
                    for i in selectable_list:
                        set_object(i.x, i.y, " ")
                    selectable_list = []
                    break
                elif keyboard.is_pressed("up"):
                    selected -= 1
                elif keyboard.is_pressed("down"):
                    selected += 1
                elif keyboard.is_pressed("right"):
                    for i in range(len(selectable_list)):
                        if selectable_list[i].y == selectable_list[selected].y and header_to_number[selectable_list[i].x] > header_to_number[selectable_list[selected].x]:
                            selected = i
                            sleep(0.05)
                            break
                elif keyboard.is_pressed("left"):
                    for i in reversed(range(len(selectable_list))):
                        if selectable_list[i].y == selectable_list[selected].y and header_to_number[selectable_list[i].x] < header_to_number[selectable_list[selected].x]:
                            selected = i
                            sleep(0.05)
                            break
                if selected >= len(selectable_list):
                    selected = 0
                elif selected < 0:
                    selected = len(selectable_list) - 1

                for i in selectable_list:
                    i.selected = False
                selectable_list[selected].selected = True
                print_map()
                sleep(0.1)
    elif whose_turn == 2:
        if len(player_list[whose_turn - 1].tower_list) >= 6:
            row_text[22] = "   TOO MANY TOWERS!!"
            print_map()
            sleep(1)   
        else:
            for x in list(map(chr, range(65, 65 + map_size[0]))):
                for y in range(map_size[1]//2, map_size[1]):
                    if is_free(x,y): 
                        set_object(x, y, Selectable(x, y))
            selected = 0
            selectable_list[selected].selected = True
            row_text[22] = "     SELECT PLACE WHERE YOU WANT TO PUT YOUR TOWER     "
            print_map()
            sleep(0.2)
            while True:
                row_text[22] = "     SELECT PLACE WHERE YOU WANT TO PUT YOUR TOWER     "
                keyp2 = ""
                #keyp2 = keyboard.read_hotkey()
                #print(keyp2)
                """if keyp2 == "enter":
                        move_attack(options[selected])
                        for i in range(150):
                            keyboard.block_key(i)
                        options = []
                        for i in player_list[whose_turn - 1].soldier_list:
                            options.append(i)
                        selected = 0"""
                if keyboard.is_pressed("enter"):
                    choosed_x = selectable_list[selected].x
                    choosed_y = selectable_list[selected].y
                    for i in selectable_list:
                        i.selected = False
                    for i in selectable_list:
                        set_object(i.x, i.y, " ")
                    selectable_list = []
                    if is_free_area(choosed_x, choosed_y, 2, 2):
                        player_list[whose_turn-1].gold -= 700
                        set_object(choosed_x, choosed_y, Tower(whose_turn, x=choosed_x, y=choosed_y))
                    else:
                        row_text[22] = "   NOT ENOUGH SPACE FOR TOWER!!!"
                        print_map()
                        sleep(1)
                    break
                elif keyboard.is_pressed("esc"):
                    for i in selectable_list:
                        i.selected = False
                    for i in selectable_list:
                        set_object(i.x, i.y, " ")
                    selectable_list = []
                    break
                elif keyboard.is_pressed("up"):
                    selected -= 1
                elif keyboard.is_pressed("down"):
                    selected += 1
                elif keyboard.is_pressed("right"):
                    for i in range(len(selectable_list)):
                        if selectable_list[i].y == selectable_list[selected].y and header_to_number[selectable_list[i].x] > header_to_number[selectable_list[selected].x]:
                            selected = i
                            sleep(0.05)
                            break
                elif keyboard.is_pressed("left"):
                    for i in reversed(range(len(selectable_list))):
                        if selectable_list[i].y == selectable_list[selected].y and header_to_number[selectable_list[i].x] < header_to_number[selectable_list[selected].x]:
                            selected = i
                            sleep(0.05)
                            break
                if selected >= len(selectable_list):
                    selected = 0
                elif selected < 0:
                    selected = len(selectable_list) - 1

                for i in selectable_list:
                    i.selected = False
                selectable_list[selected].selected = True
                print_map()
                sleep(0.1)





    elif whose_turn == 2:
        if len(player_list[whose_turn - 1].tower_list) >= 6:
            row_text[22] = "   TOO MANY TOWERS!!"
            print_map()
            sleep(1)   
        else:
            for x in list(map(chr, range(65, 65 + map_size[0]))):
                for y in range(map_size[1] // 2, map_size[1]):
                    if is_free(x,y): 
                        set_object(x, y, Selectable(x, y))

    
    #globals()[f"soldier{num_of_towers}"] = Tower(whose_turn, 10, 2, "H", 10)
    #num_of_towers += 1    




def unit_selection():
    options = []
    for i in player_list[whose_turn - 1].soldier_list:
        options.append(i)
    selected = 0
    options[0].mstatus = 1
    row_text[22] = "     CHOSE YOUR UNIT     "
    print_map()
    sleep(0.2)

    for i in range(150):
        keyboard.unblock_key(i)
    while True:
        row_text[22] = "     CHOSE YOUR UNIT     "
        keyp2 = ""
        keyp2 = keyboard.read_key()

        for i in range(150):
            keyboard.block_key(i)

        if keyp2 == "enter":
                move_attack(options[selected])
                for i in range(150):
                    keyboard.block_key(i)
                options = []
                for i in player_list[whose_turn - 1].soldier_list:
                    options.append(i)
                selected = 0
                
        elif keyp2 == "esc":
            for i in options:
                i.mstatus = 0
            break

        elif keyp2 == "up":
            selected -=1

        elif keyp2 == "down":
            selected += 1
        elif keyp2 == "right":
            selected += 1
        elif keyp2 == "left":
            selected -= 1
        if selected >= len(options):
            selected = 0
        elif selected < 0:
            selected = len(options) - 1
        for i in options:
            i.mstatus = 0
        options[selected].mstatus = 1
        print_map()
        sleep(0.2)
        for i in range(150):
            keyboard.unblock_key(i)

def unit_selection_attack(actor):
    options = []
    for x in range(header_to_number[actor.x] - 1, header_to_number[actor.x] + 2):
        for y in range(actor.y - 1, actor.y +2):
            if is_free(number_to_header[x],y) == False:
                if row_list[y].col[number_to_header[x]] not in options:
                    options.append(row_list[y].col[number_to_header[x]])
    
    options.remove(actor)
    row_text[22] = "    CHOOSE TARGET   "

    for i in options:
        if i == "*":
            options.remove("*")
    if len(options) == 0:
        row_text[22] = "\033[91m    THERE IS NOTHING TO ATTACK!  \033[0m"
        print_map()
        sleep(1)
    else:
        selected = 0
        options[0].mstatus = 1
        print_map()
        sleep(0.2)
        for i in range(150):
            keyboard.unblock_key(i)
        while True:
            keyp2 = ""
            keyp2 = keyboard.read_key()
            for i in range(150):
                keyboard.block_key(i)
            if keyp2 == "enter":
                options[selected].hp_down(actor.ap)
                actor.attack_used = True
                for i in options:
                    i.mstatus = 0 
                sleep(0.2) 
                break


            elif keyp2 == "esc":
                for i in options:
                    i.mstatus = 0
                break

            elif keyp2 == "up":
                selected -=1

            elif keyp2 == "down":
                selected += 1
            elif keyp2 == "right":
                selected += 1
            elif keyp2 == "left":
                selected -= 1
            if selected >= len(options):
                selected = 0
            elif selected < 0:
                selected = len(options) - 1

            #row_text[22] = options_str
            for i in options:
                i.mstatus = 0
            options[selected].mstatus = 1
            print_map()
            sleep(0.2)
            for i in range(150):
                keyboard.unblock_key(i)

def unit_selection_attack_tower(actor):
    if actor.attack_used == True:
        row_text[22] = "\033[91m    THIS UNIT HAD TURN ALREADY \033[0m"
        print_map()
        sleep(1)
        row_text[22] = "\033[91m    CHOOSE YOUR TOWER \033[0m"
    else:
        options = []
        for x in range(header_to_number[actor.x] - 3, header_to_number[actor.x] + 4):
            for y in range(actor.y - 3, actor.y +4):
                if is_free(number_to_header[x],y) == False:
                    if row_list[y].col[number_to_header[x]] not in options:
                        options.append(row_list[y].col[number_to_header[x]])
        
        options.remove(actor)
        row_text[22] = "    CHOOSE TARGET   "

        for i in options:
            if i == "*":
                options.remove("*")
        if len(options) == 0:
            row_text[22] = "\033[91m    THERE IS NOTHING TO ATTACK!  \033[0m"
            print_map()
            sleep(1)
            row_text[22] = "\033[91m    CHOOSE YOUR TOWER \033[0m"
        else:
            selected = 0
            options[0].mstatus = 1
            print_map()
            sleep(0.2)
            for i in range(150):
                keyboard.unblock_key(i)
            while True:
                keyp2 = ""
                keyp2 = keyboard.read_key()
                for i in range(150):
                    keyboard.block_key(i)
                if keyp2 == "enter":
                    options[selected].hp_down(actor.ap)
                    actor.attack_used = True
                    for i in options:
                        i.mstatus = 0 
                    sleep(0.2) 
                    row_text[22] = "     CHOOSE YOU TOWER"
                    break


                elif keyp2 == "esc":
                    for i in options:
                        i.mstatus = 0
                    row_text[22] = "     CHOOSE YOU TOWER"
                    break

                elif keyp2 == "up":
                    selected -=1

                elif keyp2 == "down":
                    selected += 1
                elif keyp2 == "right":
                    selected += 1
                elif keyp2 == "left":
                    selected -= 1
                if selected >= len(options):
                    selected = 0
                elif selected < 0:
                    selected = len(options) - 1

                #row_text[22] = options_str
                for i in options:
                    i.mstatus = 0
                options[selected].mstatus = 1
                print_map()
                sleep(0.2)
                for i in range(150):
                    keyboard.unblock_key(i)



def tower_selection():
    options = []
    for i in player_list[whose_turn - 1].tower_list:
        options.append(i)
    selected = 0
    options[0].mstatus = 1
    print_map()
    sleep(0.2)
    for i in range(150):
        keyboard.unblock_key(i)
    while True:
        keyp2 = ""
        keyp2 = keyboard.read_key()
        for i in range(150):
            keyboard.block_key(i)
        if keyp2 == "enter":
            unit_selection_attack_tower(options[selected])
            options = []
            for i in player_list[whose_turn - 1].tower_list:
                options.append(i)
        elif keyp2 == "esc":
            for i in options:
                i.mstatus = 0
            break

        elif keyp2 == "up":
            selected -=1

        elif keyp2 == "down":
            selected += 1
        elif keyp2 == "right":
            selected += 1
        elif keyp2 == "left":
            selected -= 1
        if selected >= len(options):
            selected = 0
        elif selected < 0:
            selected = len(options) - 1

        #row_text[22] = options_str
        for i in options:
            i.mstatus = 0
        options[selected].mstatus = 1
        print_map()
        sleep(0.2)
        for i in range(150):
            keyboard.unblock_key(i)






map_size = [19, 28]
row_text=[]
for i in range(map_size[1]):
    row_text.append(" ")

class Selectable:
    def __repr__(self):
        if self.selected == False:
            return "\033[43m \033[0m"
        else:
            return "\033[42m \033[0m"

    
    def __init__(self, x, y, selected = False):
        self.x = x
        self.y = y
        self.selected = selected
        selectable_list.append(self)


class Player:
    id_class = 0
    id = 0
    def __init__(self, name):
        self.name = name
        self.id = self.id_class
        self.id += 1
        self.castle_list = []
        self.soldier_list = []
        self.tower_list = []
        self.economy_building_list = []
        self.gold = 1000
        self.hp = 0
    def check_hp(self):
        hp = 0
        for i in self.castle_list:
            hp += i.hp
        return hp
    def check_income(self):
        income = len(self.castle_list) * 250 + len(self.economy_building_list) * 75
        return income


player_list = []
player1 = Player("Kuba")
player2 = Player("Wojtek")
player_list.append(player1)
player_list.append(player2)



class Map_Row:
    def __init__(self, id):
        self.id = id
        self.col = {}
        for i in list(map(chr, range(65, 65 + map_size[0]))):
            self.col[i] = " "
    def print_row(self):
        row_str = " "
        row_text_update(self.id)
        for letter in self.col.values():
            row_str += " " + str(letter) + "  "
        if self.id <= 9:
            print("   " + str(self.id) + " |" + row_str + "|" + row_text[self.id])
        else:
            print("  " + str(self.id) + " |" + row_str + "|" + row_text[self.id])

class Soldier:
    price = 300
    def __init__(self, player, hp=10, ap=2, x="B", y=5): #ap stands for attack power
        self.player = player
        self.hp = hp
        self.ap = ap
        self.x = x
        self.y = y
        row_list[y].col[x] = self
        player_list[player - 1].soldier_list.append(self)
        self.mstatus = 0 #menu representation, 0 - normal, 1 green highlited, 2 red highlited
        self.colors = []
        self.move_used = False
        self.attack_used = False
    
    def __repr__(self):
        if self.mstatus == 0:
            if self.player == 1:
                return "\033[36m;\033[0m"
            elif self.player == 2:
                return "\033[91m;\033[0m"
        elif self.mstatus == 1:
            return "\033[42m;\033[0m"

    def menu_repr(self, menu_id):
        if self.mstatus == 0: #normal
            if self.player == 1:
                self.colors = ["\033[34m", "\033[00m"]
            elif self.player == 2:
                self.colors = ["\033[31m", "\033[00m"]
        elif self.mstatus == 1: # highlited
            self.colors = ["\033[42m", "\033[42m"]
        elif self.mstatus == 2: # disable
            self.colors = ["\033[41m", "\033[41m"]
        

        return  self.colors[1] + str(menu_id) + " HP: " + self.colors[0] + str(self.hp) + self.colors[1] + "/" + self.colors[0] + "10 " + self.colors[1]  + "Pos: "+ self.colors[0] + str(self.x) + self.colors[1] + ":" + self.colors[0] + str(self.y) + "\033[00m]  "



    def hp_down(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        set_object(self.x, self.y, " ")
        player_list[self.player-1].soldier_list.remove(self)
        del self

    def xy(self, x, y):  #settnig position of a soldier
        row_list[y].col[x] = self
        self.x = x
        self.y = y

class Economy_building:
    price = 400
    def __init__(self, player, hp=10, x="B", y=5):
        self.player = player
        self.hp = hp
        self.x = x
        self.y = y
        row_list[y].col[x] = self
        player_list[player - 1].economy_building_list.append(self)
        self.mstatus = 0
    
    def __repr__(self):
        if self.mstatus == 0:
            if self.player == 1:
                return "\033[36m$\033[0m"
            elif self.player == 2:
                return "\033[91m$\033[0m"
        if self.mstatus == 1:
            return "\033[42m$\033[0m"

    def hp_down(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        set_object(self.x, self.y, " ")
        player_list[self.player-1].economy_building_list.remove(self)
        del self

    def xy(self, x, y):  #settnig position of a economy buikding
        row_list[y].col[x] = self
        self.x = x
        self.y = y


class Tower:
    price = 700
    def __init__(self, player, hp=10, ap=10, x="B", y=5): #ap stands for attack power
        self.player = player
        self.hp = hp
        self.ap = ap
        self.x = x
        self.y = y
        self.width = 2
        self.height = 2
        for a in range(self.width):
            for b in range(self.height):
                set_object(headshift(x, a), y + b, self)
        player_list[player - 1].tower_list.append(self)
        self.mstatus = 0 #menu representation, 0 - normal, 1 green highlited, 2 red highlited
        self.colors = []
        self.attack_used = False
    
    def __repr__(self):
        if self.mstatus == 0:
            if self.player == 1: 
                return "\033[34m#\033[00m"
            elif self.player == 2:
                return "\033[31m#\033[00m"
        elif self.mstatus == 1:
            return "\033[42m#\033[00m"

    def menu_repr(self, menu_id):
        if self.mstatus == 0: #normal
            if self.player == 1:
                self.colors = ["\033[34m", "\033[00m"]
            elif self.player == 2:
                self.colors = ["\033[31m", "\033[00m"]
        elif self.mstatus == 1: # highlited
            self.colors = ["\033[42m", "\033[42m"]
        elif self.mstatus == 2: # disable
            self.colors = ["\033[41m", "\033[41m"]
        

        return  self.colors[1] + str(menu_id) + " HP: " + self.colors[0] + str(self.hp) + self.colors[1] + "/" + self.colors[0] + "10 " + self.colors[1]  + "Pos: "+ self.colors[0] + str(self.x) + self.colors[1] + ":" + self.colors[0] + str(self.y) + "\033[00m]  "


    def hp_down(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        for a in range(self.width):
            for b in range(self.height):
                set_object(headshift(self.x, a), self.y + b, " ")
        player_list[self.player-1].tower_list.remove(self)
        del self

    def xy(self, x, y):  #settnig position of a tower
        row_list[y].col[x] = self
        self.x = x
        self.y = y

def pos(x, y):
    return row_list[y].col[x]

class Castle:
    id = 0
    def __init__(self, player, position, size, hp):
        self.player = player
        self.position = position
        self.hp = hp
        self.width = size[0]
        self.height = size[1]
        self.income = 100
        player_list[player-1].castle_list.append(self)
        for x in range(self.width):
            for y in range(self.height):
                set_object(headshift(self.position[0], x), self.position[1] + y, self)
        self.mstatus = 0


    def __repr__(self):
        if self.mstatus == 0:
            if self.player == 1:
                return "\033[36mX\033[0m"
            elif self.player == 2:
                return "\033[91mX\033[0m"
        elif self.mstatus == 1:
            return "\033[42mX\033[0m"
    
    def hp_down(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        for x in range(self.width):
            for y in range(self.height):
              set_object(headshift(self.position[0], x), self.position[1] + y, " ")
        player_list[self.player-1].castle_list.remove(self)

        del self





def headshift(x, value):
    number = header_to_number[x]
    number += value
    return number_to_header[number]

def set_object(x, y, value): #settings objects for position
    row_list[y].col[x] = value

#map creation section
number_to_header = list(map(chr, range(65, 91)))
header_to_number = {}
for i in number_to_header:
    header_to_number[i] = number_to_header.index(i)
map_header = ""
map_header += "        "
for i in list(map(chr, range(65, 65 + map_size[0]))):
    map_header += i + "   "
#map_header = ["R |  A   B   C   D   E   F   G   H   I   J   |"] =
map_header += "                               KINGDOM BATTLERS            "
row_list = []
for i in range(map_size[1]):
    row_list.append(Map_Row(i))
# create border
for i in list(map(chr, range(65, 65 + map_size[0]))):
    set_object(i, 0, "*")
for i in list(map(chr, range(65, 65 + map_size[0]))):
    set_object(i, map_size[1] - 1, "*")
for i in range(map_size[1]):
    set_object("A", i, "*")
for i in range(map_size[1]):
    set_object(list(map(chr, range(65, 65 + map_size[0])))[-1], i, "*")


# create castles
""" row_list[0].col["E"] = "X"
row_list[0].col["F"] = "X"
row_list[1].col["E"] = "X"
row_list[1].col["F"] = "X"
row_list[8].col["E"] = "X"
row_list[8].col["F"] = "X"
row_list[9].col["E"] = "X"
row_list[9].col["F"] = "X" """
def print_map():
    print()
    print(map_header)
    print("      " + map_size[0] * 4 * "-" + "-" + "   " + "-" * 74)
    for row in row_list:
        row.print_row()
    print("      " + map_size[0] * 4 * "-" + "-")

def is_free(x, y): #checking if position is free
    if header_to_number[x] < map_size[0] and y <= map_size[1] and header_to_number[x] >= 0 and y >= 0:
        if row_list[y].col[x] == " ":
            return True
        else:
            return False
    else:
        return True
def is_free_area(x, y, width, height): #checking if area is free
    for a in range(width):
        for b in range(height):
            if row_list[y + b].col[headshift(x, b+1)] != " ":
                return False
    return True


    if row_list[y].col[x] == " ":
        return True
    else:
        return False

def movement(walker): # mechanics of prompting for movement of soldiers
    steps_left = 15
    while steps_left > 0:
        row_text[22] = "    STEPS LEFT: " + str(steps_left)
        print_map()
        sleep(0.2)
        for i in range(150):
            keyboard.unblock_key(i)
        keyp = ""
        keyp = keyboard.read_key()
        for i in range(150):
            keyboard.block_key(i)
        if keyp == "esc":
            walker.move_used = True
            break
        if keyp == "enter":
            walker.move_used = True
            break
        elif keyp == "up":
            for i in range(3):
                keyboard.send('backspace')
            if is_free(walker.x, walker.y - 1):
                set_object(walker.x, walker.y, " ")
                walker.xy(walker.x, walker.y - 1)
            else:
                row_text[22] = occupied
                print_map()
                sleep(1)
        elif keyp == "down":
            for i in range(3):
                keyboard.send('backspace')
            if is_free(walker.x, walker.y + 1):
                set_object(walker.x, walker.y, " ")
                walker.xy(walker.x, walker.y + 1)
            else:
                row_text[22] = occupied
                print_map()
                sleep(1)
        elif keyp == "right":
            for i in range(3):
                keyboard.send('backspace')
            if is_free(headshift(walker.x, 1), walker.y):
                set_object(walker.x, walker.y, " ")
                walker.xy(headshift(walker.x, 1), walker.y)
            else:
                row_text[22] = occupied
                print_map()
                sleep(1)
        elif keyp == "left":
            for i in range(3):
                keyboard.send('backspace')
            if is_free(headshift(walker.x, -1), walker.y):
                set_object(walker.x, walker.y, " ")
                walker.xy(headshift(walker.x, -1), walker.y)
            else:
                row_text[22] = occupied
                print_map()
                sleep(1.5)
        
        steps_left -= 1
        row_text[22] = "    STEPS LEFT: " + str(steps_left)
        print_map()
        sleep(0.2)
    walker.move_used = True



def attack(walker): # mechanics of attack
    choice = input("Choose the direction of attack: ")
    if choice == "exit":
        pass
    elif choice == "up":
        if is_free(walker.x, walker.y - 1):
            print("Nothing to attack")
            attack(walker)
        else:
            row_list[walker.y - 1].col[walker.x].hp_down(walker.ap)
    elif choice == "down":
        if is_free(walker.x, walker.y + 1):
            print("Nothing to attack")
            attack(walker)
        else:
            row_list[walker.y + 1].col[walker.x].hp_down(walker.ap)
    elif choice == "right":
        if is_free(headshift(walker.x, 1), walker.y):
            print("Nothing to attack")
            attack(walker)
        else:
            row_list[walker.y].col[headshift(walker.x, 1)].hp_down(walker.ap)
    elif choice == "left":
        if is_free(headshift(walker.x, -1), walker.y):
            print("Nothing to attack")
            attack(walker)
        else:
            row_list[walker.y].col[headshift(walker.x, -1)].hp_down(walker.ap)


#testing 
"""soldier1 = Soldier(1, x="C", y=5, ap=10)
soldier2 = Soldier(2, x="F", y=19)
soldier3 = Soldier(1, x="N", y=11)
soldier4 = Soldier(1, x="H", y=10)
soldier5 = Soldier(1, x="P", y=20)
soldier6 = Soldier(1, x="O", y=13)
soldier7 = Soldier(1, x="K", y=13)
#soldier1.xy("N", 12)
#soldier2.xy("I", 9)

"""
castle1 = Castle(1,["H",1], [4, 2], 50)
castle2 = Castle(2,["H",25], [4, 2], 50)
"""
castle3 = Castle(1,["C",15], [4, 2], 50)
tower1 = Tower(1,10,10,x="D",y=5)
tower2 = Tower(1,10,10,x="B",y=8)
tower3 = Tower(1,10,10,x="J",y=5)
tower4 = Tower(2,10,10,x="M",y=19)
tower5 = Tower(1,10,10,x="Q",y=7)
tower6 = Tower(1,10,10,x="K",y=10)

economy1 = Economy_building(1,1,x="F",y=2)
economy2 = Economy_building(2,1,x="B",y=22)
"""
# INTERFACE SECTION
def row_text_update(index):
    if index == 0:
        row_text[index] = "   Name: \033[34m" + player_list[0].name.upper() + "\033[0m" + "  Castle HP: \033[34m" + str(player1.check_hp()) + "\033[00m / \033[34m" + str(len(player1.castle_list)*50) + "\033[00m" + "  Gold: " + "\033[34m" + str(player_list[0].gold) + "\033[00m $    Income: \033[34m" + str(player1.check_income()) + "\033[00m $"
    elif index == 2:
        row_text[index] = "   Soldiers:"
    elif index == 3:
        row_text[index] = "  "
        for i in range(3):
            if len(player1.soldier_list)>= i+1:
                row_text[index] += "[" + player1.soldier_list[i].menu_repr(i+1) #+ " ]" #str(i+1)  + " HP: \033[34m" + str(player1.soldier_list[i].hp) + "\033[00m/\033[34m10\033[00m " + "Pos: \033[34m" + str(player1.soldier_list[i].x) + "\033[00m:\033[34m" + str(player1.soldier_list[i].y) + "\033[00m]  "
    elif index == 4:
        row_text[index] = "  "
        for i in range(3,6):
            if len(player1.soldier_list)>= i+1:
                row_text[index] += "[" + player1.soldier_list[i].menu_repr(i+1)
    elif index == 6:
        row_text[index] = "   Towers:"
    elif index == 7:
        row_text[index] = "  "
        for i in range(3):
            if len(player1.tower_list)>= i+1:
                row_text[index] += "[" + player1.tower_list[i].menu_repr(i+1) #+ " ]" #str(i+1)  + " HP: \033[34m" + str(player1.soldier_list[i].hp) + "\033[00m/\033[34m10\033[00m " + "Pos: \033[34m" + str(player1.soldier_list[i].x) + "\033[00m:\033[34m" + str(player1.soldier_list[i].y) + "\033[00m]  "
    elif index == 8:
        row_text[index] = "  "
        for i in range(3,6):
            if len(player1.tower_list)>= i+1:
                row_text[index] += "[" + player1.tower_list[i].menu_repr(i+1) #+ " ]" #str(i+1)  + " HP: \033[34m" + str(player1.soldier_list[i].hp) + "\033[00m/\033[34m10\033[00m " + "Pos: \033[34m" + str(player1.soldier_list[i].x) + "\033[00m:\033[34m" + str(player1.soldier_list[i].y) + "\033[00m]  "
    elif index == 9:
        row_text[index] = "  " + "-" * 73
 
    # Interface for second player:
    elif index == 10:
        row_text[index] = "   Name: \033[31m" + player_list[1].name.upper() + "\033[0m" + "  Castle HP: \033[31m" + str(player2.check_hp()) + "\033[00m / \033[31m" + str(len(player2.castle_list)*50) + "\033[00m" + "  Gold: " + "\033[31m" + str(player_list[1].gold) + "\033[00m $    Income: \033[31m" + str(player2.check_income()) + "\033[00m $"
    elif index == 12:
        row_text[index] = "   Soldiers:"
    elif index == 13:
        row_text[index] = "  "
        for i in range(3):
            if len(player2.soldier_list)>= i+1:
                row_text[index] += "[" + player2.soldier_list[i].menu_repr(i+1)
    elif index == 14:
        row_text[index] = "  "
        for i in range(3,6):
            if len(player2.soldier_list)>= i+1:
                row_text[index] += "[" + player2.soldier_list[i].menu_repr(i+1)
    elif index == 16:
        row_text[index] = "   Towers:"
    elif index == 17:
        row_text[index] = "  "
        for i in range(3):
            if len(player2.tower_list)>= i+1:
                row_text[index] += "[" + player2.tower_list[i].menu_repr(i+1) #+ " ]" #str(i+1)  + " HP: \033[34m" + str(player1.soldier_list[i].hp) + "\033[00m/\033[34m10\033[00m " + "Pos: \033[34m" + str(player1.soldier_list[i].x) + "\033[00m:\033[34m" + str(player1.soldier_list[i].y) + "\033[00m]  "
    elif index == 18:
        row_text[index] = "  "
        for i in range(3,6):
            if len(player2.tower_list)>= i+1:
                row_text[index] += "[" + player2.tower_list[i].menu_repr(i+1) #+ " ]" #str(i+1)  + " HP: \033[34m" + str(player1.soldier_list[i].hp) + "\033[00m/\033[34m10\033[00m " + "Pos: \033[34m" + str(player1.soldier_list[i].x) + "\033[00m:\033[34m" + str(player1.soldier_list[i].y) + "\033[00m]  "
    elif index == 19:
        row_text[index] = "  " + "-" * 73
    elif index == 21:
        if whose_turn == 1:
            row_text[index] = "\033[34m  " + player_list[whose_turn-1].name.upper() + "\033[00m turn:"
        elif whose_turn == 2:
            row_text[index] = "\033[31m  " + player_list[whose_turn-1].name.upper() + "\033[00m turn:"




is_working = True
while is_working:
    main_menu()
    choice = input("What you want to do: ")
    
    if choice == "move":
        movement(soldier1)
    elif choice == "attack":
        attack(soldier1)
    elif choice == "exit":
        quit()
    




print()
print()