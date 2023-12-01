# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type

import requests
import csv

URI = "https://courttribunalfinder.service.gov.uk/search/results.json?postcode="


def get_people_data() -> list[dict]:
    people = []
    with open("people.csv", "r") as people_file:
        people_csv = csv.reader(people_file, delimiter=',')
        next(people_csv, None)
        for row in people_csv:
            people.append(
                {'name': row[0], 'postcode': row[1], 'type_of_court': row[2]})
        return people


def get_json_from_postcode(postcode: str) -> list[str]:
    response = requests.get(
        f"https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={postcode}")

    if response.status_code == 404:
        print("Unable to find postcode info.")
    if response.status_code == 500:
        print("Unable to connect!")

    return response.json()


def get_court_data(person: dict) -> dict:
    person['distance_to_court'] = 1000000
    courts_data = get_json_from_postcode(person['postcode'])
    for court in courts_data:
        if person['type_of_court'] in court['types'] and court['distance'] < person['distance_to_court']:
            person['name_of_nearest_court'] = court['name']
            person['court_dx_number'] = court['dx_number']
            person['distance_to_court'] = court['distance']

    if not person['court_dx_number']:
        person['court_dx_number'] = "N/A"

    return person


def output_data(person: dict):
    print("-" * 10)
    print(f"Name: {person['name']}")
    print(f"Postcode: {person['postcode']}")
    print(f"Type of Court: {person['type_of_court']}")
    print(f"Name of Nearest Court: {person['name_of_nearest_court']}")
    print(f"Dx number of Court: {person['court_dx_number']}")
    print(f"Distance to Court: {person['distance_to_court']}km")
    print("\n")


if __name__ == "__main__":
    # [TODO]: write your answer here

    people = get_people_data()
    for person in people:
        person = get_court_data(person)
        output_data(person)
