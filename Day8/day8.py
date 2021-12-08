digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


def get_output(input_file="input.txt"):
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            lines.append(line.strip().split("|")[1])
    return lines


def get_input_and_output(input_file="input_short.txt"):
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            left, right = line.strip().split("|")
            left = [chunk for chunk in left.split(" ") if chunk]
            right = [chunk for chunk in right.split(" ") if chunk]
            lines.append([left, right])
    return lines


def part1(data):
    counts = {
        1: 0,
        4: 0,
        7: 0,
        8: 0,
    }
    all_digits = []
    for line in data:
        all_digits.extend(line.strip().split(" "))

    for count in counts:
        for digit in all_digits:
            if len(digit) == len(digits[count]):
                counts[count] += 1
    print(f"Part1: {counts[1] + counts[4] + counts[7] + counts[8]}")


def match_segments(default, new):
    correct_segments = list(default)
    new_segments = list(new)
    return {char: new_segments.pop(0) for char in correct_segments}


def part2(data):
    known_digits = [1, 4, 7, 8]
    keys = {"a", "b", "c", "d", "e", "f", "g"}
    new_mapping = {}

    for line in data:
        signals, output = line
        for digit in known_digits:
            default_value = digits[digit]
            matching_segments = [seg for seg in signals if len(seg) == len(digits[digit])][0]
            decoded_mapping = match_segments(default_value, matching_segments)
            print(f"{digit}: {default_value} -> {''.join(decoded_mapping.values())}")

            for key in keys:
                if (
                    key not in new_mapping.keys()
                    and key in decoded_mapping.keys()
                    and decoded_mapping[key] not in new_mapping.values()
                ):
                    print(f"Updated mapping: {key} -> {decoded_mapping[key]}")
                    new_mapping[key] = decoded_mapping[key]

            # One value missing, map it from default mapping
            if len(new_mapping) == len(keys) - 1:
                missing_key = [key for key in keys if key not in new_mapping.keys()][0]
                missing_value = [key for key in keys if key not in new_mapping.values()][0]
                new_mapping[missing_key] = missing_value

            print(f"New mapping: {dict(sorted(new_mapping.items()))}")

        complete_output = []
        for number in output:
            chars = list(number)
            decoded = []
            for char in chars:
                for k,v in new_mapping.items():
                    if v == char:
                        decoded.append(k)
            complete_output.append("".join(sorted(decoded)))
        print(f"Decoded output: {complete_output}")
        complete_number = []
        for seq in complete_output:
            for k,v in digits.items():
                if v == seq:
                    complete_number.append(str(k))
        print(f"Complete number: {''.join(complete_number)}")

        break # Only one line for now


part1(get_output())
part2(get_input_and_output())
