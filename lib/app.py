import json
import sys
from flask import Flask, render_template

from models.stop import Stop

from filters.filter import pretty_minutes_filter, seconds_to_minutes_filter

app = Flask('lib', template_folder="../public/templates", static_folder="../public")

# app.debug = True

app.jinja_env.filters["seconds_to_minutes"] = seconds_to_minutes_filter
app.jinja_env.filters["pretty_minutes"]     = pretty_minutes_filter


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
    for stop in STOPS:
        stop.refresh_leave_times()

    data = [stop.to_dict() for stop in STOPS]
    return json.dumps(data)


if __name__ == "__main__":
    app.run()
