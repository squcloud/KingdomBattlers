#import section
import keyboard
import sys
from time import sleep
#glossary
occupied = "cannot move here because this place is occupied"


map_size = [19, 25]
row_text=[]
for i in range(map_size[1]):
    row_text.append(" ")

class Player:
    id_class = 0
    id = 0
    def __init__(self, name):
        self.name = name
        self.id = self.id_class
        self.id += 1
        self.soldier_list = []
        self.tower_list = []
        self.economy_building_list = []
        self.gold = 1000

player_list = []
player1 = Player("Kuba")
player2 = Player("Wojtek")
player_list.append(player1)
player_list.append(player2)



castles = []
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
    def __init__(self, player, hp=10, ap=2, x="B", y=5): #ap stands for attack power
        self.player = player
        self.hp = hp
        self.ap = ap
        self.x = x
        self.y = y
        row_list[y].col[x] = self
        player_list[player - 1].soldier_list.append(self)
    
    def __repr__(self):
        if self.player == 1:
            return "\033[36m;\033[0m"
        elif self.player == 2:
            return "\033[91m;\033[0m"

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
    def __init__(self, player, hp=10, x="B", y=5):
        self.player = player
        self.hp = hp
        self.x = x
        self.y = y
        row_list[y].col[x] = self
        player_list[player - 1].economy_building_list.append(self)
    
    def __repr__(self):
        if self.player == 1:
            return "\033[36m$\033[0m"
        elif self.player == 2:
            return "\033[91m$\033[0m"

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
    def __init__(self, player, hp=10, ap=4, x="B", y=5): #ap stands for attack power
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
    
    def __repr__(self):
        if self.player == 1: 
            return "\033[34m#\033[00m"
        elif self.player == 2:
            return "\033[33m#\033[00m"

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
        self.width = 4
        self.height = 2
        self.income = 100

    def __repr__(self):
        if self.player == 1:
            return "\033[34mX\033[0m"
        elif self.player == 2:
            return "\033[33mX\033[0m"
    
    def hp_down(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        for x in range(self.width):
            for y in range(self.height):
              set_object(headshift(self.position[0], x), self.position[1] + y, " ")
        del self

def create_castle(player, position, size, hp):
    Castle.id += 1
    castles.append(Castle(player, position, size, hp))
    for x in range(size[0]):
        for y in range(size[1]):
            set_object(headshift(position[0], x), position[1] + y, castles[Castle.id - 1])
    



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
#map_header = ["R |  A   B   C   D   E   F   G   H   I   J   |"]
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
    print("      " + map_size[0] * 4 * "-" + "-" + "              KINGDOM BATTLERS")
    for row in row_list:
        row.print_row()
    print("      " + map_size[0] * 4 * "-" + "-")

def is_free(x, y): #checking if position is free
    if row_list[y].col[x] == " ":
        return True
    else:
        return False
def is_free_area(x, y, width, height): #checking if area is free
    for a in range(width):
        for b in range(height):
            if row_list[y + b].col[headshift(x, b)] != " ":
                return False
    return True


    if row_list[y].col[x] == " ":
        return True
    else:
        return False

def movement(walker): # mechanics of prompting for movement of soldiers
    print("Press arrow:")
    while True:
        keyp = ""
        keyp = keyboard.read_key()
        for i in range(150):
            keyboard.block_key(i)
        if keyp == "esc":
            for i in range(150):
                 keyboard.unblock_key(i)
            keyboard.send('backspace')
            break
        elif keyp == "up":
            for i in range(3):
                keyboard.send('backspace')
            if is_free(walker.x, walker.y - 1):
                set_object(walker.x, walker.y, " ")
                walker.xy(walker.x, walker.y - 1)
            else:
                print(occupied)
        elif keyp == "down":
            for i in range(3):
                keyboard.send('backspace')
            if is_free(walker.x, walker.y + 1):
                set_object(walker.x, walker.y, " ")
                walker.xy(walker.x, walker.y + 1)
            else:
                print(occupied)
        elif keyp == "right":
            for i in range(3):
                keyboard.send('backspace')
            if is_free(headshift(walker.x, 1), walker.y):
                set_object(walker.x, walker.y, " ")
                walker.xy(headshift(walker.x, 1), walker.y)
            else:
                print(occupied)
        elif keyp == "left":
            for i in range(3):
                keyboard.send('backspace')
            if is_free(headshift(walker.x, -1), walker.y):
                set_object(walker.x, walker.y, " ")
                walker.xy(headshift(walker.x, -1), walker.y)
            else:
                print(occupied)
        print_map()
        print("Press arrow:")
        sleep(0.2)
        for i in range(150):
            keyboard.unblock_key(i)

def attack(walker): # mechanics of prompting for attack of soldier
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
soldier1 = Soldier(1, x="C", y=5)
soldier2 = Soldier(2, x="F", y=19)
soldier3 = Soldier(1, x="N", y=11)
soldier4 = Soldier(1, x="H", y=10)
soldier5 = Soldier(1, x="P", y=20)
soldier6 = Soldier(1, x="O", y=13)
soldier7 = Soldier(1, x="K", y=13)
#soldier1.xy("N", 12)
#soldier2.xy("I", 9)

create_castle(1,["H",1], [4, 2], 50)
create_castle(2,["H",22], [4, 2], 50)
tower1 = Tower(1,10,4,x="D",y=5)
tower2 = Tower(1,10,4,x="B",y=8)
tower3 = Tower(1,10,4,x="J",y=5)
tower4 = Tower(2,10,4,x="M",y=19)
tower5 = Tower(1,10,4,x="Q",y=7)
tower6 = Tower(1,10,4,x="K",y=10)

economy1 = Economy_building(1,1,x="F",y=2)
economy2 = Economy_building(2,1,x="B",y=22)

# INTERFACE SECTION
def row_text_update(index):
    if index == 1:
        row_text[index] = "     Name:   \033[34m" + player_list[0].name.upper() + "\033[0m" + "     Castle HP: \033[34m" + str(castles[0].hp) + "\033[00m / \033[34m50\033[00m" + "  Gold: " + "\033[34m" + str(player_list[0].gold) + "\033[00m"
    elif index == 3:
        row_text[index] = "   Soldiers:"
    elif index == 4:
        row_text[index] = "  "
        for i in range(3):
            if len(player1.soldier_list)>= i+1:
                row_text[index] += "[" + str(i+1)  + " HP: \033[34m" + str(player1.soldier_list[i].hp) + "\033[00m/\033[34m10\033[00m " + "Pos: \033[34m" + str(player1.soldier_list[i].x) + "\033[00m:\033[34m" + str(player1.soldier_list[i].y) + "\033[00m]  "
    elif index == 5:
        row_text[index] = "  "
        for i in range(3,6):
            if len(player1.soldier_list)>= i+1:
                row_text[index] += "[" + str(i+1)  + " HP: \033[34m" + str(player1.soldier_list[i].hp) + "\033[00m/\033[34m10\033[00m " + "Pos: \033[34m" + str(player1.soldier_list[i].x) + "\033[00m:\033[34m" + str(player1.soldier_list[i].y) + "\033[00m]  "
    elif index == 7:
        row_text[index] = "   Towers:"
    elif index == 8:
        row_text[index] = "  "
        for i in range(3):
            if len(player1.tower_list)>= i+1:
                row_text[index] += "[" + str(i+1)  + " HP: \033[34m" + str(player1.tower_list[i].hp) + "\033[00m/\033[34m10\033[00m " + "Pos: \033[34m" + str(player1.tower_list[i].x) + "\033[00m:\033[34m" + str(player1.tower_list[i].y) + "\033[00m]  "
    elif index == 9:
        row_text[index] = "  "
        for i in range(3,6):
            if len(player1.tower_list)>= i+1:
                row_text[index] += "[" + str(i+1)  + " HP: \033[34m" + str(player1.tower_list[i].hp) + "\033[00m/\033[34m10\033[00m " + "Pos: \033[34m" + str(player1.tower_list[i].x) + "\033[00m:\033[34m" + str(player1.tower_list[i].y) + "\033[00m]  "



is_working = True
while is_working:
    print_map()
    choice = input("What you want to do: ")
    
    if choice == "move":
        movement(soldier1)
    elif choice == "attack":
        attack(soldier1)
    elif choice == "exit":
        quit()
    




print()
print()