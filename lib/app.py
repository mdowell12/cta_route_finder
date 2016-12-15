from flask import Flask, render_template

app = Flask(__name__, template_folder="../public/templates", static_folder="../public")

from eta import train
from api import cta


app.debug = True


@app.route("/")
def index():
    tree = cta.get_train_etas("blue", "chicago")
    etas = [train.TrainETA(e) for e in tree.findall('eta')]

    # return ",".join(map(str, [e.eta_from_request_time for e in etas]))
    return render_template('index.html', etas=etas)


if __name__ == "__main__":
    app.run()
