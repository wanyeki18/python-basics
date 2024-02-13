weight = int(input("Enter weight:"))
height = float(input("Enter height:"))
BMI = int(weight/(height*height))
print("Your BMI is", BMI)

if BMI >=30 :
    print("Sorry but you are overweight.")
elif BMI <=29 and BMI >=18:
    print("You are healthy.")
else:
    print("Underweight.")
