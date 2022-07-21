import csv
import pandas as pd


rows = []

with open("planets.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
planet_data = rows[1:]

df = pd.read_csv("planets.csv")
solar_mass_list = df["solar_mass"].tolist()
solar_radius_list = df["solar_radius"].tolist()

solar_mass_list.pop(0)
solar_radius_list.pop(0)

planet_solar_mass_si_unit = []

for data in solar_mass_list:

    si_unit = float(data)*1.989e+30
    planet_solar_mass_si_unit.append(si_unit)

print(planet_solar_mass_si_unit)


planet_solar_radius_si_unit = []

for data in solar_radius_list:
    si_unit = float(data)* 6.957e+8
    planet_solar_radius_si_unit.append(si_unit)

print(planet_solar_radius_si_unit)

planet_masses = planet_solar_mass_si_unit
planet_radiuses = planet_solar_radius_si_unit
planet_names = df["planet_names"].tolist()
planet_names.pop(0)

planet_gravities = []

for index,data in enumerate(planet_names):
    gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
    planet_gravities.append(gravity)

print(planet_gravities)