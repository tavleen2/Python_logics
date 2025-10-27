from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])   
def hello_world():
    print(request.method)
    return render_template("contact.html")
    # return "<p> Hello!!</p>"

app.run(port= 8000, debug=True)