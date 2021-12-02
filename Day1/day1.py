def data(f="input.txt"):
    with open("input.txt", "r") as f:
        measurements = [int(line.strip()) for line in f.readlines()]
    return measurements

def part1(data):
    return sum(1 if data[x] > data[x-1] else 0 for x in range(1, len(data)))



def part2(data):
    return part1(
        [data[x] + data[x-1] + data[x-2] for x in range(len(data)) if x >= 2]
    )

print(f"Part 1: {part1(data())}")
print(f"Part 2: {part2(data())}")
