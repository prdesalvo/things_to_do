import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import datetime as dt
from helper import the_knot_places

from replit import db

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)
app.config["SECRET_KEY"] = os.environ['secret']


class MyForm(FlaskForm):
    place = StringField('Find things to do in...',
                        validators=[DataRequired()],
                        render_kw={"placeholder": "Minneapolis"})


@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = MyForm()
    if form.validate_on_submit():
        place_entry = form.place.data
        print(place_entry)

        places_lst = the_knot_places(place_entry)
        db[place_entry] = len(places_lst)

        return render_template('success.html',
                               form=form,
                               place_text=place_entry,
                               places_lst=places_lst)

    return render_template('index.html', form=form)


@app.route('/about.html')  # What happens when the user visits the site
def about_page():
    return render_template('about.html')


app.run(host='0.0.0.0', port=8080, debug=False)
