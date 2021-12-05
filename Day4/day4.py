def numbers(data="input.txt"):
    with open(data) as f:
        return [int(number) for number in f.readline().strip().split(",")]


def boards(data="input.txt"):
    with open(data) as f:
        lines = [line.strip() for line in f.readlines()[2:]]
        row_count = 0
        boards = []
        board = []
        for line in lines:
            if line == "":
                continue

            line = line.replace("  ", " ")
            numbers = [[int(number), False] for number in line.split(" ") if number != ""]
            board.append(numbers)
            row_count += 1
            if row_count == 5:
                boards.append(board)
                board = []
                row_count = 0

        return boards


def process_board(board, match):
    for row in board:
        for number in row:
            if number[0] == match:
                number[1] = True

    return board


def is_winning_board(board):
    rows = [row for row in board]
    for row in rows:
        if all(number[1] for number in row):
            return True

    columns = [column for column in zip(*board)]
    for column in columns:
        if all(number[1] for number in column):
            return True
    return False

def process_score(board, match):
    numbers = []
    for row in board:
        for number in row:
            if not number[1]:
                numbers.append(number[0])
    return sum(numbers) * match


def part1():
    boards_data = boards()
    for number in numbers():
        have_a_winner = False
        for idx, board in enumerate(boards_data):
            board = process_board(board, number)
            if is_winning_board(board):
                print(f"Winning board index: {idx}")
                print(f"Winning board: {board}")
                print(f"Winning board score: {process_score(board, number)}")
                have_a_winner = True
                break
        if have_a_winner:
            break

def part2():
    winning_board_indeces = []
    boards_data = boards()
    for number in numbers():
        for idx, board in enumerate(boards_data):
            if idx in [idx[0] for idx in winning_board_indeces]:
                continue
            boards_data[idx] = process_board(board, number)
            if is_winning_board(boards_data[idx]):
                winning_board_indeces.append((idx, process_score(boards_data[idx], number)))

    print(f"Total winning boards: {len(winning_board_indeces)}")
    print(f"Winniing boards: {winning_board_indeces}")
    print(f"Last winning board index: {winning_board_indeces[-1][0]}")
    print(f"Last winning board: {boards_data[winning_board_indeces[-1][0]]}")
    print(f"Last winning board score: {winning_board_indeces[-1][1]}")

part1()
part2()
