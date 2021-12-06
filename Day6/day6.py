
from typing import Counter


def data(input_file="input.txt"):
    with open(input_file, "r") as f:
        return [int(age) for age in f.readline().strip().split(",")]

def simulate(data, days):
    all_fish = {age:0 for age in range(9)}
    all_fish.update(Counter(data))

    for _ in range(days):
        fish_babies = all_fish[0]
        all_fish = {age-1:value for age, value in all_fish.items() if age > 0}
        all_fish[6] += fish_babies
        all_fish[8] = fish_babies

    print(f"After {days} days, there are {sum(all_fish.values())} fish.")

simulate(data(), 80)
simulate(data(), 256)
