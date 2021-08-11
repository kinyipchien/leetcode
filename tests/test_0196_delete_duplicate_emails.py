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
196. Delete Duplicate Emails
"""
# BUG: pandasql doesn't support DELETE or UPDATE clauses.
# import json
# import unittest

# import pandas as pd
# from pandas.testing import assert_frame_equal
# from pandasql import sqldf


# class TestSolution(unittest.TestCase):

#     def setUp(self):
#         self.input = json.loads('''
#             {"headers": {"Person": ["Id", "Email"]},
#              "rows": {"Person": [[1, "john@example.com"],
#                                  [2, "bob@example.com"],
#                                  [3, "john@example.com"]]}}
#             ''')
#         self.expected = json.loads('''
#             {"headers": ["Id", "Email"],
#              "values": [[1, "john@example.com"], [2, "bob@example.com"]]}
#             ''')

#     def test_delete_duplicate_emails(self):
#         person = pd.DataFrame(
#             self.input['rows']['Person'],
#             columns=self.input['headers']['Person'])
#         expected_df = pd.DataFrame(self.expected['values'],
#                                    columns=self.expected['headers'])

#         with open(
#             'src/problems/0196-delete-duplicate-emails.sql'
#         ) as f:
#             q = f.read()

#         pysqldf = lambda q: sqldf(q, {'person': person})
#         assert_frame_equal(pysqldf(q), expected_df)
