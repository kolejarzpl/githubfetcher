import os
import urllib.request
import json
import csv

URL = "https://api.github.com/repos/nvbn/thefuck/contributors"

def fetch_data(url):
    with urllib.request.urlopen(url) as response:
        resp = json.loads(response.read().decode())
        return resp

def save_data(resp):
    #
    nameOfJsonFile = "contributors.json"
    nameOfCSVFile = "contributors.csv"

    dirname = os.getcwd()
    filepath = os.path.join(dirname, nameOfJsonFile)
    file = open(filepath, 'w+')
    file.write(str(resp))
    csv_columns = ['login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 'url', 'html_url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'organizations_url', 'subscriptions_url', 'repos_url', 'events_url', 'received_events_url', 'type', 'site_admin', 'contributions']
    dict_data = resp
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
