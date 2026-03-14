from datetime import date
import matplotlib.pyplot as plt
import requests
import json

def get_data():
    responce = requests.get(
        "http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
            params={
                'starttime': "2000-01-01",
                "maxlatitude": "58.723",
                "minlatitude": "50.008",
                "maxlongitude": "1.67",
                "minlongitude": "-9.756",
                "minmagnitude": "1",
                "endtime": "2018-10-11",
                "orderby": "time-asc"}
        )
    text=responce.text
    quakes=json.loads(text)
    with open("earthquakes_data","w",encoding="utf-8")as f:
        json.dump(quakes,f,indent=4)
    return quakes

def get_year(earthquake):
    timestamp = earthquake['properties']['time']
    year = date.fromtimestamp(timestamp/1000).year

    return year


def get_magnitude(earthquake):
    magnitude=earthquake["properties"]["mag"]
    return magnitude


def get_magnitudes_per_year(earthquakes):
    
    magnitudes_per_year={}
    for earthquake in earthquakes:
        year=get_year(earthquake)
        magnitude=get_magnitude(earthquake)
        if year not in magnitudes_per_year:
            magnitudes_per_year[year]=[]
        magnitudes_per_year[year].append(magnitude)
    return magnitudes_per_year


def plot_average_magnitude_per_year(earthquakes):
    magnitudes_per_year=get_magnitudes_per_year(earthquakes)
    years=sorted(magnitudes_per_year.keys())
    average=[]
    for year in years:
        average_magnitude=sum(magnitudes_per_year[year])/len(magnitudes_per_year[year])
        average.append(average_magnitude)


    plt.figure()
    plt.plot(years,average)
    plt.xlabel("years")
    plt.ylabel("average")
    plt.title("average magnitudes per year")
    plt.savefig("average magnitudes per pear.png")

def plot_number_per_year(earthquakes):
    magnitudes_per_year=get_magnitudes_per_year(earthquakes)
    numbers=[]
    years=sorted(magnitudes_per_year.keys())
    for year in years:
        number=len(magnitudes_per_year[year])
        numbers.append(number)
    plt.figure()
    plt.plot(years,numbers)
    plt.xlabel("years")
    plt.ylabel("numbers")
    plt.title("number per year")
    plt.savefig("number per year.png")

quakes = get_data()["features"]

plot_number_per_year(quakes)

plt.clf()  # This clears the figure, so that we don't overlay the two plots

plot_average_magnitude_per_year(quakes)

def get_mag(earthquake):
    return earthquake ["properties"]["mag"]
def get_location(earthquake):
    long,lati,_=earthquake["geometry"]["coordinates"]
    return lati,long

def plot_earthquake_map(earthquakes,year=None):
    mags=[]
    latis=[]
    longs=[]
    for earthquake in earthquakes:
        if year is not None and get_year(earthquake)!=year:
            continue
        mag=get_mag(earthquake)
        lati,long=get_location(earthquake)
        latis.append(lati)
        longs.append(long)
        mags.append(mag*40)
    plt.figure(figsize=(8,6))
    plt.scatter(longs,latis,s=mags,alpha=0.7)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    if year is None:
        plt.title("earthquakes_map")
        plt.savefig("earthquakes_map.png")
    else:
        plt.title(f"earthquake-{year}")
        plt.savefig(f"earthquake_{year}.png")

plot_earthquake_map(quakes)

def all_years_maps(earthquakes):
    mag_per_year=get_magnitudes_per_year(earthquakes)
    years=sorted(mag_per_year.keys())
    for year in years:
        plot_earthquake_map(earthquakes,year)
all_years_maps(quakes)

def plot_earthquake_with_histograms(earthquakes, year=None):
    # Create three empty lists to store:
    # 1. magnitudes (used to control circle sizes)
    # 2. latitudes
    # 3. longitudes
    mags = []
    latis = []
    longs = []

    # Loop through every earthquake in the input list
    for earthquake in earthquakes:
        # If a specific year is given, skip earthquakes not from that year
        if year is not None and get_year(earthquake) != year:
            continue

        # Get magnitude from this earthquake
        mag = get_mag(earthquake)

        # Get latitude and longitude from this earthquake
        lati, long = get_location(earthquake)

        # Add latitude to the latitude list
        latis.append(lati)

        # Add longitude to the longitude list
        longs.append(long)

        # Scale magnitude so the scatter circles are easier to see
        mags.append(mag * 40)

    # Create one whole figure
    fig = plt.figure(figsize=(8, 8))

    # Add the main scatter plot area
    # [left, bottom, width, height]
    ax_scatter = fig.add_axes([0.1, 0.1, 0.65, 0.65])

    # Add the top histogram area (for longitude distribution)
    ax_histx = fig.add_axes([0.1, 0.78, 0.65, 0.18])

    # Add the right histogram area (for latitude distribution)
    ax_histy = fig.add_axes([0.78, 0.1, 0.18, 0.65])

    # Draw the main scatter plot:
    # x = longitude
    # y = latitude
    # s = marker size based on magnitude
    # alpha = transparency
    ax_scatter.scatter(longs, latis, s=mags, alpha=0.6)
    ax_scatter.set_xlabel("Longitude")
    ax_scatter.set_ylabel("Latitude")
    ax_scatter.set_title("Earthquakes map with histograms")

    # Draw the top histogram:
    # this shows how many earthquakes fall into each longitude bin
    ax_histx.hist(longs, bins=10)
    ax_histx.set_ylabel("Count")

    # Draw the right histogram:
    # this shows how many earthquakes fall into each latitude bin
    # orientation="horizontal" makes the bars go sideways
    ax_histy.hist(latis, bins=10, orientation="horizontal")
    ax_histy.set_xlabel("Count")

    # Save the whole figure to a png file
    fig.savefig("earthquakes_hist_map.png")