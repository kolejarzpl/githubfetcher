import os
import urllib.request
import json
import csv

import repository.contributorRepository
from service import contributorService
from repository import contributorRepository

import sqlite3

URL = "https://api.github.com/repos/nvbn/thefuck/contributors"


def fetch_data(url):
    with urllib.request.urlopen(url) as response:
        resp = json.loads(response.read().decode())
        return resp


def save_data(resp):
    name_of_json_file = "contributors.json"
    csv_file = "contributors.csv"

    dirname = os.getcwd()
    filepath = os.path.join(dirname, name_of_json_file)
    file = open(filepath, 'w+')
    file.write(str(resp))
    csv_columns = (
        'login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 'url', 'html_url', 'followers_url', 'following_url',
        'gists_url', 'starred_url', 'organizations_url', 'subscriptions_url', 'repos_url', 'events_url',
        'received_events_url', 'type', 'site_admin', 'contributions')
    dict_data = resp

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
    # save_data(resp)

    contributorService.add_contributors(resp)

    print(contributorService.get_all_contributors())
    print(contributorService.get_contributor_by_name("kimtree"))

    contributorRepository.drop_table("contributors")
