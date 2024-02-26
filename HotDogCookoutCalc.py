hotdogs_package = 10
buns_package = 8

print("Hot Dog Cookout Calculator")
print()
print(f"You have {hotdogs_package} hotdogs in 1 package.")
print()
print(f"You have {buns_package} buns in 1 package.")
print()
num_people = int(input("How many people are attending the cookout? : "))
num_hotdog = int(input("How many hot dogs will each person be given? : "))
print()

total_hotdog = num_people * num_hotdog

min_hotdog_package = total_hotdog // hotdogs_package
min_bun_package = total_hotdog // buns_package
hotdogs_left = total_hotdog % hotdogs_package
buns_left = total_hotdog % buns_package

print(f"   You will need {total_hotdog} hot dogs.")
print(f"-You will need a minimum of {min_hotdog_package} packages of hot dogs.")
print(f"-You will need a minimum of {min_bun_package} packages of buns.")
print(f"-You will have {hotdogs_left} hot dogs left over.")
print(f"-You will have {buns_left} buns left over.")