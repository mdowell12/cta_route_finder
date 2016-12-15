from datetime import datetime
import yaml
import requests
import os
import xml.etree.ElementTree as ET


cur_dir = os.path.dirname(os.path.abspath(__file__))
config = yaml.load(open(os.path.join(cur_dir, '../../config/config.yaml'), 'r'))

TIME_FORMAT = "%Y%m%d %H:%M:%S"


def parse_time(s):
    return datetime.strptime(s, TIME_FORMAT)


class TrainETA(object):

    def __init__(self, eta_element):
        d = dict([(e.tag, e.text) for e in list(eta_element)])

        for k, v in d.iteritems():
            setattr(self, k, v)

        self.request_time = self.parse_time(self.prdt)
        self.arrival_time = self.parse_time(self.arrT)

        self.eta_from_request_time = self.get_eta_seconds(self.request_time)

    @staticmethod
    def parse_time(s):
        return parse_time(s)

    def get_eta_seconds(self, baseline=None):
        baseline = baseline if baseline else datetime.now()
        return (self.arrival_time - baseline).seconds
