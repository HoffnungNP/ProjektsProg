import pandas as pd
from flask import Flask, send_file, redirect, url_for, render_template, request
app = Flask(__name__)
users = {}

data = "zied.csv"
zied_df = pd.read_csv(data)

# Function to save DataFrame as CSV
def save_csv():
    csv_filename = "zied.csv"
    zied_df.to_csv(csv_filename, index=False)  # Save as CSV without index
    return csv_filename

# Route to download CSV
@app.route("/zied.csv")
def download_csv():
    csv_file = save_csv()
    return send_file(csv_file, as_attachment=True)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/page2")
def test():
    return render_template("page2.html")

@app.route("/cat1")
def cat1():
    return render_template("cat1.html")

@app.route("/cat2")
def cat2():
    return render_template("cat2.html")

@app.route("/dog1")
def dog1():
    return render_template("dog1.html")

@app.route("/guineapig")
def guineapig():
    return render_template("guineapig.html")

@app.route("/dog2")
def dog2():
    return render_template("dog2.html")

@app.route("/rabbit")
def rabbit():
    return render_template("rabbit.html")

@app.route("/panemtdzivnieku")
def panemt():
    return render_template("panemtdzivnieku.html")

@app.route("/pierakstisanas")
def pierakst():
    return render_template("pierakstisanas.html")

@app.route("/ziedosana")
def zied():
    return render_template("ziedosana.html")

@app.route("/klutparpartneri", methods=["GET", "POST"])
def partn():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return "Lietotājs ir jau reģistrēts!"
        else:
            users[username] = password
            return "Paldies par piedalīšanos patversmei!"

    return render_template("klutparpartneri.html")

if __name__ == "__main__":
    app.run(debug = True)

