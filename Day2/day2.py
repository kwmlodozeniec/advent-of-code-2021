def data(f="input.txt"):
    with open('input.txt', 'r') as f:
        data = [line.strip().split(" ") for line in f.readlines()]
    return data

def part1(data):
    h_pos = 0
    depth = 0

    for movement in data:
        if movement[0] == "forward":
            h_pos += int(movement[1])
        elif movement[0] == "down":
            depth += int(movement[1])
        elif movement[0] == "up":
            depth -= int(movement[1])

    return h_pos * depth

def part2(data):
    h_pos = 0
    depth = 0
    aim = 0

    for movement in data:
        if movement[0] == "forward":
            h_pos += int(movement[1])
            depth += aim * int(movement[1])
        elif movement[0] == "down":
            aim += int(movement[1])
        elif movement[0] == "up":
            aim -= int(movement[1])

    return h_pos * depth

print(f"Part 1: {part1(data())}")
print(f"Part 2: {part2(data())}")
