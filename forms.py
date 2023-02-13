from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField)
from wtforms.validators import InputRequired

class HeroInputForm(FlaskForm):
    your_hero = StringField('Your Hero', validators = [InputRequired()])
    your_hero_realm = RadioField('Your Hero Realm', choices = ['Serendale', 'Serendale 2', 'Crystalvale'], validators = [InputRequired()])
    your_hero_summon_cost = StringField('Your Hero Summon Cost')

    sd_candidate_list = TextAreaField('Serendale Candidates')
    sd_summon_cost = TextAreaField('Serendale Candidate Hero Summon Cost')
    
    sd_2_candidate_list = TextAreaField('Serendale 2 Candidates')
    sd_2_summon_cost = TextAreaField('SD 2 Candidate Hero Summon Cost + Hire Price')

    cv_candidate_list = TextAreaField('Crystalvale Candidates')
    cv_summon_cost = TextAreaField('Crystalvale Hero Summon Cost + Hire Price')
