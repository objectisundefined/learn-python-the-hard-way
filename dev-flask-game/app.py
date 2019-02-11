from flask import Flask, session, redirect, url_for, escape, request, render_template
import game.planisphere as planisphere

app = Flask(__name__)

@app.route("/")
def index():
  # this is used to "setup" the session with starting values
  session['room_name'] = planisphere.START
  return redirect(url_for("game"))


@app.route("/game", methods=['POST', 'GET'])
def game():
  room_name = session.get('room_name')

  if request.method == "GET":
    if room_name:
      room = planisphere.load_room(room_name)
      return render_template("show_room.html", room=room)
    else:
      # why is there here? do you need it?
      return render_template("you_died.html")

  else:
    action = request.form.get('action')

    if room_name and action:
      room = planisphere.load_room(room_name)
      next_room = room.go(action)

      if not next_room:
        session['room_name'] = planisphere.name_room(room)
      else:
        session['room_name'] = planisphere.name_room(next_room)

    return redirect(url_for("game"))

# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# this should be put at bottom
if __name__ == "__main__":
  app.run()


# I’m using sessions in my game, and I can’t test it with nosetests. Read the Flask Testing Documentation about “Other Testing Tricks” (http://flask.pocoo.org/docs/0.12/testing/#othertesting-tricks) for information on creating fake sessions inside your tests.

# I get an ImportError. It could be one or more of these: wrong directory, wrong Python version,
# PYTHONPATH not set, no __init__.py file, and/or spelling mistake in import.