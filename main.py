import os
import urllib.request
import json
import pandas as pd

# URL = "https://api.github.com/repos/nvbn/thefuck/contributors"
URL = "https://api.github.com/users/KrzysztofO19926"


# JSON_FILE_PATH = "path"


def fetch_data(url):
    with urllib.request.urlopen(url) as response:
        resp = json.loads(response.read())
        print(resp)
        return resp


def save_data(resp):
    nameOfJsonFile = "contributors.json"
    nameOfCSVFile = "contributors.csv"

    dirname = os.getcwd()
    filepath = os.path.join(dirname, nameOfJsonFile)
    file = open(filepath, 'w+')
    file.write(str(resp))

    print(resp)

    # jsonFile = pd.read_json(filepath)
    jsonFile = pd.read_json(r'C:\Users\Krzysiek\Dropbox\priv\Python\githubfetcher\contributors.json', orient='index')

    jsonFile.to_csv(filepath + nameOfCSVFile, index=False)


if __name__ == '__main__':
    resp = fetch_data(URL)
    save_data(resp)

