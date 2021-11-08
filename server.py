import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import date, datetime


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    list_email_club = []
    for club in clubs:
        list_email_club.append(club['email'])
    email = request.form['email']
    if email in list_email_club:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        today = datetime.now()
        active_competition = []
        for competition in competitions:
            date_comp = competition['date']
            date_time_comp = datetime.strptime(date_comp, '%Y-%m-%d %H:%M:%S')
            if today < date_time_comp:
                active_competition.append(competition)

        return render_template('welcome.html', clubs=clubs, club=club, 
            active_competition=active_competition, competitions=competitions)

    else:
        flash("Adresse mail incorrect.Veuillez réessayer.")
        return render_template('index.html')



@app.route('/book/<competition>/<club>')
def book(competition,club): 
    competition_obj = [item for item in competitions if item["name"] == competition][0]
    places_available = int(competition_obj['numberOfPlaces'])
    club_obj = [item for item in clubs if item["name"] == club][0]
    points_club = int(club_obj['points'])
    max_booking = min(places_available, points_club)
    if max_booking >= 12:
        max_booking = 12
    else:
        max_booking = max_booking
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition, max_booking=max_booking)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, 
            competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
    club['points'] = int(club['points']) - placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', clubs=clubs, club=club, 
        competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))