from flask import Flask, request, render_template
from package import fetch

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        ticker = request.form["ticker"]
        info = fetch.company_info(ticker)
        return render_template("home.html", info=info)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(port=5000)
