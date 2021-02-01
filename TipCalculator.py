print("Welcome to tip calculator")

bill_one = input("What was the total bill?: \n")
percentage = input("What % tip would you like to give? 10, 12, or 15? \n")
split = input("How many people to split the bill? \n")

bill_two = float(bill_one)

percentage_tip = int(percentage)

split_people = int(split)

bill_three = (percentage_tip / 100) * bill_two

bill_aftertip = bill_three + bill_two

bill_total = bill_aftertip / split_people

bill_final = (round(bill_total,2))

bill_total = str(bill_final)

print("Each person should pay $" + bill_total)

input("Press any key and enter to close this script: ")