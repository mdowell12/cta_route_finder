import xml.etree.ElementTree as ET
import requests
import yaml
import os


cur_dir = os.path.dirname(os.path.abspath(__file__))
config = yaml.load(open(os.path.join(cur_dir, '../../config/config.yaml'), 'r'))

URL = config["cta_api"]["base_url"]
API_KEY = config["cta_api"]["api_key"]

station_ids = {
    "blue": {
        "chicago": 41410
    }
}


def construct_url(station_id):
    return URL + "?key=" + API_KEY + "&mapid=" + str(station_id)


def get_train_etas(line, stop, direction=None):
    url = construct_url(station_ids[line][stop])
    res = requests.get(url)
    
    if res.status_code != 200:
        raise Exception("Bad API request; error code {}".format(res.status_code))

    tree = ET.fromstring(res.text)

    if tree.find('errCd').text != '0':
        raise Exception("Error (code {}) returned by API: {}".format(tree.find('errCd').text, tree.find('errNm').text))

    return tree
