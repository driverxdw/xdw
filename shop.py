#!/usr/bin/python
#encoding=utf-8
product=['orange','apple','banana','peach','purple']
price=[12,10,8,14,20]
bought=[]
for p in product :
    index=product.index(p)
    print p , price[index]
money=int(raw_input('please input your money :'))
while 1:
    choice=raw_input('please input the fruit you want to buy :').strip()
    if money<min(price):
        print 'you can\'t afford anything,the following is what you bought :'
	print bought
	break
    elif money<price[product.index(choice)]:
        print 'you can\'t afford this price,please choose another~'
    else :
        print 'you buy the %s' % choice
	bought.append(choice)
	money=money-price[product.index(choice)]
	print 'you have $%d now !' % money

