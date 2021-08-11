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
176. Second Highest Salary
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = json.loads('''
            {"headers": {"Employee": ["Id", "Salary"]},
             "rows": {"Employee": [[1, 100], [2, 200], [3, 300]]}}
            ''')
        self.expected = json.loads('''
            {"headers": ["SecondHighestSalary"], "values": [[200]]}
            ''')

    def test_second_highest_salary(self):
        employee = pd.DataFrame(
            self.input['rows']['Employee'],
            columns=self.input['headers']['Employee'])
        expected_df = pd.DataFrame(self.expected['values'],
                                   columns=self.expected['headers'])

        with open(
            'src/problems/0176-second-highest-salary.sql'
        ) as f:
            q = f.read()

        pysqldf = lambda q: sqldf(q, {'employee': employee})
        assert_frame_equal(pysqldf(q), expected_df)
