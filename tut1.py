from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content="Testing") #sends list to webpage when template is rendered

#use of a f string to format a string simply
#name is taken from whatever is passed to the function
@app.route("/<name>")
def person(name):
    return f"Hello {name}!"

#if admin tab clicked, or /admin written in the url
#page will be redirected to user function passing Admin! as name
@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST": #if user types a name in the box, we recieve what is POSTED
        user = request.form["nm"] #we recieve what is in the input box named "nm"
        return redirect(url_for("user", usr = user)) #sends to user function with the user's name as a variable
    else: #if there is no name submitted, we are just GETting the webpage
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"




if __name__ == "__main__":
    app.run(debug=True)