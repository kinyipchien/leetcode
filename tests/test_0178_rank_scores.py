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
178. Rank Scores
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = json.loads('''
            {"headers": {"Scores": ["Id", "Score"]},
             "rows": {"Scores": [[1, 3.50],
                                 [2, 3.65],
                                 [3, 4.00],
                                 [4, 3.85],
                                 [5, 4.00],
                                 [6, 3.65]]}}
            ''')
        self.expected = json.loads('''
            {"headers": ["Score", "Rank"],
             "values": [[4.00, 1],
                        [4.00, 1],
                        [3.85, 2],
                        [3.65, 3],
                        [3.65, 3],
                        [3.50, 4]]}
            ''')

    def test_exchange_seats(self):
        scores = pd.DataFrame(
            self.input['rows']['Scores'],
            columns=self.input['headers']['Scores'])
        expected_df = pd.DataFrame(self.expected['values'],
                                   columns=self.expected['headers'])

        with open(
            'src/problems/0178-rank-scores.sql'
        ) as f:
            q = f.read()

        pysqldf = lambda q: sqldf(q, {'scores': scores})
        assert_frame_equal(pysqldf(q), expected_df)
