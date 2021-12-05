from collections import Counter


def data(f="input.txt"):
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data


def part1(data):
    gamma_rate = []
    epsilon_rate = []

    for idx in range(len(data[0])):
        current_column = [value[idx] for value in data]
        counter = Counter(current_column)
        gamma_rate.append(counter.most_common(1)[0][0])
        epsilon_rate.append(counter.most_common()[-1][0][0])

    gamma_rate = "".join(gamma_rate)
    epsilon_rate = "".join(epsilon_rate)

    print(f"Gamma rate: {gamma_rate} [{int(gamma_rate, 2)}]")
    print(f"Epsilon rate: {epsilon_rate} [{int(epsilon_rate, 2)}]")

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def reduce_to_common(data, idx, common):
    """
    Common term looks for most common value if 0, and least common value if -1.
    """
    if len(data) == 1:
        return data[0]

    current_column = [value[idx] for value in data]
    counts = Counter(current_column).most_common()
    value_to_keep = 0
    if len(counts) == 2 and counts[0][1] == counts[1][1]:
        value_to_keep = str(1 + common)
    else:
        value_to_keep = counts[common][0]
    reduced_data = [value for value in data if value[idx] == value_to_keep]
    return reduce_to_common(reduced_data, idx + 1, common)


def part2(data):
    oxygen_rate = []
    scrubber_rate = []

    oxygen_rate = reduce_to_common(data, 0, 0)
    scrubber_rate = reduce_to_common(data, 0, -1)
    print(f"Oxygen rate: {oxygen_rate} [{int(oxygen_rate, 2)}]")
    print(f"Scrubber rate: {scrubber_rate} [{int(scrubber_rate, 2)}]")

    return int(oxygen_rate, 2) * int(scrubber_rate, 2)


print(f"Part 1: {part1(data())}")
print(f"Part 2: {part2(data())}")
