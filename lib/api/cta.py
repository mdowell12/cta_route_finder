import xml.etree.ElementTree as ET
import requests
import yaml
import os
import datetime


TIME_FORMAT = "%Y%m%d %H:%M:%S"

cur_dir = os.path.dirname(os.path.abspath(__file__))
config = yaml.load(open(os.path.join(cur_dir, '../../config/config.yaml'), 'r'))

URL = config["cta_api"]["train_url"]
API_KEY = config["cta_api"]["train"]


def construct_base_url(station_id):
    return URL + "?key=" + API_KEY + "&mapid=" + str(station_id)


def get_train_etas(station_id, direction_id=None, max_results=None):
    url = construct_base_url(station_id)

    # Note this is applied to both route directions!
    if max_results is not None:
        url += "&max={}".format(max_results)

    res = requests.get(url)
    
    if res.status_code != 200:
        raise Exception("Bad API request; error code {}".format(res.status_code))

    tree = ET.fromstring(res.text)

    if tree.find('errCd').text != '0':
        raise Exception("Error (code {}) returned by API: {}".format(tree.find('errCd').text, tree.find('errNm').text))

    if direction_id is not None:
        tree = filter(lambda e: e.find('trDr').text == str(direction_id), tree.findall('eta'))

    return tree


def route_name_from_eta(eta):
    return eta.find('rt').text


def eta_in_minutes(eta):
    arrival = eta.find('arrT').text
    eta = _parse_time(arrival) - datetime.datetime.now()
    return eta.seconds / 60.0


def _parse_time(s):
    return datetime.datetime.strptime(s, TIME_FORMAT)

