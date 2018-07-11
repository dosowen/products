year = int(input('please type the year:'))
def is_leap():
	if year % 4 == 0:
		print('it is a leap year')
	else:
		print('it is not a leap year')
is_leap()