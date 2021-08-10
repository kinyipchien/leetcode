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
181. Employees Earning More Than Their Managers
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

table = json.loads('''
    {"headers": {"Employee": ["Id", "Name", "Salary", "ManagerId"]},
     "rows": {"Employee": [[1, "Joe", 70000, 3],
                           [2, "Henry", 80000, 4],
                           [3, "Sam", 60000, null],
                           [4, "Max", 90000, null]]}}
    ''')
employee = pd.DataFrame(table['rows']['Employee'],
                      columns=table['headers']['Employee'])


class TestSolution(unittest.TestCase):

    def test_employees_earning_more_than_their_managers(self):
        with open(
            'src/problems/0181-employees-earning-more-than-their-managers.sql'
        ) as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["Employee"], "values": [["Joe"]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)
