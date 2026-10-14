import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Configuration and endpoints
PIXELA_ENDPOINT ="https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"

HEADERS = {
    'X-USER-TOKEN': TOKEN
}

def create_user() -> None:
    """Registers a new account with the Pixela API (run once)."""
    user_params = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes',
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print("User creation response: ", response.text)


def create_graph() -> None:
    """Creates a new habit tracking graph definition (run once)."""
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    graph_config = {
        'id': GRAPH_ID,
        'name': 'Study Graph',
        'unit': 'Hr',
        'type': 'float',
        'color': 'ajisai',
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print("Graph creation response: ", response.text)

url = "https://pixe.la/v1/users/yashcontractor04/graphs/graph1.html"

today = datetime.today().strftime('%Y%m%d')

def post_pixel(date: str, quantity: str) -> None:
    """Records a new daily habit entry (POST)."""
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_config = {
        'date': date,
        'quantity': quantity,
    }
    response = requests.post(pixel_endpoint, json=pixel_config, headers=HEADERS)
    print("Post pixel response: ", response.text)

def update_pixel(date: str, quantity: str) -> None:
    """Updates an existing entry on a specific date (PUT)."""
    update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    data_config = {
        'quantity': quantity,
    }
    response = requests.put(url=update_endpoint, json=data_config, headers=HEADERS)
    print("Update pixel response: ", response.text)

def delete_pixel(date: str) -> None:
    """Deletes an entry on a specific date (DELETE)."""
    delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    response = requests.delete(url=delete_endpoint, headers=HEADERS)
    print("Delete pixel response: ", response.text)


if __name__ == "__main__":
    today = datetime.now().strftime('%Y%m%d')

    # Active habit logging:
    post_pixel(date=today, quantity='2.5')

    # Example operational endpoints:
    # update_pixel(date=today, quantity='3.0')
    # delete_pixel(date=today)

    print(f"View graph live at: https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html")