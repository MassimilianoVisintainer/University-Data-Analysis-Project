from dataManipulation.data_handling import DataHandler
from configparser import ConfigParser
from visualization.visualize import Visualization

def main():
    """
    The main function of the script responsible for implementing the data handling, visualization, and database operations.
    """
    # Initialize ConfigParser to read configuration from config.ini file
    config = ConfigParser()
    config.read('config.ini') 

    # Initialize DataHandler and Visualization objects
    data_handler = DataHandler('data.db')  # Pass the database name to DataHandler constructor
    visualization = Visualization()

    # Initialize tables using DataHandler
    data_handler.initialize_table(config.get('FilePath','test_file_path'), 'test_data')
    data_handler.initialize_table(config.get('FilePath','ideal_function_file_path'), 'ideal_function_table')
    data_handler.initialize_table(config.get('FilePath','training_file_path'), 'training_data')  

    # Find the indexes of the four  ideal function that best fit the four training functions
    choosen_indexes = data_handler.select_ideal_functions('training_data', 'ideal_function_table')
    # Map the individual test case points to the four ideal functions
    data_handler.find_test_ideal_function('test_data', 'ideal_function_table', 'training_data', choosen_indexes)

    # Plot graphs
    visualization.plot_training_ideal_selected_graph()
    for index in choosen_indexes:
        visualization.plot_test_ideal(f'y{index}')

if __name__ == "__main__":
    main()
