def get_map():
    with open("data") as file:
        data = file.read()
    return data


def get_tree_hits(slope_map, slope):
    slope_y = slope[1]
    slope_x = slope[0]
    x = 0
    y = 0
    trees = 0
    while y < len(slope_map)-1:
        if slope_map[y][x] == "#":
            trees += 1
        x = (slope_x + x) % len(slope_map[1])
        y += slope_y
    return trees


def print_outcome(total, total_list):
    print('''
    Slope (1, 1) = {}
    Slope (3, 1) = {}
    Slope (5, 1) = {}
    Slope (7, 1) = {}
    Slope (1, 2) = {}
    All Slopes   = {}
    '''.format(total_list[0], total_list[1], total_list[2], total_list[3],
               total_list[4], total))


def parse_slopes(slopes, slope_map):
    total_trees = 0
    totals = []
    for slope in slopes:
        trees = get_tree_hits(slope_map, slope)
        if not total_trees:
            total_trees += trees
        else:
            total_trees *= trees
        totals.append(trees)
    return (totals, total_trees)


def main():

    slope_map = get_map().split("\n")
    total_trees = 0
    totals = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    totals, total_trees = parse_slopes(slopes, slope_map)
    print_outcome(total_trees, totals)        


main()
