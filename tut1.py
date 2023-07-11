from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html", content=["tim","joe","bill"])

#use of a f string to format a string simply
#name is taken from whatever is passed to the function
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

#if admin tab clicked, or /admin written in the url
#page will be redirected to user function passing Admin! as name
@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()