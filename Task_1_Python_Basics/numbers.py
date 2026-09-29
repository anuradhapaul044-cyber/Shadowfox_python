# Program 1
def format_number(number, character):
    return "{}{}".format(number, character)

print(format_number(145, "o"))


# Program 2
radius = 84
pi = 3.14

area = pi * radius * radius
water = area * 1.4

print(int(area))
print(int(water))


# Program 3
distance = 490
time_minutes = 7

time_seconds = time_minutes * 60
speed = distance / time_seconds

print(int(speed))