import requests
import datetime
import json

class Nasa():
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError('NASA api key is required')
        self.api_key = api_key

    ## private method
    def __get_request_api(self, url_ext: str, params: dict | None):
        base_url = 'https://api.nasa.gov/'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        if params is None:
            params = {}
        params['api_key'] = self.api_key
        response = requests.get(url=f"{base_url}/{url_ext}", params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code, response.text)
            raise ValueError(f'Error fetching data from NASA API\n{response.text}\nStatus code: {response.status_code}')
        return None

    # return the Astronomy Picture of the Day nasa api request response in json
    def get_apod(self):
        date = datetime.datetime.now.strftime('%Y-%m-%d')
        params = {"hd": True,'thumbs': True, 'date': date}
        return self.__get_request_api('planetary/apod', params)