from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

teams = ["",""]

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="POST":
        global team1, team2
        teams[0] = request.form['team1']
        teams[1] = request.form['team2']
        # country = request.form['country']
        return redirect(url_for('predicc'))
    return render_template("index.html")

@app.route('/predicc', methods=['GET','POST'])
def predicc():
    return render_template("predicc.html", teams = teams)

if __name__ == "__main__":
    app.run(debug=True)