import csv
import json
import os
import urllib.request

from repository import contributorRepository
from service import contributorService
from repository import userRepository
from service import userService

URL = "https://api.github.com/repos/nvbn/thefuck/contributors"
login = 0


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

def addUser(user_url):
    login = input("Podaj login użytkownika:")
    print("podany login:", login)
    user_URL = "https://api.github.com/users/"+login

    return user_URL

def fetch_user_data(user_url):
    with urllib.request.urlopen(user_url) as user_response:
        user_response = json.loads(user_response.read().decode())
        return user_response


if __name__ == '__main__':
    resp = fetch_data(URL)
    # save_data(resp)

    contributorService.add_contributors(resp)

    print(contributorService.get_all_contributors())
    # print(contributorService.get_contributor_by_name("kimtree"))

    contributorRepository.drop_table("contributors")

    user_URL = addUser(login)
    print(user_URL)
    user_resp = fetch_user_data(user_URL)
    print(type(user_resp))
    print(resp)

    userService.add_users(user_resp)
    print(user_resp)
    print(userService.get_all_users())
    userRepository.drop_table("users")


