from collections import Counter


def data(input_file="input.txt"):
    grid = []
    with open(input_file) as f:
        for line in f.readlines():
            line = list(line.strip())
            line = [int(number) for number in line]
            grid.append(line)
    return grid


def check_is_lowest(point: tuple, grid: list, rows: int, columns: int):
    x, y = point
    target_point_value = grid[x][y]
    if x == 0 and y == 0:
        deltas = [(0, 1), (1, 0)]
    elif x == 0 and y == columns - 1:
        deltas = [(0, -1), (1, 0)]
    elif x == rows - 1 and y == columns - 1:
        deltas = [(-1, 0), (0, -1)]
    elif x == rows - 1 and y == 0:
        deltas = [(-1, 0), (0, 1)]
    elif x == 0 and y > 0 and y < columns - 1:
        deltas = [(0, 1), (1, 0), (0, -1)]
    elif x > 0 and x < rows - 1 and y == columns - 1:
        deltas = [(-1, 0), (0, -1), (1, 0)]
    elif x == rows - 1 and y > 0 and y < columns - 1:
        deltas = [(0, 1), (-1, 0), (0, -1)]
    elif x > 0 and x < rows - 1 and y == 0:
        deltas = [(1, 0), (0, 1), (-1, 0)]
    else:
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    point_values = []
    for delta in deltas:
        x_delta, y_delta = delta
        print(f"Checking ({x + x_delta},{y + y_delta}) [x: {x}, y: {y}]")
        point_values.append(grid[x + x_delta][y + y_delta])
    point_values.append(target_point_value)

    if min(point_values) == target_point_value and point_values.count(target_point_value) == 1:
        return True

    return False


def part1(data):
    rows = len(data)
    columns = len(data[0])
    print(f"Rows: {rows}, Columns: {columns}")

    lowest_coordinates = []
    for row_idx, row in enumerate(data):
        for column_idx, number in enumerate(row):
            if check_is_lowest((row_idx, column_idx), data, rows, columns):
                lowest_coordinates.append((row_idx, column_idx))

    numbers = []
    for point in lowest_coordinates:
        print(f"{point}: {data[point[0]][point[1]]}")
        numbers.append(data[point[0]][point[1]])

    print(f"Low point count: {len(lowest_coordinates)}, Risk level: {sum(num + 1 for num in numbers)}")
    counts = Counter(numbers)
    print(f"Counts: {counts}")


part1(data())
