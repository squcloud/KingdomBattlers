print()
print()
class Map_Row:
    def __init__(self, id):
        self.id = id
        self.rows = {"A" : " ", "B" : " ", "C" : " ", "D" : " ", "E" : " ", "F" : " ", "G" : " ", "G" : " ", "I" : " ", "J" : " ", }
    def print_row(self):
        row_str = " "
        for letter in self.rows.values():
            row_str += " " + letter + "  "
        print("  " + str(self.id) + " |" + row_str)

#Setting up the header of the map and the list of rows
map_header = ["R |  A   B   C   D   E   F   G   H   I   J"]
row_list = []
for i in range(10):
    row_list.append(Map_Row(i))


#testing of printing map
print(map_header)
for row in row_list:
    row.print_row()



def print_map():
    pass

print()
print()