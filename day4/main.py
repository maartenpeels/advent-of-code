import re

filename = "passports.txt"
REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid_passports_part_1 = 0
valid_passports_part_2 = 0
passports = []

def to_int(value):
  try:
    return int(value)
  except:
    return None

def check_number(number, from_value, to_value):
  number = to_int(number)
  if number and number >= from_value and number <= to_value:
    return True
  else:
    return False

def match(regex, inp):
  result = re.search(regex, inp)
  if result is not None:
    return True
  else:
    return False

with open(filename) as f:
    current_block = ''
    for line in f:
      if line.strip() == '':
        fields = current_block.strip().split(' ')
        passports.append({field.split(':')[0]: field.split(':')[1] for field in fields})
        current_block = ''
      else:
        current_block += f' {line.strip()}'

for passport in passports:
  valid_keys = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
  if REQUIRED_FIELDS <= passport.keys():
    valid_passports_part_1 += 1
  else:
    continue

  # byr (Birth Year) - four digits; at least 1920 and at most 2002.
  byr = to_int(passport['byr'])
  valid_keys['byr'] = check_number(byr, 1920, 2002)

  # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
  iyr = to_int(passport['iyr'])
  valid_keys['iyr'] = check_number(iyr, 2010, 2020)

  # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
  eyr = to_int(passport['eyr'])
  valid_keys['eyr'] = check_number(eyr, 2020, 2030)

  # hgt (Height) - a number followed by either cm or in:
  #   If cm, the number must be at least 150 and at most 193.
  #   If in, the number must be at least 59 and at most 76.
  hgt = to_int(passport['hgt'][:-2])
  unit = passport['hgt'][-2:]

  if unit == 'cm':
    valid_keys['hgt'] = check_number(hgt, 150, 193)
  elif unit == 'in':
    valid_keys['hgt'] = check_number(hgt, 59, 76)

  # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
  valid_keys['hcl'] = match('^#[a-f0-9]{6}$', passport['hcl'])

  # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
  valid_keys['ecl'] = passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

  # pid (Passport ID) - a nine-digit number, including leading zeroes.
  valid_keys['pid'] = match('^[0-9]{9}$', passport['pid'])

  if all(value == True for value in valid_keys.values()):
    valid_passports_part_2 += 1

print(f'Answer part 1: {valid_passports_part_1}')
print(f'Answer part 2: {valid_passports_part_2}')
