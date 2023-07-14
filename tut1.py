from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta  #used to set up max time session can last on

app = Flask(__name__)
app.secret_key = "heytheret"  #secret key to encrypt session data
app.permanent_session_lifetime = timedelta(days=5)  #stores permanent session data for 5 days

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
        session.permanent = True   #turns session into permament session
        user = request.form["nm"] #we recieve what is in the input box named "nm"
        session["user"] = user  #session uses dictinary key, setting the user key in the session to the user object 
        flash("Login successful.")
        return redirect(url_for("user")) #sends to user function with the user's name as a variable
    else: #if there is no name submitted, we are just GETting the webpage
        if "user" in session:
            flash("Already logged in.")
            return redirect(url_for("user")) #if user is already logged in, send to user page
        return render_template("login.html")  #else send to login page

@app.route("/user") #user sent from login method
def user():
    if "user" in session:  #checks if user is logged in first
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in.")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    if "user" in session:  #checks if user is logged in first
        user = session["user"]
        flash(f"You have been logged out, {user}", "info") #sends message to login page for user confirmation only if user was logged in   
    session.pop("user", None) #removes user from the session 
    return redirect(url_for("login"))




if __name__ == "__main__":
    app.run(debug=True)