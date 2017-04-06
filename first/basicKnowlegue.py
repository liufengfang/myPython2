# -*- coding: utf-8 -*-

a = 2
if a == 3 or a == 2:
    print a
elif a < 99:
    print a - 5
else:
    print "ss:", -a - 9

print "这是中文"

# 格式化字符串和占位符
print '你好，%s,你卡内的余额为%d' % ('刘芳芳', 100000)

# 测试list
mylist = ['liu', 234, ['l', 'i', 'u'], True]
if not mylist[len(mylist) - 1]:
    print 'last word'
else:
    mylist.pop(1)
    print mylist

# 条件判断和循环
sum = 0
for i in range(101):
    sum += i
print 'sum=', sum


