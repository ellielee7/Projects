str = "It's thanksgiving day. It's my birthday,too!"
print str.replace("day", "month")
list = [2, 54, -2, 7, 12, 98]
max(list)
min(list)
print "Max value element : ", max(list)
print "Min value element : ", min(list)
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print (x[-1])
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print (x)
print len(x)
value = len(x)/2
print value
list1 = x[:value]
print list1
list2 = x[value:]
print list2
list2.insert(0,list1)
print list2
