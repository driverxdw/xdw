#!/usr/bin/python
#encoding=utf-8
import time
import pickle
choice=0
money=15000     #信用卡额度
shopping_list=[] #消费列表
doc='ATM.txt'
def flush_and_choice():
  global money
  f=open(doc,'a+')
  print '\033[1;32m-----------------------------------------'
  print '\033[1;32m1.存款     2.提现'
  print '\033[1;32m3.消费     4.转账(未实现)'
  print '\033[1;32m5.冻结     6.退出'
  print '\033[1;32m7.解锁(逻辑问题，已移出)'
  print '\033[1;32m-----------------------------------------'
  lines=f.readlines()
  if len(lines)>0:
    money=int(lines[-1].split('\t')[2])
  global choice
  choice=(raw_input('please input the num you want to :').strip())
  f.close()
def deposit():
  f=file(doc,'a')
  money_deposit=int(raw_input('please input the money you want to despoit :'))
  print 'Dealing...'
  time.sleep(2)
  print "ok,there is %d letf" % int(money+money_deposit)
  f.write(time.strftime('%Y-%m-%d',time.localtime(time.time()))+'\t')
  f.write('\033[1;36m'+str(money_deposit)+'\t')
  f.write(str(money+money_deposit)+'\n')
  f.close()
def drawing():
  f=file(doc,'a')
  money_drawing=int(raw_input('please input the money you want to drawing :'))
  print('please wait a minute~')
  time.sleep(2)
  print('sucessfully drawinged!')
  f.write(time.strftime('%Y-%m-%d',time.localtime(time.time()))+'\t')
  f.write('\033[1;31m'+'-'+str(money_drawing)+'\t')
  f.write(str(money-money_drawing)+'\n')
def authentic():
  f=file('authentic_usr.txt','rb')
  for result in f.readlines():
    if 'locked' in result:
      print '\033[1;31mThe account has been locked~please unlick!'
      exit()
  for num in range (0,3):
    account_name=raw_input('\033[1;35mplease input the account_name:')
    account_key=raw_input('please input the account_key:')
    if account_name=='xdw' and account_key=='123':
       print 'Welcome xdw~'
       return
    else :
       print '\033[1;31msorry!the input is not correct!'
  print 'Sorry!The account_name or the account_key is not correct and the account will be locked for 24 hours~'
  f=file('authentic_usr.txt','wb')
  pickle.dump('locked',f,0)
  f.close()
  exit()
def frezz():
  f=open('authentic_usr.txt','wb')
  f.write('locked')
  f.close()
  print 'The account has been locked!~'
  exit()
def contral_center():
  authentic()
  while 1:
    flush_and_choice()
    if choice=='1':
       deposit()
    elif choice=='2':
       drawing()
    elif choice=='5':
       frezz()   
    elif choice=='6':
       return
contral_center()
