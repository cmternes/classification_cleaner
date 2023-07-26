#from flask import Flask
import re

#app = Flask(__name__)

#@app.route ("/")
def class_format(string):
    if string[0].isalpha() == True: #Determines the classification system by checking if first character is a letter (IPC/CPC) or number (US)
        class_list = re.findall(r'\w+\/?\w+', input) #pattern matches IPC/CPC format
        return class_list
    else:
        USclass_list = re.findall(r'\d+\/?\d+\.?\w+', input)
        US_pattern_decimal = re.compile(r'(\d+)\/(\d+)(?:[a-zA-z]+|\.)(?:\w+)?')
        class_list = [re.sub(US_pattern_decimal, r'\1/\2*', x) for x in USclass_list] #this removes any decimals and/or trailing letters 
        return class_list                                                             #and replaces with an asterisk

#input = "435; 435/462; 21/27F 424/164.1; 424/164.100P;"
input = "424/93.21; 435/462 424/164.1; 424/164.100P; 424/164.100S; 424/94.63; 424/94.630P; 435/188.5; 435/188.500S; 435/212; 435/22; 435/220; 435/220S; 435/252.33; 435/252.330S; 435/320.1; 435/320.100S; 435/4; 435/69.1; 435/69.2; 435/69.3; 435/69.300S; 435/692; 435/7.37; 435/7.370P; 435/737; 514/192; 514/192S; 514/200; 514/200S; 514/210.09; 514/210.090S; 530/300; 530/350; 530/388.4; 530/388.400S; 536/23.1; 536/23.2; 536/23.200S; 536/231 424/94.2; 424/94.200S; 424/94.61; 424/94.610P; 424/94.63; 424/94.630S; 435/200; 435/200S; 435/226; 435/226P"

list = class_format(input)
unique_list = []
[unique_list.append(x) for x in list if x not in unique_list]

print(*unique_list)









