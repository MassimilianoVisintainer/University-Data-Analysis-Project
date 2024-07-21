import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dataManipulation.data_handling import DataHandler
from db.database_functions  import Database  



class TestDataHandler(unittest.TestCase):

    def test_select_ideal_functions(self):
        # Define sample data for testing
        training_table = 'training_data'
        ideal_table = 'ideal_functions'
        db_name = 'test_database.db'

        # Initialize a Database object and create a temporary database
        database = Database(db_name)

        # Define sample training data and ideal function data
        df_training_data = pd.DataFrame({
            'X': [1, 2, 3],
            'y1': [10, 11, 12],
            'y2': [20, 21, 22]
        })
        df_ideal_functions_data = pd.DataFrame({
            'X': [1, 2, 3],
            'y1': [9, 10, 11],
            'y2': [19, 20, 21]
        })

        # Upload the sample data to the temporary database
        database.upload_data_to_table(training_table, df_training_data)
        database.upload_data_to_table(ideal_table, df_ideal_functions_data)

        # Call the method select_ideal_functions tested
        data_handling = DataHandler()
        chosen_indexes = data_handling.select_ideal_functions(training_table, ideal_table, db_name)

        # Define the expected result (based on the sample data defined before)
        expected_indexes = [1, 2] 

        # Assert if the result is the one expected
        self.assertEqual(chosen_indexes, expected_indexes)

        # Clean up by removing the temporary database created
        del database

