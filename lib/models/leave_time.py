
from ..api import cta


class LeaveTime(object):

    def __init__(self, eta, walk_time_min):

        self.eta = cta.eta_in_minutes(eta)
        self.walk_time_min = walk_time_min
        self.leave_time = self.calculate_leave_time(self.eta, walk_time_min)

        # Bus/Train information
        self.route_name = cta.route_name_from_eta(eta)

    @staticmethod
    def calculate_leave_time(eta, walk_time_min):
        """
        How much time do I have before I need to leave to catch this bus/train?
        """
        return eta - walk_time_min
