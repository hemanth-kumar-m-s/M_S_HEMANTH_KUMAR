# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
w=float(weight)
h=float(height)
bmi = (w/h**2)
bmi_int=int(bmi)
print(bmi_int)