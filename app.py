from flask import Flask, render_template, request
from db import init_db, save_cv

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    #request.method Sjekker hvilken type request som ble sendt.
    if request.method == "POST":
        # request form Henter data brukeren skriver i skjemaet
        navn = request.form["navn"]
        epost = request.form["epost"]
        telefon = request.form["telefon"]
        utdanning = request.form["utdanning"]
        erfaring = request.form["erfaring"]
        ferdigheter = request.form["ferdigheter"]

        # INPUT VALIDERING
        if not navn or not epost:
            error = "Navn og e-post må fylles ut"
            #render_template Viser HTML-filen.
            return render_template("index.html", error=error)
        # error er Variabel jeg lagde for å lagre feilmeldinger

        if len(telefon) < 8:
            error = "Telefonnummer må være minst 8 tall"
            return render_template("index.html", error=error)

        # Lagre CV i databasen
        save_cv(navn, epost, telefon, utdanning, erfaring, ferdigheter)

        # Vis CV på nettsiden
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