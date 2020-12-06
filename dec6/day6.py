import time
with open("data.txt") as file:
    data = file.read()
    data = data.strip().split("\n\n")


#  Part 1

yes_sum = 0

for group in data:
    unique_answers = set()
    for answer in group:
        if answer == "\n":
            continue
        else:
            unique_answers.add(answer)
    yes_sum += len(unique_answers)

print(yes_sum)

# Part 2


ait = 0

for group in data:
    list_of_sets = []

    for line in group.split("\n"):
        line_answers = set()

        for answer in line:
            line_answers.add(answer)
        list_of_sets.append(line_answers)
    intersect = None

    for answer_set in list_of_sets:
        if intersect == None:
            intersect = answer_set
        else:
            intersect = intersect.intersection(answer_set)
    ait += len(intersect)


print(ait)

