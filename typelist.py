l = ['magical unicorns',19,'hello',98.98,'world']

def newlist(list):
    new_str = ""
    sum = 0
    is_str = False
    is_num = False
    for item in list:
        if type(item) == str:
            new_str += item
            is_str = True
        else:
            sum += item
            is_num = True
    if is_str == True and is_num == False:
        print "this is the new string", new_str
        print "this list has only string values"
    elif is_num == True and is_str == False:
        print "this list has only integers"
        print "this is the new sum", sum
    else:
        print "this is a mixed list"
        print "this is the new sum", sum
        print "this is the new string", new_str

newlist(l)
