from flask import Flask, render_template, jsonify, request
from pathFinder import path, graph
from pathFinder import haversineDistance, findClosestPlace, completeCoordinateList, PLACES
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/process_pathCoordinates', methods=['POST'])
def process_pathCoordinates():

    data = request.get_json()
    source = data[0]
    destination = data[1]
    day = data[2]
    time = data[3]


    # Slat, Slon = PLACES[source]
    # Dlat, Dlon = PLACES[destination]

    #  using geopy

    geolocator = Nominatim(user_agent="MyApp")

    S = geolocator.geocode(source)
    Slat, Slon = S.latitude, S.longitude

    D = geolocator.geocode(destination)
    Dlat, Dlon = D.latitude, D.longitude   

    ModifiedSource, ModifiedDestination = findClosestPlace(Slat, Slon), findClosestPlace(Dlat, Dlon)


    coordinateList = path(graph, ModifiedSource, ModifiedDestination)
    
    modifiedList = []

    for i in coordinateList:
        a = int(i[0])
        b = int(i[1])
        a = a*0.00001
        b = b*0.00001
        modifiedList.append([round(a, 5), round(b, 5)])

    print(modifiedList)
    
    return modifiedList




if __name__ == '__main__':
    app.run(debug=True) 
