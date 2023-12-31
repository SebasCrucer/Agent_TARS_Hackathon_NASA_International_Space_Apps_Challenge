# Import the 'Consultor' class from the 'api_io.consultor' module and the 'sys' module for handling command-line arguments.
from plugin_io.consultor import Consultor
import sys

# Retrieve the name of the planet from the command-line arguments.
planet_name = sys.argv[1]

# Create an instance of the 'Consultor' class and provide the path to a CSV file containing data (e.g., "planets_system.csv").
consultor_instance = Consultor("plugin_io\\planets_system.csv")

# Try to retrieve and print the flattened row data for the specified planet using the 'get_flat_row' method.
try:
    flattened_row_data = consultor_instance.get_flat_row(planet_name)
    print(flattened_row_data)

# Catch a KeyError if the specified planet name is not found in the data.
except KeyError:
    print("No records found for the specified planet.")
