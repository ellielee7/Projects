oddnum = range(1,1000)
for i in oddnum:
    if i%2!=0:
        print i

for count in range(1, 1001, 2):
    print count

for count in range(5,1000001,5):
    print count


a = [1, 2, 5, 10, 255, 3]
sum = 0
for s in range(0,len(a)):
   sum = sum+a[s]
print sum

a = [1, 2, 5, 10, 255, 3]
print (sum(a) / len(a))
