#!/usr/bin/python
#encoding=utf-8
f=file('shop_2.txt')
product=[]
price=[]
for i in f.readlines():
    i=i.split()
    product.append(i[0])
    price.append(i[1])
for i in product:
    print i,price[product.index(i)]
