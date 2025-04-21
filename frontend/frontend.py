import time
import requests

backend_url = "http://backend-container:5000"

while True:
    try:
        response = requests.get(backend_url)
        if response.status_code == 200:
            print("Frontend received the following response from the backend:")
            print(response.text)
        else:
            print("Backend returned an unexpected status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Failed to communicate with the backend. Error:", e)
    
    time.sleep(10)  # wait for 10 seconds before the next request
