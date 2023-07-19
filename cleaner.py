import re

#Determines the classification system by checking if first character is a letter (IPC/CPC) or number (US)
def classification_type_check(string):
    return string[0].isalpha()

#Generates a list of classifications based on regex matching
def convert_string_to_list(string):
    if classification_type_check(string) == True:
        class_list = re.findall(r'\w+\/?\w+', input) #pattern matches IPC/CPC format
        return class_list
    else:
        USclass_list = re.findall(r'\d+\/?\d+\.?\w+', input)
        US_pattern_decimal = re.compile(r'(\d+)\/(\d+)(?:\w+|\.)(?:\w+)?')
        class_list = [re.sub(US_pattern_decimal, r'\1/\2*', x) for x in USclass_list] #this removes any decimals and/or trailing letters 
        return class_list                                                             #and replaces with an asterisk
        
        

#def remove_US_dots_letters(list):
    #letter_format = re.compile(r'(\d+\/\d+)[a-zA-Z]')
    #dot_format = re.compile(r'(\d+\/\d+)\.\w+')
    #for i in USclass_list:
        #if i == letter_format or dot_format:
            #print("format")

US_pattern = re.compile(r'(\d+)(?:\/)?(\w+)?\.(\w+)?')


input = "435; 435/462; 21/27F 424/164.1; 424/164.100P;"
#input = "A61K; C07K19/00; C12N15/28; C12N15/28"

#if classification_type_check(input) == False:
    #remove_US_dots_letters(classification_type_check(input))
    
#class_list = convert_string_to_list(input))

print(convert_string_to_list(input))






