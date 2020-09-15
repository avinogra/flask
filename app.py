
from flask import Flask, render_template
import data
app = Flask(__name__)


@app.route('/')
def main():
    tours=data.tours
    departures=data.departures
    return render_template('index.html',
                            tours=tours,
                            departures=departures)


@app.route('/departures/<departure>/')
def render_departures(departure):
    list_departure=dict()
    departures=data.departures
    for tour in data.tours:
        # print(data.tours.get(tour))
        if data.tours.get(tour)['departure']==departure:
            list_departure[tour]=data.tours.get(tour)
    nights = [list_departure[x]['nights'] for x in list_departure] 
    price = [list_departure[x]['price'] for x in list_departure] 
    stat = {'nights_min': min(nights),
            'nights_max': max(nights),
            'price_max': max(price),
            'price_min': min(price)}        
    return render_template('departure.html',
                            list_departure=list_departure,
                            stat=stat,
                            departures=departures)


@app.route('/tours/<int:id>/')
def render_tours(id):
    current_tours=data.tours.get(id)
    departures=data.departures
    return render_template('tour.html', 
                            tour=current_tours,
                            departures=departures)

if __name__ == '__main__':
    app.run()
# app.run(debug=True)
