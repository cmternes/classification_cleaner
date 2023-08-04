from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('cleaner.html')

@app.route ('/', methods=['POST'])
def class_format():
    if request.method == 'POST':
        string = request.form['textbox']
        if string[0].isalpha() == True: #Determines the classification system by checking if first character is a letter (IPC/CPC) or number (US)
            class_list = re.findall(r'\w+\/?\w+', string) #pattern matches IPC/CPC format
            #return class_list
        else:
            USclass_list = re.findall(r'\d+\/?\d+\.?\w+', string)
            US_pattern_decimal = re.compile(r'(\d+)\/(\d+)(?:[a-zA-z]+|\.)(?:\w+)?')
            class_list = [re.sub(US_pattern_decimal, r'\1/\2*', x) for x in USclass_list] #this removes any decimals and/or trailing letters and replaces with an asterisk
            #return class_list
        unique_list = []
        [unique_list.append(x) for x in class_list if x not in unique_list]
        return '\n'.join(unique_list)

if __name__ == "__main__":
    app.run(debug=True)











