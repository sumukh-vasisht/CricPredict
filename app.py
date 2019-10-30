from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="POST":
        team1 = request.form['team1']
        team2 = request.form['team2']
        # country = request.form['country']
        global mes
        mes=team1+"."+team2
        message=team1+"."+team2
        return redirect(url_for('predicc',t1=team1,t2=team2))
    return render_template("index.html")

@app.route('/predicc', methods=['GET','POST'])
def predicc():
    return render_template("page2.html")

if __name__ == "__main__":
    app.run(debug=True)