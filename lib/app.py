import json
import sys
from flask import Flask, render_template

from models.stop import Stop

app = Flask('lib', template_folder="../public/templates", static_folder="../public")

# app.debug = True

STOPS = [
    Stop.create_stop("chicago"),
    Stop.create_stop("ashland"),
    Stop.create_stop("grand_ogden")
]


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api")
def api():
    print "Getting from API"
    for stop in STOPS:
        stop.refresh_leave_times()

    data = [stop.to_dict() for stop in STOPS]

    return json.dumps(data)


if __name__ == "__main__":
    app.run()
