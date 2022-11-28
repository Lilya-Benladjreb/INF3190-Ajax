from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/query", methods=["GET"])
def query():
    query = request.args.get("q")
    fichier = open("cours.txt", "r")
    lignes = fichier.readlines()
    coursTrouves = []
    for ligne in lignes:
        if query in ligne.lower():
            coursTrouves.append(ligne)
    return render_template("listesCours.html", liste=coursTrouves)