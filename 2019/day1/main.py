import math

modules = [int(module.strip()) for module in open('input.txt').readlines()]


def get_fuel_for_mass(mass):
    return math.floor(mass / 3) - 2


def get_extra_fuel_for_fuel(fuel):
    extra_fuel = math.floor(fuel / 3) - 2
    if extra_fuel < 0:
        return fuel
    return get_extra_fuel_for_fuel(extra_fuel) + fuel


if __name__ == '__main__':
    total_fuel = list(map(get_fuel_for_mass, modules))
    total_extra_fuel = list(map(get_extra_fuel_for_fuel, total_fuel))

    answer_part1 = sum(total_fuel)
    print(f'Answer for part 1: {answer_part1}')

    answer_part2 = sum(total_extra_fuel)
    print(f'Answer for part 2: {answer_part2}')
