from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField)
from wtforms.validators import InputRequired

class HeroInputForm(FlaskForm):
    your_hero = StringField('Your Hero And Summon Cost:', validators=[InputRequired()])
    your_hero_realm = RadioField('Your Hero Realm: ', choices = ['Serendale', 'Serendale 2', 'Crystalvale'], validators = [InputRequired()])
    sd_candidate_list = TextAreaField('Serendale Candidates And Summon Costs:')
    sd_2_candidate_list = TextAreaField('Serendale 2 Candidates And Summon Costs:')
    cv_candidate_list = TextAreaField('Crystalvale Candidates And Summon Costs:')
