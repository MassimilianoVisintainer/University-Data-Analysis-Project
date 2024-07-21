import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  
from mathematicalOperations.math_functions import MathFunctions  
import pandas as pd


class TestMathFunctions(unittest.TestCase):
    """
    A test case class for testing methods of the MathFunctions class.
    """

    def test_calculate_deviation(self):
        """
        Test the calculate_deviation method of MathFunctions class.
        """
        # Define sample data for testing
        first_test_values = pd.DataFrame({
            'y1': [10, 11, 3, 8],
        })

        second_test_values = pd.DataFrame({
            'y1': [9, 9, 0, 4]  
        })

        # Define the expected result
        expected_deviation = pd.DataFrame({
            'y1': [1, 2, 3, 4] 
        })

        math_functions = MathFunctions()  # Instantiate MathFunctions class
        deviation = math_functions.calculate_deviation(first_test_values['y1'], second_test_values['y1'])  # Calculate deviation
        self.assertTrue((deviation == expected_deviation['y1']).all())  # Assert the calculated deviation is the one expected

    def test_sum_squared_deviations(self):
        """
        Test the sum_squared_deviations method of MathFunctions class.
        """
        # Define sample data for testing
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

        math_functions = MathFunctions()  # Instantiate MathFunctions class

        # Call the method sum_squared_deviations tested
        min_positions = math_functions.sum_squared_deviations(df_training_data, df_ideal_functions_data)

        # Define the expected result
        expected_min_positions = [0, 1] 

        # Assert the result is the one expected
        self.assertEqual(min_positions, expected_min_positions) 
