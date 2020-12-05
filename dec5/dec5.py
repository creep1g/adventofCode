with open("data.txt") as file:
    data = file.read()
    ticket = data.split()

seats = []

row_list = [i for i in range(0, 127+1)]
col_list = [j for j in range(0, 7+1)]
highest = 0
rows = []
cols = []
IDs = []
for data in ticket:
    temp_list = row_list
    for char in data:
        length = round(len(temp_list)//2)
        if char == "F":
            temp_list = temp_list[:length]
        elif char == "B":
            temp_list = temp_list[length:]
    rows.append(temp_list[0])

for data in ticket:
    temp_list = col_list
    for char in data[-3:]:
        length = round(len(temp_list)//2)
        if char == "R":
            temp_list = temp_list[length:]
        elif char == "L":
            temp_list = temp_list[:length]
    cols.append(temp_list[0])

counter = 0
while counter < len(rows):
    ID = (rows[counter] * 8) + cols[counter]
    if ID > highest:
        highest = ID

    IDs.append(ID)
    counter += 1

counter = 0
IDs.sort()
while counter < len(IDs):
    ID = IDs[counter]
    IDabove = IDs[counter + 1]
    IDbelow = IDs[counter - 1]
    if counter == 0:
        IDbelow = ID -1
    if IDabove > len(IDs):
        break
    if ID - 1 != IDbelow:
        print("ID:",ID)
        print("BE",IDbelow)
        our = ID - 1
    elif ID + 1 != IDabove:
        print("ID:",ID)
        print("AB",IDabove)
    counter += 1
print("Our ID:", our)
print("Highest:", highest)

