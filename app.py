from flask import Flask, render_template, redirect, url_for

from forms import HeroInputForm, MatsInputForm
from dexscreener_api import DexscreenerDatabaseManager
from controller import StatsController, MatsController

app = Flask(__name__)
app.secret_key = "ieropajdklsagnfjklghrkjlffjdklasfjkdsa;"


@app.route("/", methods=["GET", "POST"])
def index():
    form = HeroInputForm()

    if form.validate_on_submit():
        controller = StatsController(form)

        return render_template("summon_sheet.html", controller=controller.optimized_summon_odds_list())

    return render_template("index.html")


@app.route("/heroform/", methods=["GET", "POST"])
def hero_form():
    form = HeroInputForm()
    return render_template("hero_form.html", form=form)


@app.route("/matsform/", methods=["GET", "POST"])
def mats_form():
    form = MatsInputForm()

    if form.validate_on_submit():
        mats_price_object = DexscreenerDatabaseManager()

        if mats_price_object.is_update_time():
            mats_price_object.update_database_prices()


        mining_results_controller = MatsController(form, mats_price_object.dexscreener_dfk_mats_dictionary)
        return render_template("mining_results.html", controller=mining_results_controller)



    return render_template("mats_form.html", form=form)


@app.route("/aboutsummonsheet/")
def about():
    return render_template("about_summon_sheet.html")


@app.route("/about_mats_profitability_tool")


@app.errorhandler(Exception)
def failure_form(e):
    return render_template("failure.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
