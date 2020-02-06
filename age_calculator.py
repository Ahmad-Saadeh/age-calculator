from datetime import datetime

def check_birthdate(year, month, day):
	birthdate = datetime(year, month, day)
	today = datetime.now()
	if birthdate > today:
		return False
	else:
		return True

def calculate_age(year, month, day):
	birthdate = datetime(year, month, day)
	today = datetime.now()
	deff = today - birthdate
	ageInDays = deff.days
	age = int(ageInDays/365)
	print("You are {} years old ".format(age))

def main():
	year = int(input("Enter year of birth:"))
	month = int(input("Enter month of birth:"))
	day = int(input("Enter day of birth:"))

	if check_birthdate(year, month, day):
		calculate_age(year, month, day)
	else:
		print("Invalid birthdate!")

if __name__ == '__main__':
	main()
