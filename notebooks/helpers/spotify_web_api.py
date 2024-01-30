import requests
import time
import base64
import pickle
import os

CLIENT_ID = "dee2e80b810a4654a8f6b021582580bf"
CLIENT_SECRET = "76f0e40443d046058317e4c6412d478c"

URL_API = "https://api.spotify.com/v1/"
URL_ACCOUNTS = 'https://accounts.spotify.com/'

EP_TOKEN = 'api/token/'
EP_AUDIO_FEATURES = "audio-features/"

FILE_AUTH = 'spotify_auth_token.pkl'
DIR_CACHE = 'cached_files'

THRESH_EXPIRATION = 60

def get_track_features(track_ids: list[str]):

    auth_token = get_auth_token()

    headers = {
        'Authorization': 'Bearer ' + auth_token.token
    }

    url = URL_API + EP_AUDIO_FEATURES + '?ids=' + ','.join(track_ids)
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()


class SpotifyAuthToken:
    token: str
    expires_at: float

    def __init__(self, response: requests.models.Response):
        self.token = response.json()['access_token']
        self.expires_at = time.time() + int(response.json()['expires_in'])
        

def get_auth_token():

    os.makedirs(DIR_CACHE, exist_ok=True)
    path_auth_token = os.path.join(DIR_CACHE, FILE_AUTH)

    auth_token = None

    if os.path.exists(path_auth_token):
        with open(path_auth_token, 'rb') as file_auth_token:
            auth_token = pickle.load(file_auth_token)

    if (auth_token and auth_token.expires_at <= time.time() - THRESH_EXPIRATION)\
        or not auth_token:
        auth_token = api_request_auth_token()
    
        with open(path_auth_token, 'wb') as file_auth_token:
            pickle.dump(auth_token, file_auth_token)
    
    return auth_token
    

def api_request_auth_token():
    
    credentials = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode('utf-8')
    headers = {
        'Authorization': 'Basic ' + credentials
    }
    data = {
        'grant_type': 'client_credentials'
    }
    url = URL_ACCOUNTS + EP_TOKEN
    response = requests.post(url, headers=headers, data=data)

    return SpotifyAuthToken(response)
    