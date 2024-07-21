import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from db.database_functions  import Database  

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Create an in-memory SQLite database for testing purpose
        self.db_name = ':memory:'
        self.database = Database(self.db_name)

    def test_upload_data_to_table(self):
        # Define sample data for testing
        df_data_example = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        })
        table_name = 'test_table'

        # Call the method upload_data_to_table to be tested
        self.database.upload_data_to_table(table_name, df_data_example)

        # Load data from the table
        df_loaded_data = self.database.load_data_from_table(table_name)

        # Assert the loaded data matches the original data defined
        pd.testing.assert_frame_equal(df_loaded_data, df_data_example)

if __name__ == '__main__':
    unittest.main()
