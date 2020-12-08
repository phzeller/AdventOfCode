input = []

def calculateSummands(input):
    for indexI, i in enumerate(input):
        for indexJ, j in enumerate(input):
            if i + j == 2020 and indexI != indexJ:
                return (i, j)

def main():
    with open("input") as input_file:
        input = input_file.read().splitlines()

    input = list(map(int, input))
    summands = calculateSummands(input)
    print("Target = {} * {} = {}".format(summands[0], summands[1], summands[0] * summands[1]))




if __name__ == "__main__":
    main()
