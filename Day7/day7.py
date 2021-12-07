def data(input_file="input.txt"):
    with open(input_file) as f:
        return [int(x) for x in f.read().split(",")]


def part1(data):
    total_costs = {}
    positions = range(max(data) + 1)
    for pos in positions:
        total_cost = sum(abs(crab - pos) for crab in data)
        total_costs[pos] = total_cost

    min_cost = {k: v for k, v in sorted(total_costs.items(), key=lambda item: item[1])}
    print(f"Cheapest postition: {list(min_cost)[0]}")
    print(f"Total cost: {min_cost[list(min_cost)[0]]}")


def part2(data):
    total_costs = {}
    positions = range(max(data) + 1)
    for pos in positions:
        total_cost = sum(sum(range(abs(crab - pos) + 1)) for crab in data)
        total_costs[pos] = total_cost

    min_cost = {k: v for k, v in sorted(total_costs.items(), key=lambda item: item[1])}
    print(f"Cheapest postition: {list(min_cost)[0]}")
    print(f"Total cost: {min_cost[list(min_cost)[0]]}")


part1(data())
part2(data())
