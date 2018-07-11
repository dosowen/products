number = input('please type the number you are going to average (like 1,2,3):')
number2 = [int(x) for x in number.split(',')]
def sum_of_list(numbers):
	return sum(numbers)/len(numbers)
print(sum_of_list(number2))