bill=input(" what is your total bill? ")
tip_percentage=input(" what is the tip percentage you would like to give? 10, 12, or 15? ")
total_number_of_people=input(" how many people to split the bill? ")
b=int(bill)
t=int(tip_percentage)
p=int(total_number_of_people)
tip=t/100
split=b/p
total = tip + split
new_total = round(total,2)
print(f"each person should pay {new_total}")