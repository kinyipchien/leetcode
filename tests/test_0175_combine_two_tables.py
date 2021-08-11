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
175. Combine Two Tables
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = json.loads('''
            {"headers":
                {"Person": ["PersonId", "LastName", "FirstName"],
                 "Address":
                     ["AddressId", "PersonId", "City", "State"]},
             "rows":
                 {"Person": [[1, "Wang", "Allen"]],
                  "Address": [[1, 2, "New York City", "New York"]]}}
            ''')
        self.expected = json.loads('''
            {"headers": ["FirstName", "LastName", "City", "State"],
             "values": [["Allen", "Wang", null, null]]}
            ''')

    def test_combine_two_tables(self):
        address = pd.DataFrame(
            self.input['rows']['Address'],
            columns=self.input['headers']['Address'])
        person = pd.DataFrame(
            self.input['rows']['Person'],
            columns=self.input['headers']['Person'])
        expected_df = pd.DataFrame(self.expected['values'],
                                   columns=self.expected['headers'])

        with open(
            'src/problems/0175-combine-two-tables.sql'
        ) as f:
            q = f.read()

        pysqldf = lambda q: sqldf(
            q, {'address': address, 'person': person})
        assert_frame_equal(pysqldf(q), expected_df)
