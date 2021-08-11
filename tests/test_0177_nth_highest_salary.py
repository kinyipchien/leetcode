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
177. Nth Highest Salary
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
                {"headers": {"Employee": ["Id", "Salary"]},
                 "argument": 2,
                 "rows": {"Employee": [[1, 100], [2, 200], [3, 300]]}}
            '''),
            json.loads('''
                {"headers": {"Employee": ["Id", "Salary"]},
                 "argument": 1,
                 "rows": {"Employee": [[1, 100], [2, 100]]}}
            ''')
        ]
        self.expected = [
            json.loads('''
                {"headers": ["getNthHighestSalary(2)"],
                 "values": [[200]]}
            '''),
            json.loads('''
                {"headers": ["getNthHighestSalary(1)"],
                 "values": [[100]]}
            ''')
        ]


    def case(self, i):
        employee = pd.DataFrame(
            self.input[i]['rows']['Employee'],
            columns=self.input[i]['headers']['Employee'])
        expected_df = pd.DataFrame(self.expected[i]['values'],
                                   columns=self.expected[i]['headers'])
        with open(
            'src/problems/0177-nth-highest-salary.sql'
        ) as f:
            q = f.read().format(N=self.input[i]['argument'])

        pysqldf = lambda q: sqldf(
            q, {'employee': employee})
        assert_frame_equal(pysqldf(q), expected_df)

    def test_exchange_seats(self):
        for i, _ in enumerate(self.input):
            self.case(i)
