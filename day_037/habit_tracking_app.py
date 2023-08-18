"""
Habit Tracking Project by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules/libraries ######################################################################################################
import os
import requests
from datetime import datetime as dt

# Declare constant variables ###########################################################################################################
USER = os.environ.get("USER")
TOKEN = os.environ.get("TOKEN")


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_PARAMETERS = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

GRAPH_ID = "workout-graph1"

# Main #################################################################################################################################

# Perform a POST request by setting up an account in Pixela
# user_response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMETERS)
# print(user_response.text)

# # Create a graph definition
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Workout Minutes Graph",
#     "unit": "min",
#     "type": "float",
#     "color": "momiji",
# }
#
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
# print(graph_response.text)

# Get today's date in this format: yyyyMMdd
# date = dt(year=2023, month=3, day=30)
today = dt.now()
date = today

# Post values to the graph
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("How long was your workout today?"),
}

pixel_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=HEADERS)
print(pixel_response.text)

# # Updating a pixel
# pixel_update_endpoint = f'{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}/{date.strftime("%Y%m%d")}'
#
# pixel_update_data = {
#     "quantity": "1",
# }
#
# pixel_update_response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=HEADERS)
# print(pixel_update_response.text)
#
# # Deleting a pixel
# pixel_delete_response = requests.delete(url=pixel_update_endpoint, headers=HEADERS)
# print(pixel_delete_response.text)
