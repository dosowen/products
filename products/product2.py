products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name,price])
print(products)

for p in products:
	print(p[0],'要',p[1],'塊錢')
with open ('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p2 in products:
		f.write(p2[0] + ',' + p2[1] + '\n')

k=[]
with open ('products.csv', 'r',encoding='big5') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name,price = line.strip().split(',')
		k.append([name, price])
print(k)
