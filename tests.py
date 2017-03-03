import unittest
import Trains


class TrainTests(unittest.TestCase):
    def test_is_train_approaching(self):
        train_that_is_not_approaching = self.fixture_data({u'isApp': u'0'})
        train_that_is_approaching = self.fixture_data({u'isApp': u'1'})

        self.assertFalse(Trains.is_train_approaching_station(train_that_is_not_approaching))
        self.assertTrue(Trains.is_train_approaching_station(train_that_is_approaching))

    def test_is_train_heading_into_loop(self):
        train_into_loop = self.fixture_data({u'trDr': Trains.TRAIN_DIRECTION_INTO_LOOP})
        train_away_from_loop = self.fixture_data({u'trDr': u'1'})

        self.assertTrue(Trains.is_train_heading_into_loop(train_into_loop))
        self.assertFalse(Trains.is_train_heading_into_loop(train_away_from_loop))

    def fixture_data(self, keyvals=None):
        replacement_values = keyvals or {}
        train = {
            u'arrT': u'2015-04-30T20:31:24',
            u'destNm': u'Kimbal',
            u'destSt': u'30173',
            u'flags': None,
            u'heading': u'269',
            u'isApp': u'0',
            u'isDly': u'0',
            u'lat': u'41.90383',
            u'lon': u'-87.63685',
            u'nextStaId': u'40650',
            u'nextStaNm': u'North/Clybourn',
            u'nextStpId': u'30125',
            u'prdt': u'2015-04-30T20:29:24',
            u'rn': u'827',
            u'trDr': u'1'
        }
        return {**train, **replacement_values}
