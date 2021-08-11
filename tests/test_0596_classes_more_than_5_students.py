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


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [
            json.loads('''
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
                '''),
            json.loads('''
                {"headers": {"courses": ["student", "class"]},
                 "rows": {"courses": [["A", "Math"],
                                      ["B", "English"],
                                      ["C", "Math"],
                                      ["D", "Biology"],
                                      ["E", "Math"],
                                      ["F", "Math"],
                                      ["A", "Math"]]}}
                ''')
        ]
        self.expected = [
            json.loads('''
                {"headers": ["class"], "values": [["Math"]]}
                '''),
            json.loads('''
                {"headers":["class"],"values":[]}
                ''')
        ]

    def case(self, i):
        courses = pd.DataFrame(
            self.input[i]['rows']['courses'],
            columns=self.input[i]['headers']['courses'])
        expected_df = pd.DataFrame(self.expected[i]['values'],
                                   columns=self.expected[i]['headers'])

        with open(
            'src/problems/0596-classes-more-than-5-students.sql'
        ) as f:
            q = f.read()

        pysqldf = lambda q: sqldf(q, {'courses': courses})
        assert_frame_equal(pysqldf(q), expected_df)

    def test_classes_more_than_5_students(self):
        for i, _ in enumerate(self.input):
            self.case(i)
