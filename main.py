#import section
import keyboard
import sys
from time import sleep
#glossary
occupied = "cannot move here because this place is occupied"

map_size = [19, 25]
castles = []
class Map_Row:
    def __init__(self, id):
        self.id = id
        self.col = {}
        for i in list(map(chr, range(65, 65 + map_size[0]))):
            self.col[i] = " "
    def print_row(self):
        row_str = " "
        for letter in self.col.values():
            row_str += " " + str(letter) + "  "
        if self.id <= 9:
            print("   " + str(self.id) + " |" + row_str + "|")
        else:
            print("  " + str(self.id) + " |" + row_str + "|")

class Soldier:
    def __init__(self, player, hp=10, ap=2, x=5, y=5): #ap stands for attack power
        self.player = player
        self.hp = hp
        self.ap = ap
        self.x = 0
        self.y = 0
    
    def __repr__(self):
        if self.player == 1:
            return "O"
        elif self.player == 2:
            return "@"

    def hp_down(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        set_object(self.x, self.y, " ")
        del self

    def xy(self, x, y):  #settnig position of a soldier
        row_list[y].col[x] = self
        self.x = x
        self.y = y

class Tower:
    def __init__(self, player, hp=10, ap=4, x=5, y=5): #ap stands for attack power
        self.player = player
        self.hp = hp
        self.ap = ap
        self.x = x
        self.y = y
        self.width = 2
        self.height = 2
        for a in range(self.width):
            for b in range(self.height):
                set_object(headshift(number_to_header[x], a), y + b, self)
    
    def __repr__(self):
        return "#"

    def hp_down(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        set_object(self.x, self.y, " ")
        del self

    def xy(self, x, y):  #settnig position of a soldier
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

    def __repr__(self):
        return "X"

def create_castle(player, position, size, hp):
    Castle.id += 1
    castles.append(Castle(player, position, size, hp))
    for x in range(size[0]):
        for y in range(size[1]):
            set_object(headshift(position[0], x), position[1] + y, str(castles[Castle.id - 1]))
    



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
    print("      " + map_size[0] * 4 * "-" + "-")
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
soldier1 = Soldier(1)
soldier2 = Soldier(2)
soldier1.xy("N", 12)
soldier2.xy("I", 9)

create_castle(1,["H",1], [4, 2], 10)
create_castle(1,["H",17], [4, 2], 10)
pies = Tower(1,10,4,5,5)
is_working = True
while is_working:
    print_map()
    print(soldier2.hp)
    choice = input("What you want to do: ")
    
    if choice == "move":
        movement(soldier1)
    elif choice == "attack":
        attack(soldier1)
    elif choice == "exit":
        quit()
    




print()
print()