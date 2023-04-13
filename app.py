from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


# Dashboard
@app.route("/")
def dashboard():
  return render_template("dashboard.html", now=datetime.utcnow())


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
