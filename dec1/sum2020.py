'''Find two entries that sum up to 2020 and return the product
of those two numbers '''


def open_file(filename):
    try:
        file_obj = open(filename, "r")
        return file_obj
    except FileNotFoundError:
        return None


def process_file(file_obj):
    '''parse through file and add each line as an int to a list'''
    line_list = []
    for entrie in file_obj:
        line_list.append(int(entrie.strip()))
    return line_list


def find_sum(line_list, break_sum):
    '''Find the two entries that sum up to 2020'''
    for num_1 in line_list:
        for num_2 in line_list:
            for num_3 in line_list:
                num_4 = num_1 + num_2 + num_3
                if num_4 == 2020:
                    return (num_1, num_2, num_3)


def print_output(num_1, num_2, num_3):
    print("{} + {} + {} = {} and {} * {} * {} = {}".
          format(num_1, num_2, num_3, num_1 + num_2 + num_3,num_1, num_2, num_3,
                 num_1 * num_2 * num_3))


def main():
    filename = "data.txt"
    file_obj = open_file(filename)
    if file_obj:
        line_list = process_file(file_obj)
        num_1, num_2, num_3 = find_sum(line_list, 2020)
        print_output(num_1, num_2, num_3)


main()
