# Import needed modules/libraries #######
import requests

# from pprint import pprint

# Create constant/global variables #######
SHEETY_PRICES_ENDPOINT = (
    "https://api.sheety.co/17d8fefb19eab46bd53463191a3510a8/flightDeals/prices"
)

# Create DataManager class #######


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Returns all the sheet data from the destination"""

        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        # # Test: print the data
        # pprint(data)

        return self.destination_data

    def update_destination_codes(self):
        "Updates the IATA codes for each city in the sheet data"

        # Make a Put request and use the row id from sheet_data to update
        # the Goggle Sheet with the IATA codes.
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
            )
            print(response.text)
