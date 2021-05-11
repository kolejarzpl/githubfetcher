import os
import urllib.request
import json
import csv
import sys
import pandas as pd

# URL = "https://api.github.com/repos/nvbn/thefuck/contributors"
URL = "https://api.github.com/users/KrzysztofO19926"

#dupa dupa cyckzx

def fetch_data(url):
    with urllib.request.urlopen(url) as response:
        resp = json.loads(response.read().decode())
        print(resp)
        return resp


def save_data(resp):
    #
    nameOfJsonFile = "contributors.json"
    nameOfCSVFile = "contributors.csv"

    dirname = os.getcwd()
    filepath = os.path.join(dirname, nameOfJsonFile)
    file = open(filepath, 'w+')
    file.write(str(resp))

    # print(resp['login'])

    # x = json.dumps(resp)

    for key, value in resp.items():
        print(key, value)

    csv_columns = ['No', 'Name', 'Country']
    dict_data = [
        {'No': 1, 'Name': 'Alex', 'Country': 'India'},
        {'No': 2, 'Name': 'Ben', 'Country': 'USA'},
        {'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
        {'No': 4, 'Name': 'Smith', 'Country': 'USA'},
        {'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
    ]
    csv_file = "Names.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")


if __name__ == '__main__':
    resp = fetch_data(URL)
    save_data(resp)
