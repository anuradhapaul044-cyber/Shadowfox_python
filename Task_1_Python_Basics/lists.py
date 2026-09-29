# Justice League List

justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]

# 1. Number of members
print("\n1. Number of members:", len(justice_league))


# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("\n2. After adding members:")
print(justice_league)


# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("\n3. Wonder Woman as leader:")
print(justice_league)


# 4. Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")

print("\n4. Green Lantern between Aquaman and Flash:")
print(justice_league)


# 5. Replace the list with new members
justice_league = ["Cyborg","Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]

print("\n5. New Justice League:")
print(justice_league)


# 6. Sort alphabetically
justice_league.sort()

print("\n6. Alphabetically sorted:")
print(justice_league)

print("\nNew leader:", justice_league[0])