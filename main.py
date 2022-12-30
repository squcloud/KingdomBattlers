#glossary
occupied = "cannot move here because this place is occupied"

map_size = [20, 10]
class Map_Row:
    def __init__(self, id):
        self.id = id
        self.col = {}
        for i in list(map(chr, range(65, 65 + map_size[0]))):
            self.col[i] = " "
    def print_row(self):
        row_str = " "
        for letter in self.col.values():
            row_str += " " + letter + "  "
        print("  " + str(self.id) + " |" + row_str + "|")

class Soldier:
    def __init__(self, player, hp=10, ap=2): #ap stands for attack power
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

    def xy(self, x, y):  #settnig position of a soldier
        row_list[y].col[x] = str(self)
        self.x = x
        self.y = y
def pos(x, y):
    return row_list[y].col[x]

def headshift(x, value):
    number = header_to_number[x]
    number += value
    return number_to_header[number]

#map creation section
number_to_header = list(map(chr, range(65, 91)))
header_to_number = {}
for i in number_to_header:
    header_to_number[i] = number_to_header.index(i)
map_header = ""
map_header += "       "
for i in list(map(chr, range(65, 65 + map_size[0]))):
    map_header += i + "   "
#map_header = ["R |  A   B   C   D   E   F   G   H   I   J   |"]
row_list = []
for i in range(10):
    row_list.append(Map_Row(i))
# create castles
row_list[0].col["E"] = "X"
row_list[0].col["F"] = "X"
row_list[1].col["E"] = "X"
row_list[1].col["F"] = "X"
row_list[8].col["E"] = "X"
row_list[8].col["F"] = "X"
row_list[9].col["E"] = "X"
row_list[9].col["F"] = "X"
def print_map():
    print()
    print(map_header)
    print("     " + map_size[0] * 4 * "-" + "-")
    for row in row_list:
        row.print_row()
    print("     " + map_size[0] * 4 * "-" + "-")

def is_free(x, y): #checking if position is free
    if row_list[y].col[x] == " ":
        return True
    else:
        return False
def set_object(x, y, value): #settings objects for position
    row_list[y].col[x] = value
def movement(walker): # mechanics of prompting for movement of soldiers
    choice = input("Twoj wybor: ")
    if choice == "exit":
        quit()
    elif choice == "up":
        if is_free(walker.x, walker.y - 1):
            set_object(walker.x, walker.y, " ")
            walker.xy(walker.x, walker.y - 1)
        else:
            print(occupied)
    elif choice == "down":
        if is_free(walker.x, walker.y + 1):
            set_object(walker.x, walker.y, " ")
            walker.xy(walker.x, walker.y + 1)
        else:
            print(occupied)
    elif choice == "right":
        if is_free(headshift(walker.x, 1), walker.y):
            set_object(walker.x, walker.y, " ")
            walker.xy(headshift(walker.x, 1), walker.y)
        else:
            print(occupied)
    elif choice == "left":
        if is_free(headshift(walker.x, -1), walker.y):
            set_object(walker.x, walker.y, " ")
            walker.xy(headshift(walker.x, -1), walker.y)
        else:
            print(occupied)

#testing 
soldier1 = Soldier(1)
soldier2 = Soldier(2)
soldier1.xy("A", 5)
soldier2.xy("G", 3)

is_working = True
while is_working:
    print_map()
    movement(soldier2)




print()
print()