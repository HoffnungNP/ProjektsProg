from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/page2")
def test():
    return render_template("page2.html")

@app.route("/cat1")
def cat1():
    return render_template("cat1.html")

@app.route("/panemtdzivnieku")
def panemt():
    return render_template("panemtdzivnieku.html")

@app.route("/pierakstisanas")
def pierakst():
    return render_template("pierakstisanas.html")

@app.route("/ziedosana")
def zied():
    return render_template("ziedosana.html")

@app.route("/klutpardalibnieku")
def partn():
    return render_template("klutparpartneri.html")

if __name__ == "__main__":
    app.run(debug = True)
