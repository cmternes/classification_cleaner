import re

def classification_type_check(string):
    return string[0].isalpha()

def convert_string_to_list(string):
    if classification_type_check(string) == True:
        ICPclass_list = re.findall(r'\w+(?:\/)?(?:\w+)?', input)
        return ICPclass_list
    else:
        USclass_list = re.findall(r'\d+(?:\/)?(?:\w+)?(?:\.)?(?:\w+)?', input)
        return USclass_list

def remove_US_dots_letters(list):
    letter_format = re.compile(r'(\d+\/\d+)[a-zA-Z]')
    dot_format = re.compile(r'(\d+\/\d+)\.\w+')
    for i in USclass_list:
        if i == letter_format or dot_format:
            print("format")

input = "435; 435/462; 21/27F 424/164.1; 424/164.100P;"

if classification_type_check(input) == False:
    remove_US_dots_letters(classification_type_check(input))
    


print(convert_string_to_list(input))






