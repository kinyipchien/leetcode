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
180. Consecutive Numbers
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [
            json.loads('''
                {"headers": {"Logs": ["Id", "Num"]},
                 "rows": {"Logs": [[1, 1],
                                   [2, 1],
                                   [3, 1],
                                   [4, 2],
                                   [5, 1],
                                   [6, 2],
                                   [7, 2]]}}
                 '''),
            json.loads('''
                {"headers": {"Logs": ["Id", "Num"]},
                 "rows": {"Logs": [[1, 1],
                                   [2, 1],
                                   [4, 1],
                                   [5, 1]]}}
                 '''),
            json.loads('''
                {"headers": {"Logs": ["Id", "Num"]},
                 "rows": {"Logs": [[1, 3],
                                   [2, 3],
                                   [3, 3],
                                   [4, 3]]}}
                 '''),
            json.loads('''
                {"headers": {"Logs": ["Id", "Num"]},
                 "rows": {"Logs": [[1, 1],
                                   [2, 1],
                                   [3, 1],
                                   [4, 2],
                                   [5, 1],
                                   [6, 1],
                                   [7, 1]]}}
                 ''')
        ]
            
        self.expected = [
            json.loads('''
                {"headers": ["ConsecutiveNums"], "values": [[1]]}
                '''),
            json.loads('''
                {"headers": ["ConsecutiveNums"], "values": [[1]]}
                '''),
            json.loads('''
                {"headers": ["ConsecutiveNums"], "values": [[3]]}
                '''),
            json.loads('''
                {"headers": ["ConsecutiveNums"], "values": [[1]]}
                ''')
        ]


    def case(self, i):
        logs = pd.DataFrame(
            self.input[i]['rows']['Logs'],
            columns=self.input[i]['headers']['Logs'])
        expected_df = pd.DataFrame(self.expected[i]['values'],
                                   columns=self.expected[i]['headers'])

        with open(
            'src/problems/0180-consecutive-numbers.sql'
        ) as f:
            q = f.read()

        pysqldf = lambda q: sqldf(q, {'logs': logs})
        assert_frame_equal(pysqldf(q), expected_df)

    def test_exchange_seats(self):
        for i, _ in enumerate(self.input):
            self.case(i)
