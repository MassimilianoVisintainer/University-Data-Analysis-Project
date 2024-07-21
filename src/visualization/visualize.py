from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Category10
from db.database_functions import Database

class Visualization:
    """
    A class to visualize data using Bokeh plots.

    Attributes:
        database (Database): An instance of the Database class to interact with the database.
        df_ideal_functions_selected (DataFrame): DataFrame containing selected ideal functions data.

    Methods:
        plot_test_ideal: Plot test data points against ideal functions.
        plot_training_ideal_selected_graph: Plot training functions against selected four ideal functions.
    """

    def __init__(self):
        """
        Initializes the Visualization object by loading ideal functions data from the database.
        """
        try:
            self.database = Database('data.db')
            self.df_ideal_functions_selected = self.database.load_data_from_table('ideal_functions_selected_data')
        except Exception as e:
            print("An error occurred during initialization:", e)

    def plot_test_ideal(self, y_value):
        """
        Plots test data points against ideal functions.

        Args:
            y_value (str): The y-value identifier.

        Returns:
            None
        """
        try:
            df_test_ideal = self.database.load_data_from_table(f"test_data_{y_value}")

            # Create a Bokeh plot
            output_file(f"../plots/TestIdeal{y_value}.html")
            p = figure(title=f"Test data points vs. Ideal Functions {y_value}", x_axis_label="X", y_axis_label="Y")

            # Plot test data points 
            p.scatter(df_test_ideal['x_value_test'], df_test_ideal['y_value_test'], legend_label=f"Test data points for {y_value}", color="blue", size=8)
            
            # Plot ideal function 
            p.line(self.df_ideal_functions_selected['x'], self.df_ideal_functions_selected[y_value], legend_label=f"Ideal function {y_value}", color="red")
            
            p.legend.location = "top_left"
            p.legend.click_policy = "hide"
            show(p)
        except Exception as e:
            print(f"An error occurred during plotting TestIdeal{y_value}:", e)

    def plot_training_ideal_selected_graph(self):
        """
        Plots training functions against selected four ideal functions.

        Returns:
            None
        """
        try:
            df_training_data = self.database.load_data_from_table('training_data')

            # Create a Bokeh plot
            output_file("../plots/TrainingIdeal.html")
            p = figure(title="Training functions vs. 4 Ideal Functions", x_axis_label="X", y_axis_label="Y")

            # Define color palette for ideal functions
            colors = Category10[10]
            
            # Plot ideal functions
            for i, col_ideal in enumerate(self.df_ideal_functions_selected.columns[1:]):
                p.line(self.df_ideal_functions_selected['x'], self.df_ideal_functions_selected[col_ideal], legend_label=f"Ideal Function {col_ideal}", color=colors[i % len(colors) + 1])

            # Plot training functions
            for i, col_train in enumerate(df_training_data.columns[1:]):
                p.line(df_training_data['x'], df_training_data[col_train], legend_label=f"Training Function {col_train}", color=colors[i % len(colors)])
                    
            p.legend.location = "top_left"
            p.legend.click_policy = "hide"
            show(p)
        except Exception as e:
            print("An error occurred during plotting TrainingIdeal:", e)
