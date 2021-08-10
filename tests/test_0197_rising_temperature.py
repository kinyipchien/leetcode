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
197. Rising Temperature
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

table = json.loads('''
    {"headers": {"Weather": ["Id", "RecordDate", "Temperature"]},
     "rows": {"Weather": [[1, "2015-01-01", 10],
                          [2, "2015-01-02", 25],
                          [3, "2015-01-03", 20],
                          [4, "2015-01-04", 30]]}}
    ''')
weather = pd.DataFrame(table['rows']['Weather'],
                       columns=table['headers']['Weather'])


class TestSolution(unittest.TestCase):

    def test_rising_temperature(self):
        with open(
            'src/problems/0197-rising-temperature.sql'
        ) as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["Id"], "values": [[2], [4]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)
