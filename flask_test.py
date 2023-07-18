#Package import
from flask import Flask, render_template, send_File, make_response, url_for, Response, redirect, request

#Initialize app
app = Flask(__name__)

#Decorator for Homepage
@app.route("/")
def index():
    return render_template('index.html', PageTitle = "landing page")

if __name__ == '__main__':
    app.run(debug = True)
