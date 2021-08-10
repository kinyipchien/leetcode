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
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

table = json.loads('''
    {"headers": {"Person": ["Id", "Email"]},
     "rows": {"Person": [[1, "john@example.com"],
                         [2, "bob@example.com"],
                         [3, "john@example.com"]]}}
    ''')
person = pd.DataFrame(table['rows']['Person'],
                      columns=table['headers']['Person'])


# class TestSolution(unittest.TestCase):

#     # BUG: pandasql doesn't support DELETE or UPDATE clauses.
#     def test_delete_duplicate_emails(self):
#         with open(
#             'src/problems/0196-delete-duplicate-emails.sql'
#         ) as f:
#             q = f.read()

#         result = json.loads('''
#         {"headers": ["Id", "Email"],
#          "values": [[1, "john@example.com"], [2, "bob@example.com"]]}
#         ''')

#         result_df = pd.DataFrame(result['values'],
#                                  columns=result['headers'])
#         assert_frame_equal(pysqldf(q), result_df)
