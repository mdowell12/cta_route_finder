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
    """
    Main accessor of CTA API.

    :return: list of dicts, info about each requested stop and its upcoming arrival times, sorted by how soon you should leave

    TODO: delegate logic to separate function for testing
    """
    for stop in STOPS:
        stop.refresh_leave_times()

    data = [stop.to_dict() for stop in STOPS]

    # Flatten data structure
    data = [_merge_stop_info_with_leave_time_dict(stop, leave_time) for stop in data for leave_time in stop['leave_times']]

    data = filter(lambda x: x['leave_time'] >= 0, data)
    data = sorted(data, key=lambda x: x['leave_time'])

    return json.dumps(data)


def _merge_stop_info_with_leave_time_dict(stop, leave_time):
    leave_time['station_name']  = stop['station_name']
    leave_time['walk_time_min'] = stop['walk_time_min']

    return leave_time


if __name__ == "__main__":
    app.run()
