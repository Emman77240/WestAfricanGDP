import os
from flask import Flask, render_template, session, redirect, url_for, flash, request, logging
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, validators
from flask_wtf import Form
from envparse import env
import httplib2
import json

app = Flask(__name__,  static_url_path='/static')

env.read_envfile()

app.config['SECRET_KEY'] = env.str('SECRET_KEY')

bootstrap = Bootstrap(app)

class CountryData(Form):
    year = StringField('Year', [validators.Length(4)])
    submit = SubmitField('Submit')

class NameForm(Form):
    name = StringField('Tell me your name?', [validators.Required()])
    submit = SubmitField('Submit')


# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        return render_template('dashboard.html', form=form, name=name)
    else:
        return render_template('home.html', form=form)


# About
@app.route('/about')
def about():
    return render_template('about.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# Benin Republic Data Request
@app.route('/ben_data', methods=['GET', 'POST'])
def ben_data():
    year = None
    form = CountryData()
    if form.validate_on_submit():
        year = form.year.data
        form.year.data = ''

        # Make api request
        url = ('http://api.worldbank.org/v2/countries/ben/indicators/NY.GDP.MKTP.CD/?format=json')
        h = httplib2.Http()
        response, content = h.request(url,'GET')
        result = json.loads(content)

        for index in range(len(result[1])):
            date = result[1][index]['date']
            if date == year:
                if year >= '1968':
                    gdp = float(result[1][index]['value'])
                    return render_template('ben_display.html', gdp=gdp)
        else:
            flash('Invalid year input', 'danger')
            return render_template('ben_data.html', form=form)
    else:
        return render_template('ben_data.html', form=form)


@app.route('/ben_display', methods=['GET', 'POST'])
def ben_display():
    return render_template('ben_display.html', gdp=gdp)


# Burkina Faso Data Request
@app.route('/bfa_data', methods=['GET', 'POST'])
def bfa_data():
    year = None
    form = CountryData()
    if form.validate_on_submit():
        year = form.year.data
        form.year.data = ''

        # Make api request
        url = ('http://api.worldbank.org/v2/countries/bfa/indicators/NY.GDP.MKTP.CD/?format=json')
        h = httplib2.Http()
        response, content = h.request(url,'GET')
        result = json.loads(content)

        for index in range(len(result[1])):
            date = result[1][index]['date']
            if date == year:
                if year >= '1968':
                    gdp = float(result[1][index]['value'])
                    return render_template('bfa_display.html', gdp=gdp)
        else:
            flash('Invalid year input', 'danger')
            return render_template('bfa_data.html', form=form)
    else:
        return render_template('bfa_data.html', form=form)


@app.route('/bfa_display', methods=['GET', 'POST'])
def bfa_display():
    return render_template('bfa_display.html', gdp=gdp)


# Cote D'Ivoire Data Request
@app.route('/civ_data', methods=['GET', 'POST'])
def civ_data():
    year = None
    form = CountryData()
    if form.validate_on_submit():
        year = form.year.data
        form.year.data = ''

        # Make api request
        url = ('http://api.worldbank.org/v2/countries/civ/indicators/NY.GDP.MKTP.CD/?format=json')
        h = httplib2.Http()
        response, content = h.request(url,'GET')
        result = json.loads(content)

        for index in range(len(result[1])):
            date = result[1][index]['date']
            if date == year:
                if year >= '1968':
                    gdp = float(result[1][index]['value'])
                    return render_template('civ_display.html', gdp=gdp)
        else:
            flash('Invalid year input', 'danger')
            return render_template('civ_data.html', form=form)
    else:
        return render_template('civ_data.html', form=form)


@app.route('/civ_display', methods=['GET', 'POST'])
def civ_display():
    return render_template('civ_display.html', gdp=gdp)


# Ghana Data Request
@app.route('/ghana_data', methods=['GET', 'POST'])
def ghana_data():
    year = None
    form = CountryData()
    if form.validate_on_submit():
        year = form.year.data
        form.year.data = ''

        # Make api request
        url = ('http://api.worldbank.org/v2/countries/gha/indicators/NY.GDP.MKTP.CD/?format=json')
        h = httplib2.Http()
        response, content = h.request(url,'GET')
        result = json.loads(content)

        for index in range(len(result[1])):
            date = result[1][index]['date']
            if date == year:
                if year >= '1968':
                    gdp = float(result[1][index]['value'])
                    return render_template('ghana_display.html', gdp=gdp)
        else:
            flash('Invalid year input', 'danger')
            return render_template('ghana_data.html', form=form)
    else:
        return render_template('ghana_data.html', form=form)


@app.route('/ghana_display', methods=['GET', 'POST'])
def ghana_display():
    return render_template('ghana_display.html', gdp=gdp)


# Nigeria Data Request
@app.route('/nigeria_data', methods=['GET', 'POST'])
def nigeria_data():
    year = None
    form = CountryData()
    if form.validate_on_submit():
        year = form.year.data
        form.year.data = ''

        # Make api request
        url = ('http://api.worldbank.org/v2/countries/nga/indicators/NY.GDP.MKTP.CD/?format=json')
        h = httplib2.Http()
        response, content = h.request(url,'GET')
        result = json.loads(content)

        for index in range(len(result[1])):
            date = result[1][index]['date']
            if date == year:
                if year >= '1968':
                    gdp = float(result[1][index]['value'])
                    return render_template('nigeria_display.html', gdp=gdp)
        else:
            flash('Invalid year input', 'danger')
            return render_template('nigeria_data.html', form=form)
    else:
        return render_template('nigeria_data.html', form=form)


@app.route('/nigeria_display', methods=['GET', 'POST'])
def nigeria_display():
    return render_template('nigeria_display.html', gdp=gdp)


if __name__=='__main__':
    app.run(debug=True)



