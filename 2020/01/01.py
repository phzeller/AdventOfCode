input = []

def calculateSummands(input):
    for indexI, i in enumerate(input):
        for indexJ, j in enumerate(input):
            if i + j == 2020 and indexI != indexJ:
                return (i, j)

def calculateThreeSummands(input):
    for indexI, i in enumerate(input):
        for indexJ, j in enumerate(input):
            for indexK, k in enumerate(input):
                if i + j + k == 2020 and indexI != indexJ != indexK:
                    return i, j, k

def main():
    with open("input") as input_file:
        input = input_file.read().splitlines()

    input = list(map(int, input))

    # PART 1
    summands = calculateSummands(input)
    if len(summands) == 2:
        print("Part 1 Target = {} * {} = {}".format(summands[0], summands[1], summands[0] * summands[1]))
    else:
        print("Part1: no solution found")

    # PART 2
    threeSummands = calculateThreeSummands(input)
    if len(threeSummands) == 3:
        print("Part 2 Target = {} * {} * {} = {}".format(threeSummands[0], threeSummands[1], threeSummands[2],
                                                         threeSummands[0] * threeSummands[1] * threeSummands[2]))
    else:
       print("Part1: no solution found")

if __name__ == "__main__":
    main()
