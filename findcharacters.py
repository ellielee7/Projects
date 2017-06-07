word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []
for word in word_list:
    if char in word:
        new_list.append(word)
        print new_list





# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# new_list = ''
# def find(str, ch):
#     index = 0
#     while index < len(str):
#         if str[index] == ch:
#             return index
#         index = index + 1
#     return -1
#
# print "find(\"apple\", 'l') = ", find("apple", 'l')
# print "find(\"apple\", 'p') = ", find("apple", 'p')
