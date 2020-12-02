'''Program should split up each line in data.txt, separate password rules
and password and look for valid passwords'''

'''each line contains 3 components, 1st is a range of indecies where
exactly 1  of them must contain the given letter in a password,
next is the letter in question, after that we get
the password'''


def open_file(filename):
    try:
        file_obj = open(filename, "r")
        return file_obj
    except FileNotFoundError:
        return None


def file_to_list(file_obj):
    '''parse through list, create a list of lists'''
    file_list = []
    for line in file_obj:
        file_list.append(line.strip().split(" "))

    return file_list


def slit_list(data_list):
    top, bottom = data_list[0].split("-")
    char = data_list[1].replace(":", "")
    password = data_list[2]
    return (int(top), int(bottom), char, password)


def find_valid_passwords(data_list):
    '''Parse through file and check if password fits rules'''
    valid = 0
    for row in data_list:
        top, bottom, char, password = slit_list(row)
        print(top, bottom, char, password)
        if password[top - 1] == char or password[bottom - 1] == char:
            valid += 1
    return valid

## this is not correct should return 699
def main():
    file_object = open_file("data.txt")
    data_list = file_to_list(file_object)
    print(find_valid_passwords(data_list))


main()
