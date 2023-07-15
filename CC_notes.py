
#Notes & Tips for Classification Cleaner


###Split a string by semicolon in Python

my_str = 'one;two;three;four'

my_list = my_str.split(';')

print(my_list)	#['one', 'two', 'three', 'four']


### filter() function to remove any empty strings from the list

my_str = ';one;two;three;four;' #leading and trailing semicolons yield empty (leading/trailing) strings

my_list = list(filter(None, my_str.split(';')))

print(my_list) #['one', 'two', 'three', 'four']







