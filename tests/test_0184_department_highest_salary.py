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
184. Department Highest Salary
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
                {"headers":
                    {"Employee":
                        ["Id", "Name", "Salary", "DepartmentId"],
                     "Department": ["Id", "Name"]},
                 "rows": {"Employee": [[1, "Joe", 70000, 1],
                                       [2, "Jim", 90000, 1],
                                       [3, "Henry", 80000, 2],
                                       [4, "Sam", 60000, 2],
                                       [5, "Max", 90000, 1]],
                          "Department": [[1, "IT"], [2, "Sales"]]}}
            ''')
        ]
        self.expected = [
            json.loads('''
                {"headers": ["Department", "Employee", "Salary"],
                 "values": [["IT", "Jim", 90000],
                            ["Sales", "Henry", 80000],
                            ["IT", "Max", 90000]]}
            ''')
        ]


    def case(self, i):
        department = pd.DataFrame(
            self.input[i]['rows']['Department'],
            columns=self.input[i]['headers']['Department'])
        employee = pd.DataFrame(
            self.input[i]['rows']['Employee'],
            columns=self.input[i]['headers']['Employee'])
        expected_df = pd.DataFrame(self.expected[i]['values'],
                                   columns=self.expected[i]['headers'])

        with open(
            'src/problems/0184-department-highest-salary.sql'
        ) as f:
            q = f.read()

        pysqldf = lambda q: sqldf(
            q, {'department': department, 'employee': employee})
        assert_frame_equal(pysqldf(q), expected_df)

    def test_exchange_seats(self):
        for i, _ in enumerate(self.input):
            self.case(i)
