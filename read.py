# /usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime

with open('E:/test.txt','w' ) as f:
    f.write('今天是')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('E:/test.txt','r') as f:
    s = f.read()
    print('open for read')
    print(s)

with open('E:/test.txt','rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)