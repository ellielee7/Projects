def odd_even(num):
  for num in range(1,num):
      if (num % 2 == 0):
          print "Number is {} This is an even number.".format(num)
      else:
          print "Number is {} This is an odd number.".format(num)
odd_even(2001)

def multiply(arr, num):
    for item in range(0, len(arr)):
        arr[item] *= num
    return arr
number_list = [2,4,10,16]
print multiply(number_list, 5)

def layered_multiples(array):
    print array
    new_array = []
    for x in array:
        val_array =[]
        for x in range(0, x):
            val_array.append(1)
        new_array.append(val_array)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
