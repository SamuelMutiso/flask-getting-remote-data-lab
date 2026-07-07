import requests
import json

class GetRequester:

    def __init__(self, url):
        # Store the target API URL when the class instance is created
        self.url = url

    def get_response_body(self):
        """
        Sends an HTTP GET request to the initialized URL 
        and returns the raw response content in bytes.
        """
        response = requests.get(self.url)
        
        # .content returns the raw response body as bytes (e.g., b"...")
        return response.content

    def load_json(self):
        """
        Sends an HTTP GET request to the initialized URL
        and parses the response text directly into Python dictionaries/lists.
        """
        response = requests.get(self.url)
        
        # .json() automatically decodes the JSON payload into Python objects
        return response.json()