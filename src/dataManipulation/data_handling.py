from db.database_functions import Database
from mathematicalOperations.math_functions import MathFunctions
import math
import matplotlib.pyplot as plt
import pandas as pd

class DataHandler(Database):
    """
    A class for handling data processing tasks related to ideal functions and test data.
    Inherits from the Database class.

    Methods:
        select_ideal_functions:  Selects the four ideal functions that best fit the training data minimizing the sum of all y deviations squared (Least-Square).
        find_test_ideal_function: Map the test case points to the four ideal functions, and create the associated databases.
    """

    def select_ideal_functions(self, first_table, second_table):
        """
        Selects the four ideal functions that best fit the training data minimizing the sum of all y deviations squared (Least-Square).

        Args:
            first_table (str): The name of the table containing training data.
            second_table (str): The name of the table containing ideal function data.

        Returns:
            list: A list of indexes corresponding to the selected ideal functions.
        """
        try:
            math_functions = MathFunctions()  # Instantiate MathFunctions class
            df_training_data = self.load_data_from_table(first_table)  # Load training data from the databse
            df_ideal_functions_data = self.load_data_from_table(second_table)  # Load ideal functions data from the database
            chosen_indixes = math_functions.sum_squared_deviations(df_training_data, df_ideal_functions_data)  # Get the indexes of the four ideal functions based on least squares
            chosen_indexes = [x + 1 for x in chosen_indixes]  # Increase the indexes by 1 to consider the column X
            print("chosen index", chosen_indexes)
            return chosen_indexes  # Return the four selected ideal functions indexes
            
        except Exception as e:
            print("An error occurred during the selection of the four best fit ideal functions:", e)
            return []

    def find_test_ideal_function(self, test_table, ideal_functions_table, training_table, chosen_indixes):
        """
        Map the test case points to the four ideal functions, and create the associated databases.

        Args:
            test_table (str): The name of the table containing test data.
            ideal_functions_table (str): The name of the table containing selected ideal functions.
            training_table (str): The name of the table containing training data.
            chosen_indixes (list): A list of indexes corresponding to the selected ideal functions.

        Returns:
            None
        """
        try:
            math_functions = MathFunctions()  # Instantiate MathFunctions class
            df_test_data = self.load_data_from_table(test_table)  # Load test data from the database
            df_ideal_functions_data = self.load_data_from_table(ideal_functions_table)  # Load selected ideal functions from the database
            df_training_data = self.load_data_from_table(training_table)  # Load training data  from the database
            print("chosen indices", chosen_indixes)
            if chosen_indixes is not None:
                columns_to_select = [0] + chosen_indixes  # Columns to select for comparison, including the first column
            else:
                columns_to_select = [0]
            df_ideal_functions_selected_data = df_ideal_functions_data.iloc[:, columns_to_select]  # Select data associated to the four ideal functions selected
            self.upload_data_to_table('ideal_functions_selected_data', df_ideal_functions_selected_data)  # Upload selected ideal functions data to a new table
            max_deviation_training_ideal = []  # Initialize list to store maximum deviations
            # Calculate deviations between training data and selected ideal functions
            for col_train, col_ideal in zip(df_training_data.columns[1:], df_ideal_functions_selected_data.columns[1:]):
                deviation = math_functions.calculate_deviation(df_training_data[col_train].values, df_ideal_functions_selected_data[col_ideal].values)
                max_deviation = deviation.max()
                max_deviation_training_ideal.append(max_deviation)
                print("max_deviation_training_ideal", max_deviation_training_ideal)
            # Map test data to selected ideal functions and create associated databases
            for max_deviation_training_value, col_ideal in zip(max_deviation_training_ideal, df_ideal_functions_selected_data.columns[1:]):
                results = []  # Initialize list to store results
                # Iterate over test data
                for index, row in df_test_data.iterrows():
                    # Calculate deviation between test data and selected ideal function
                    deviation = math_functions.calculate_deviation(df_ideal_functions_selected_data[df_ideal_functions_selected_data['x'] == row['x']][col_ideal], row['y'])
                    # Check if deviation is within the  range defined by the task
                    if (deviation - max_deviation_training_value < (max_deviation_training_value * math.sqrt(2))).any():
                        results.append({
                            'x_value_test': row['x'],
                            'y_value_test': row['y'],
                            'deviation_y': deviation.iloc[-1],
                            'y_value_ideal': (df_ideal_functions_selected_data[df_ideal_functions_selected_data['x'] == row['x']][col_ideal]).iloc[-1]
                        })
                    else:
                        print("not in the range")
                results = pd.DataFrame(results)  # Convert results to DataFrame
                self.upload_data_to_table(f'test_data_{col_ideal}', results)  # Upload test data to a new table
        except Exception as e:
            print("An error occurred during test ideal function search:", e)
