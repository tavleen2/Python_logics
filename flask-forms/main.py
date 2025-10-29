from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])   
def hello_world():
    if (request.method == "POST"):
        #handle the form
        with open("file.txt", "w") as f:
            f.write(f"The name is: {request.form['name']} , \n The email is : {request.form['email']}, \n The DOB is : {request.form['dob']}\n")
        return render_template("contact.html")
    else:
        return render_template("contact.html")

app.run(port= 8000, debug=True)