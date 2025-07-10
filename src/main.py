from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("Email")
        return redirect(url_for('resume_parser', email=email))
    return render_template("login.html")

@app.route("/parser")
def resume_parser():
    email = request.args.get("email")
    greeting = None
    if email:
        try:
            name, domain = email.split("@")
            org = domain.split(".")[0].title()
            first_name = name.split(".")[0].title()
            greeting = f"Hello {first_name} of {org}"
            return render_template("parser.html", greeting=greeting)
        except Exception:
            greeting = None
    else:
        #show an unauthorised page
        return render_template("unauthorised.html")
    