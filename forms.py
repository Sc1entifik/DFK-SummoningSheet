from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField)
from wtforms.validators import InputRequired

class HeroInputForm(FlaskForm):
    your_hero = StringField('YourHero', validators = [InputRequired()])
    sd_candidate_list = TextAreaField('SDCandidates')
    sd_2_candidate_list = TextAreaField('SD2Candidates')
    cv_candidate_list = TextAreaField('CVCandidates')
    your_hero_realm = RadioField('Realm', choices = ['Serendale', 'Serendale 2', 'Crystalvale'], validators = [InputRequired()])
