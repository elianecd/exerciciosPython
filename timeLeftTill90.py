#Calculate the time left if lives till 90

age = input("What is your current age? ")

age_left = 90 - int(age)
months = age_left * 12
weeks = age_left * 52
days = age_left * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")