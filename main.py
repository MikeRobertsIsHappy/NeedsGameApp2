from flask import Flask, redirect, url_for, render_template, request, session
import logging
import jackalbot as jb
from datetime import datetime, timedelta
from pathlib import Path
import pathlib
import os.path



app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

# first step is to get the users name.  This initiates the session
@app.route("/", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form["nm"]
		session["user"] = user
		session['game_state_data'] = 'starting new session'
		return redirect(url_for("game"))
	else:
		if "user" in session:
			return redirect(url_for("game"))

		return render_template("login.html")

@app.route("/game")
def game():
	if "user" in session:
		user = session["user"]
		return render_template("index.html")
	else:
		return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response, new_game_state_data  = jb.jackalbot_response(user_input, session)
    session['game_state_data'] = new_game_state_data
    return bot_response

@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("login"))


if __name__ == "__main__":
	app.run(host='127.0.0.1', port=8080)  #, debug=True, threaded=True  