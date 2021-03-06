# Copyright (C) 2021  Kin-Yip Chien

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
626. Exchange Seats
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = json.loads('''
            {"headers": {"seat": ["id", "student"]},
             "rows": {"seat": [[1, "Abbot"],
                               [2, "Doris"],
                               [3, "Emerson"],
                               [4, "Green"],
                               [5, "Jeames"]]}}
            ''')
        self.expected = json.loads('''
            {"headers": ["id", "student"],
             "values": [[1, "Doris"],
                        [2, "Abbot"],
                        [3, "Green"],
                        [4, "Emerson"],
                        [5, "Jeames"]]}
            ''')

    def test_exchange_seats(self):
        seat = pd.DataFrame(
            self.input['rows']['seat'],
            columns=self.input['headers']['seat'])
        expected_df = pd.DataFrame(self.expected['values'],
                                   columns=self.expected['headers'])

        with open(
            'src/problems/0626-exchange-seats.sql'
        ) as f:
            q = f.read()

        pysqldf = lambda q: sqldf(q, {'seat': seat})
        assert_frame_equal(pysqldf(q), expected_df)
