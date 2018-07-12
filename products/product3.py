
def input_data():
	products = []
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append([name,price])
	print(products)
	return products

def print_product(products):
	for p in products:
		print(p[0],'要',p[1],'塊錢')

def write_file(filename):
	with open (filename, 'w') as f:
		f.write('商品,價格\n')
		for p2 in products:
			f.write(p2[0] + ',' + p2[1] + '\n')


def read_file(filename,products):
	import os
	if os.path.isfile(filename):
		print('yeah ,I found it!!!')
		with open (filename, 'r',encoding='big5') as f:
			for line in f:
				if '商品,價格' in line:
					continue
				name,price = line.strip().split(',')
				products.append([name, price])
		print(products)
	else:
		print('I did not found it!!!!!')

products=input_data()
print_product(products)
write_file('products.csv')
read_file('products.csv',products)