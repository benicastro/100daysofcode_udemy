"""
Cheap Flight Tracker by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Import needed modules/libraries #######
from data_manager import DataManager

# Create instance of DataManager class
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

# Check if sheet_data contains any values for the "iataCode" key. If not, use the FlightSearch class to get them.
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
