from flask import Flask, render_template, redirect, url_for
from forms import HeroInputForm
from controller import StatsController 

app = Flask(__name__)
app.secret_key = 'ieropajdklsagnfjklghrkjlffjdklasfjkdsa;'

@app.route('/', methods = ['GET','POST'])
def index():
    form = HeroInputForm()

    if form.validate_on_submit():
        controller = StatsController(form)
        stats_list = [stats_dict for stats_dict in controller.summon_odds_list]
        table_header, header_span_dict, table_subheader, table_rows = controller.return_table_headers_and_rows()

        return render_template('start_sheet.html', table_rows = table_rows, table_header = table_header, header_span = header_span_dict, table_subheader = table_subheader) 

    return render_template('index.html') 


@app.route('/hero_form/', methods = ['GET','POST'])
def hero_form():
    form = HeroInputForm()
    return render_template('hero_form.html', form = form)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.errorhandler(Exception)
def failure_form(e):
    return render_template('failure.html')



if __name__== "__main__":
    app.run(debug=True)


