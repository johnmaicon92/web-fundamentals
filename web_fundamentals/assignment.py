"""
1. Exploring Web Technologies and Python Programming
Objective: The aim of this assignment is to deepen your understanding and practical skills in web technologies and Python programming. You will explore the functionalities of the World Wide Web, web architectures, and the Python programming language, particularly focusing on setting up environments, API interactions, and data handling.

Problem Statement: You are tasked with creating a Python application that interfaces with a public API, fetches data, and processes it. This application should provide insights into how different web architectures work and demonstrate your ability to set up a Python environment, make API requests, and handle JSON data.

Task 1: Setting Up a Python Virtual Environment and Installing Packages

1. Create a new Python virtual environment in your project directory.

2. Activate the virtual environment.

3. Install the `requests` packages.

Expected Outcome: A successfully created and activated virtual environment with the required packages installed.

Task 2: Fetching Data from the Pokémon API

1. Write a Python script to make a GET request to the Pokémon API (`https://pokeapi.co/api/v2/pokemon/pikachu`).

2. Extract and print the name and abilities of the Pokémon.

Expected Outcome: The script should output the name of the Pokémon (Pikachu) and a list of its abilities.

Task 3: Analyzing and Displaying Data

1. Modify the script to fetch data for three different Pokémon.

2. Create a function to calculate and return the average weight of these Pokémon.

3. Print the names, abilities, and average weight of the three Pokémon. **Code Example:**

def fetch_pokemon_data(pokemon_name):
    return #json response

def calculate_average_weight(pokemon_list):
    return #average weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
Expected Outcome: The script should display the names and abilities of the three chosen Pokémon and their average weight. The function should correctly calculate and return the average weight based on the data fetched from the API. 

2. Exploring the Digital Cosmos with Python and the Web
Problem Statement: Imagine you are a developer tasked with creating a feature for a web application that provides users with insightful information about various space objects. Your application will fetch data from a publicly available space API, process this data, and display it in a user-friendly format.

Task 1: Set up a Python Virtual Environment and Install Required Packages

Create a new virtual environment in Python. Activate the virtual environment. Install the `requests` package for making HTTP requests.

Expected Outcome: A successfully created and activated virtual environment with the `requests` package installed.

Task 2: Fetch Data from a Space API Write a Python script that makes a GET request to a space API (e.g., [The Solar System OpenData](https://api.le-systeme-solaire.net/en/)) to fetch data about planets.

Parse the JSON response and extract information about each planet, such as its name, mass, and orbit period.

Code Example:

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = #get planet English name
            mass = #get planet mass
            orbit_period = #get planet orbit period
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()
Expected Outcome:

Planet: Uranus, Mass: 8.68127, Orbit Period: 30685.4 days
Planet: Neptune, Mass: 1.02413, Orbit Period: 60189.0 days
Planet: Jupiter, Mass: 1.89819, Orbit Period: 4332.589 days
Planet: Mars, Mass: 6.41712, Orbit Period: 686.98 days
Planet: Mercury, Mass: 3.30114, Orbit Period: 87.969 days
Planet: Saturn, Mass: 5.68336, Orbit Period: 10759.22 days
Planet: Earth, Mass: 5.97237, Orbit Period: 365.256 days
Planet: Venus, Mass: 4.86747, Orbit Period: 224.701 days
Task 3: Data Presentation and Analysis - Perform a simple analysis, such as finding the planet with the longest orbit period or the heaviest planet. 

import requests

def fetch_planet_data():
    # Enhance format the output in a more readable manner
    return #list of planets

def find_heaviest_planet(planets):
    return #heaviest planet

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
Expected Outcome: A more structured and formatted output, along with an analysis result, such as identifying the heaviest planet in the solar system.
"""