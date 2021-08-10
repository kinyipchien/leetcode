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
pysqldf = lambda q: sqldf(q, globals())

table = json.loads('''
    {"headers": {"Customers": ["Id", "Name"],
                 "Orders": ["Id", "CustomerId"]},
     "rows": {"Customers": [[1, "Joe"],
                            [2, "Henry"],
                            [3, "Sam"],
                            [4, "Max"]],
              "Orders": [[1, 3],
                         [2, 1]]}}
    ''')
customers = pd.DataFrame(table['rows']['Customers'],
                      columns=table['headers']['Customers'])
orders = pd.DataFrame(table['rows']['Orders'],
                      columns=table['headers']['Orders'])


class TestSolution(unittest.TestCase):

    def test_customers_who_never_order(self):
        with open(
            'src/problems/0183-customers-who-never-order.sql'
        ) as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["Customers"], "values": [["Henry"], ["Max"]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)
