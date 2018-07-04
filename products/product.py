products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	p = []
	price = input('請輸入商品價格: ')
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

