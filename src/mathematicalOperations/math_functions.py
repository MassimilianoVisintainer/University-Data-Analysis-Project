import numpy as np

class MathFunctions:
    """
    A class containing mathematical functions.
    """

    def sum_squared_deviations(self, df_training_data, df_ideal_functions_data):
        """
        Function to minimize the sum of squared deviations for each ideal function.

        Args:
            df_training_data (DataFrame): DataFrame containing training data.
            df_ideal_functions_data (DataFrame): DataFrame containing ideal function data.

        Returns:
            list: A list of positions corresponding to the minimum sum of squared deviations for each ideal function.
        """
        try:
            min_position = []  # Initialize list to store positions of minimum deviations
            for col_training in df_training_data.columns[1:]:  # Exclude the first column (X)
                sum_of_deviations = []  # Initialize list to store sum of squared deviations
                for col in df_ideal_functions_data.columns[1:]:  # Exclude the first column (X)
                    deviation = self.calculate_deviation(df_training_data[col_training].values, df_ideal_functions_data[col].values)  # Calculate deviation between training data and ideal function
                    sum_of_squares = np.sum(element**2 for element in deviation)  # Calculate sum of squared deviations
                    sum_of_deviations.append(sum_of_squares)  # Append sum of squared deviations to the list
                min_dev_position = sum_of_deviations.index(min(sum_of_deviations))  # Find position of minimum deviation
                min_position.append(min_dev_position)  # Append position to the list
            return min_position  # Return list of positions
        except Exception as e:
            print("An error occurred during sum_squared_deviations:", e)
            return []

    def calculate_deviation(self, first_element, second_element):
        """
        Calculate the deviation between two arrays.

        Args:
            first_element (array-like): First array.
            second_element (array-like): Second array.

        Returns:
            array: Absolute deviation between the two arrays.
        """
        try:
            deviation = np.abs(first_element - second_element)  # Calculate absolute deviation
            return deviation  # Return deviation array
        except Exception as e:
            print("An error occurred during deviation calculation:", e)
            return []
