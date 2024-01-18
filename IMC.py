#Calculo do IMC

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#new_height = float(height)
#calc_height = new_height**2
#new_weight = int(weight)
#print(round(new_weight // calc_height))

# OUTRA FORMA:
#bmi = int(weight) / float(height)**2  #ou usar // para arredondar
#print(round(bmi))

bmi = round(int(weight) / float(height)**2)
#print(f"Your BMI is: {bmi}")
if bmi < 18.5:
	print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
	print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
	print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
	print(f"Your BMI is {bmi}, you are obese.")
else:
	print(f"Your BMI is {bmi}, you are clinically obese.")
