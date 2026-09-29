import random

# 1. Roll a six-sided die 20 times

six_count = 0
one_count = 0
two_sixes = 0
previous_roll = 0

for i in range(20):
    roll = random.randint(1, 6)
    print("Roll:", roll)

    if roll == 6:
        six_count += 1

    if roll == 1:
        one_count += 1

    if roll == 6 and previous_roll == 6:
        two_sixes += 1

    previous_roll = roll

print("Number of times 6 was rolled:", six_count)
print("Number of times 1 was rolled:", one_count)
print("Number of times two 6s came in a row:", two_sixes)


# 2. Jumping Jacks Workout

completed = 0

for i in range(10):
    completed += 10
    remaining = 100 - completed

    print("You completed", completed, "jumping jacks.")

    if completed == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()

        if skip == "yes" or skip == "y":
            print("You completed a total of", completed, "jumping jacks.")
            break
        else:
            print(remaining, "jumping jacks remaining.")
    else:
        print(remaining, "jumping jacks remaining.")