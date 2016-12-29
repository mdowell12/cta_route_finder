import datetime

from ..api import cta
from .leave_time import LeaveTime


MAX_RESULTS_FROM_API = 5
MAX_ACCEPTABLE_ETA_MINS = 45

# TODO: replace with database
STATIONS = {
    "chicago": {"id": 41410, "walk_time_min": 7, "direction_id": 5, "type": "train"},
    "ashland": {"id": 40170, "walk_time_min": 13, "direction_id": 5, "type": "train"}
}


class Stop(object):
    """
    Factory pattern: https://github.com/gennad/Design-Patterns-in-Python/blob/master/factory.py
    """

    @staticmethod
    def create_stop(station):
        if Stop.is_train_stop(station):
            return TrainStop(station)
        else:
            return BusStop(station)

    @staticmethod
    def is_train_stop(station):
        stop = STATIONS[station]
        return stop["type"] == "train"


class TrainStop(object):

    def __init__(self, station):
        self._station = STATIONS[station]
        self._stop_id = self._station["id"]
        self._direction_id = self._station["direction_id"]
        
        self.station_name = station
        self.walk_time_min = self._station["walk_time_min"]
        self.leave_times = []
        self.has_nonnegative_leave_time = False

    def set_leave_times(self):
        self.leave_times = []

        etas = cta.get_train_etas(self._stop_id, direction_id=self._direction_id)
        etas = filter(lambda eta: self._is_valid_eta(eta), etas)
        etas = sorted(etas, key=(lambda eta: cta.eta_in_minutes(eta)))

        self.leave_times = [LeaveTime(eta, self.walk_time_min) for eta in etas]
        self.has_nonnegative_leave_time = any(l.leave_time > 0 for l in self.leave_times)

    @staticmethod
    def _is_valid_eta(eta_obj):
        eta_in_mins = cta.eta_in_minutes(eta_obj)
        return 0 <= eta_in_mins <= MAX_ACCEPTABLE_ETA_MINS


class BusStop(object):
    pass
