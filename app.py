from flask import Flask, render_template, request
from db import init_db, save_cv

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]
        telefon = request.form["telefon"]
        utdanning = request.form["utdanning"]
        erfaring = request.form["erfaring"]
        ferdigheter = request.form["ferdigheter"]

    
        save_cv(navn, epost, telefon, utdanning, erfaring, ferdigheter)

        return render_template(
            "index.html",
            navn=navn,
            epost=epost,
            telefon=telefon,
            utdanning=utdanning,
            erfaring=erfaring,
            ferdigheter=ferdigheter
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)