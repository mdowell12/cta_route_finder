import xml.etree.ElementTree as ET
import requests
import yaml
import os
import datetime


TIME_FORMAT_TRAIN = "%Y%m%d %H:%M:%S"
TIME_FORMAT_BUS   = "%Y%m%d %H:%M"

cur_dir = os.path.dirname(os.path.abspath(__file__))
config = yaml.load(open(os.path.join(cur_dir, '../../config/config.yaml'), 'r'))

TRAIN_URL = config["cta_api"]["train_url"]
TRAIN_API_KEY = config["cta_api"]["train"]

BUS_URL = config["cta_api"]["bus_url"]
BUS_API_KEY = config["cta_api"]["bus"]

def construct_base_url_train(station_id):
    return TRAIN_URL + "?key=" + TRAIN_API_KEY + "&mapid=" + str(station_id)

def construct_base_url_bus(route, station_id, direction_id):
    """
    Example: http://www.ctabustracker.com/bustime/api/v2/getstops?key=vcmLZ8ijQBfAa85dx674crqpT&rt=65&dir=Eastbound
    """
    return BUS_URL + "?key=" + BUS_API_KEY + "&rt=" + str(route) + "&stpid=" + str(station_id) + "&dir" + str(direction_id)

def get_train_etas(station_id, direction_id=None, max_results=None):
    url = construct_base_url_train(station_id)

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


def get_bus_etas(route, station_id, direction_id, max_results=None):
    url = construct_base_url_bus(route, station_id, direction_id)

    res = requests.get(url)

    if res.status_code != 200:
        raise Exception("Bad API request; error code {}".format(res.status_code))

    tree = ET.fromstring(res.text)

    if tree.find('error') is not None:
        raise Exception("Error returned by bus API: {}".format(tree.find('error').find('msg').text))

    return tree.findall('prd')


def route_name_from_eta_train(eta):
    rt = eta.find('rt').text
    destination = eta.find('destNm').text
    stop_name = eta.find('staNm').text

    return "{} Line to {} at {}".format(_route_name_map_filter(rt), destination, stop_name)


def route_name_from_eta_bus(prd):
    rt =        prd.find('rt').text
    direction = prd.find('rtdir').text
    stop_name = prd.find('stpnm').text

    return "{} {} at {}".format(rt, direction, stop_name)


def eta_in_minutes_train(eta):
    arrival = eta.find('arrT').text
    eta = _parse_time(arrival, TIME_FORMAT_TRAIN) - datetime.datetime.now()
    return eta.seconds / 60.0


def eta_in_minutes_bus(prd):
    arrival = prd.find('prdtm').text
    eta = _parse_time(arrival, TIME_FORMAT_BUS) - datetime.datetime.now()
    return eta.seconds / 60.0


def _parse_time(s, time_format):
    return datetime.datetime.strptime(s, time_format)

def _route_name_map_filter(r):
    """
    CTA API returns weird route names sometimes.  Map them to pretty values here.
    """
    m = {
        "G": "Green"
    }

    return m[r] if r in m else r
