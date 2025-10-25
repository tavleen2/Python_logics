from flask import Flask

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])    #accepts both GET and POST request
def hello_world():
    return "<p> Hello !!</p>"

app.run(port= 8000, debug=True)