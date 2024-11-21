import requests
import json
def fetch_planet_data(planet_name):
    url = f"https://api.le-systeme-solaire.net/rest/bodies/{planet_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['isPlanet']:
            name = data['englishName']
            mass = f"{data['mass']['massValue']} E {data['mass']['massExponent']}"
            orbit_period = data['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
            raw_data = {
                "englishName": data['englishName'],
                "mass": data['mass'], 
                "sideralOrbit": data['sideralOrbit']
            }
            print(json.dumps(raw_data, indent=4))
        else:
            print(f"The provided name '{planet_name}' does not correspond to a planet.")
    else:
        print(f"Error fetching data for {planet_name}. Status code: {response.status_code}")

fetch_planet_data("jupiter")

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    if response.status_code == 200:
        planets = response.json()['bodies']
        return [planet for planet in planets if planet['isPlanet']]
    else:
        print(f"Error fetching planet data. Status code: {response.status_code}")
        return []

def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0
    for planet in planets:
        mass = float(f"{planet['mass']['massValue']} E {planet['mass']['massExponent']}")
        if mass > max_mass:
            max_mass = mass
            heaviest_planet = planet
    return heaviest_planet['englishName'], max_mass

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass}.")