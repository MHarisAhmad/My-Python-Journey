#Swaping first and last elements of the list
list = [10, 20, 30, 40, 50]
list[0], list[-1] = list[-1], list[0]
print(list)

#Age eligibility for Internship
eligible_ages = []
underage_ages = []
ages = [16, 21, 17, 19, 15, 22, 18, 25, 14]
for a in ages:
    if a >=17 and a<=22:
        eligible_ages.append(a)
    elif a < 17:
        underage_ages.append(a)
print(sorted(eligible_ages))
print(sorted(underage_ages))