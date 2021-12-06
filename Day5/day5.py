def data(input_file="input.txt"):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
        processed_lines = []
        for line in lines:
            start_finish = line.split(" -> ")
            start = [int(x) for x in start_finish[0].split(",")]
            finish = [int(y) for y in start_finish[1].split(",")]
            processed_lines.append((start, finish))
    return processed_lines


def h_and_v_lines(data):
    valid_lines = []
    for line in data:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            valid_lines.append(line)

    return valid_lines


def get_max_size(data):
    x_values = []
    y_values = []
    for line in data:
        for point in line:
            x_values.append(point[0])
            y_values.append(point[1])
    return max(x_values), max(y_values)


def part1(data):
    valid_lines = h_and_v_lines(data)
    max_x, max_y = get_max_size(valid_lines)
    grid = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]
    for line in valid_lines:
        x_values = sorted([line[0][0], line[1][0]])
        y_values = sorted([line[0][1], line[1][1]])
        for x in range(x_values[0], x_values[1] + 1):
            for y in range(y_values[0], y_values[1] + 1):
                grid[y][x] += 1

    flat_grid = [item for sublist in grid for item in sublist]
    intersections = len([item for item in flat_grid if item >= 2])

    print(f"Part 1: {intersections}")


def part2(data):
    max_x, max_y = get_max_size(data)
    grid = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]
    for line in data:
        x_values = [line[0][0], line[1][0]]
        y_values = [line[0][1], line[1][1]]

        if x_values[0] == x_values[1] or y_values[0] == y_values[1]:
            x_values = sorted([line[0][0], line[1][0]])
            y_values = sorted([line[0][1], line[1][1]])
            for x in range(x_values[0], x_values[1] + 1):
                for y in range(y_values[0], y_values[1] + 1):
                    grid[y][x] += 1
        else:
            step_x = 1 if x_values[0] < x_values[1] else -1
            step_y = 1 if y_values[0] < y_values[1] else -1

            steps = abs(x_values[0] - x_values[1]) + 1
            x_start = x_values[0]
            y_start = y_values[0]
            for _ in range(steps):
                grid[y_start][x_start] += 1
                x_start += step_x
                y_start += step_y
                steps -= 1


    flat_grid = [item for sublist in grid for item in sublist]
    intersections = len([item for item in flat_grid if item >= 2])

    print(f"Part 2: {intersections}")


part1(data())
part2(data())
