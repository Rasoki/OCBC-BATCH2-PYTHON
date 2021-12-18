# name = "Hacktiv8"
# Age= 54
# has_laptops = True
# print(name, Age, has_laptops)

# age = 1
# Age = 2
# aGe = 3
# AGE = 4
# a_g_e = 5
# _age = 6
# age_ = 7
# _AGE_ = 8

# print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)

# a = 4
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)

# a = 10

# b = 20
# print(a == b)
# print(a != b)
# print(a <= b)
# print(a >= b)

#dictionary
MLB_team = {
    'Colorado' : 'Rockies',
    'Boston' : 'Red Sox',
    'Minnesota' : 'Twins',
    'Milwaukee' : 'Brewers',
    'Seattle' : 'Mariners'
}

print(MLB_team)
print(MLB_team['Milwaukee'])
print(f"MLB Team of Milwaukee {MLB_team['Milwaukee']}")

MLB_team['Kansas City'] = 'Royals'
print(f"MLB Team of Kansas City {MLB_team['Kansas City']}")

print(MLB_team)

for key, value in MLB_team.items():
    print(key, value)


