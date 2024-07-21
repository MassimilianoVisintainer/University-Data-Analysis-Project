import sqlalchemy as db
import pandas as pd

class Database:
    """
    A class for interacting with a SQLite database.
    """

    def __init__(self, db_name):
        """
        Initialize the Database object.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        try:
            self.engine = db.create_engine(f'sqlite:///{db_name}')  # Create SQLite engine
            self.connection = self.engine.connect()  # Connect to the database
        except Exception as e:
            print(f"An error occurred during {db_name} database initialization:", e)

    def upload_data_to_table(self, table_name, df_data_example):
        """
        Upload DataFrame data to a table in the database.

        Args:
            table_name (str): The name of the table to upload data to.
            df_data_example (DataFrame): The DataFrame containing the data to upload.
        """
        try:
            self.df_data = df_data_example  # Store DataFrame data
            self.df_data.to_sql(table_name, self.engine, if_exists='replace', index=False)  # Upload data to table
        except Exception as e:
            print(f"An error occurred during data upload to table {table_name}:", e)
    
    def initialize_table(self, file_path, table_name):
        """
        Initialize a table in the database with data coming from a CSV file.

        Args:
            file_path (str): The path to the CSV file containing the data.
            table_name (str): The name of the table to initialize.
        """
        try:
            self.df_data = pd.read_csv(filepath_or_buffer=file_path, sep=',', encoding='latin1')  # Read data from CSV file
            self.upload_data_to_table(table_name, self.df_data)  # Upload data to table       
            print("Data loaded into database successfully.")
        except Exception as e:
            print(f"An error occurred during table {table_name} initialization:", e)

    def load_data_from_table(self, table_name):
        """
        Load data from a table in the database into a DataFrame.

        Args:
            table_name (str): The name of the table to load data from.

        Returns:
            DataFrame: The data loaded from the table.
        """
        try:
            df_table_data = pd.read_sql_table(table_name, self.engine)  # Load data from table into DataFrame
            return df_table_data
        except Exception as e:
            print(f"An error occurred during data loading from table {table_name}:", e)
            return pd.DataFrame()
