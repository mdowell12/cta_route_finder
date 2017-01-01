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
    for stop in STOPS:
        stop.set_leave_times()

    print {stop.station_name: [(l.eta, l.leave_time, l.route_name) for l in stop.leave_times] for stop in STOPS}
    return render_template('index.html', stops=STOPS)


if __name__ == "__main__":
    app.run()
