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
596. Classes More Than 5 Students
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

table = json.loads('''
    {"headers": {"courses": ["student", "class"]},
     "rows": {"courses": [["A", "Math"],
                          ["B", "English"],
                          ["C", "Math"],
                          ["D", "Biology"],
                          ["E", "Math"],
                          ["F", "Computer"],
                          ["G", "Math"],
                          ["H", "Math"],
                          ["I", "Math"]]}}
    ''')
courses = pd.DataFrame(table['rows']['courses'],
                       columns=table['headers']['courses'])


class TestSolution(unittest.TestCase):

    def test_classes_more_than_5_students(self):
        with open(
            'src/problems/0596-classes-more-than-5-students.sql'
        ) as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["class"], "values": [["Math"]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)
