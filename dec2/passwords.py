'''Program should split up each line in data.txt, separate password rules
and password and look for valid passwords'''

'''each line contains 3 components, 1st is the min and maximum number a letter
can appear in a password, next is the letter in question, after that we get
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


def find_valid_passwords(data_list):
    '''Parse through file and check if password fits rules'''
    valid_count = 0
    for i in data_list:
        try:
            min_num, max_num = i[0].split("-")
            min_num = int(min_num)
            max_num = int(max_num)
            rule_letter = i[1].replace(":", "")
        except:  # For some reason the last index in data_list is empty string
            #  This exception catches it and returns our valid number
            print(i)
            return valid_count
        for j in i:
            letter_count = 0

            for letter in i[2]:
                if letter == rule_letter:
                    letter_count += 1

        if letter_count >= min_num and letter_count <= max_num:
            valid_count += 1

    return valid_count


def main():
    file_object = open_file("data.txt")
    data_list = file_to_list(file_object)
    print(find_valid_passwords(data_list))


main()
