
from ..api import cta


class LeaveTime(object):

    def __init__(self, eta_in_minutes, walk_time_min, route_name=None, color=None):

        self.eta = eta_in_minutes
        self.walk_time_min = walk_time_min
        self.leave_time = self.calculate_leave_time(self.eta, walk_time_min)

        # Bus/Train information
        self.route_name = route_name
        self.color = color.lower() if color else None

    @staticmethod
    def calculate_leave_time(eta, walk_time_min):
        """
        How much time do I have before I need to leave to catch this bus/train?
        """
        return eta - walk_time_min
