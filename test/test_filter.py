import unittest

from lib.filters import filter as filter_mod

PRETTY_MINUTES_LEAVE_NOW_TEXT = 'Leave now!'


class TestJinjaFilters(unittest.TestCase):

    def test_seconds_to_minutes_filter(self):

        x = filter_mod.seconds_to_minutes_filter(25.6)
        self.assertEqual(x, '0 mins')

        x = filter_mod.seconds_to_minutes_filter(123.4)
        self.assertEqual(x, '2 mins')
  
    def test_pretty_minutes_filter(self):

        x = filter_mod.pretty_minutes_filter(2)
        self.assertEqual(x, '2 mins')

        x = filter_mod.pretty_minutes_filter(5.34)
        self.assertEqual(x, '5 mins')

        x = filter_mod.pretty_minutes_filter(0.2)
        self.assertEqual(x, PRETTY_MINUTES_LEAVE_NOW_TEXT)


    def test_route_name_map_filter(self):

        x = filter_mod.route_name_map_filter("G")
        self.assertEqual(x, "Green")

        x = filter_mod.route_name_map_filter("centaurs")
        self.assertEqual(x, "centaurs")