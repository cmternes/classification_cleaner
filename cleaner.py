import re

p = re.compile('\w+\/?(\w+)?(\.)?(\w+)?')

x = input("Enter classifications: ")

p.match(x)



