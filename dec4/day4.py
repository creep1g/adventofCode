# Something wrong, returns 159 when it should return 156

def get_data(filename):
    file_object = open(filename, "r")
    return file_object


def data_to_list(data):
    data_list = []
    temp_list = []
    for line in data:
        if line.split() != []:
            for j in line.split():
                temp_list.append(j)
        else:
            data_list.append(temp_list)
            temp_list = []
    return data_list


def count_valid(data_list, check_list):
    valid = 0
    for data in data_list:
        count = 0
        for index in data:
            key, value = index.strip().split(":")
            if key == "cid":
                continue
            else:
                if check_key_value(key, value, check_list):
                    count += 1
                else:
                    break
        if count >= 7:
            valid += 1
    return valid


def check_key_value(key, value, check_list):
    eyecolors = "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
    if key == "cid":
        return 0
    elif key == "pid":
        return 1
    else:
        if key in check_list:
            if (key == check_list[0] and
                    (int(value) >= 1920 and int(value) <= 2002)):
                return 1
            elif (key == check_list[1] and
                    (int(value) >= 2010 and int(value) <= 2020)):
                return 1
            elif (key == check_list[2] and
                    (int(value) >= 2020 and int(value) <= 2030)):
                return 1
            elif key == check_list[3]:
                if value[-2:] == "cm":
                    if int(value[:-2:]) >= 150 and int(value[:-2:]) <= 193:
                        return 1
                elif value[-2:] == "in":
                    if int(value[:-2:]) >= 59 and int(value[:-2:]) <= 76:
                        return 1
            elif (key == check_list[4] and
                    (value[0] == "#" and len(value[1:]) == 6)):
                return 1

            elif key == check_list[5] and value in eyecolors:
                return 1
        else:
            return 0

def main():
    needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    data = get_data("data.txt")
    data_list = data_to_list(data)
    valid = count_valid(data_list, needed)
    print(valid)


main()
