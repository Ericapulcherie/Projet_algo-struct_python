from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def read():
    username = request.form['username']
    return render_template("index.html", name=username)

@app.route("/tatii")
def tatiana():
    return render_template("tatiana.html")

@app.route("/tatii", methods=['POST'])
def tatiana_result():
    number = int(request.form['n'])
    times = int(request.form['k'])
    
    for i in range (1, times+1):
        if number%10 == 0:
            number = number/10
        else:
            number = number-1
    
    return render_template("tatiana.html", result=number)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Exo1")
def Exo1():
    return render_template("Exo1.html")

def facto(n):
    if n == 0:
        return 1
    else:
        return n*facto(n-1)

@app.route("/Exo1", methods=['POST'])
def result():
    nbre = int(request.form['nombre'])

    fact = facto(nbre)
    result = str(fact)
    chaine = "Le resultat est "+result

    return render_template("Exo1.html", resultat=chaine)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")  