#!/usr/bin/env python
#encoding=utf-8
import time
for i in range (1,100) :
    try:
      print i
      time.sleep(1)
    except KeyboardInterrupt: 
      print 'crtl+C has been used , but please don\'t interupt me!'
      continue
