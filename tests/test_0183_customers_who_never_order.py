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
183. Customers Who Never Order
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = json.loads('''
            {"headers": {"Customers": ["Id", "Name"],
                         "Orders": ["Id", "CustomerId"]},
             "rows": {"Customers": [[1, "Joe"],
                                    [2, "Henry"],
                                    [3, "Sam"],
                                    [4, "Max"]],
                      "Orders": [[1, 3],
                                 [2, 1]]}}
            ''')
        self.expected = json.loads('''
            {"headers": ["Customers"], "values": [["Henry"], ["Max"]]}
            ''')

    def test_customers_who_never_order(self):
        customers = pd.DataFrame(
            self.input['rows']['Customers'],
            columns=self.input['headers']['Customers'])
        orders = pd.DataFrame(
            self.input['rows']['Orders'],
            columns=self.input['headers']['Orders'])
        expected_df = pd.DataFrame(self.expected['values'],
                                   columns=self.expected['headers'])

        with open(
            'src/problems/0183-customers-who-never-order.sql'
        ) as f:
            q = f.read()

        pysqldf = lambda q: sqldf(
            q, {'customers':customers, 'orders': orders})
        assert_frame_equal(pysqldf(q), expected_df)
