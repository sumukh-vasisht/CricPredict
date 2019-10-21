from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="POST":
        team1 = request.form['team1']
        team2 = request.form['team2']
        country = request.form['country']
        return team1+team2+country
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)