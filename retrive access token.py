import requests
import base64

# Your client ID and client secret
client_id = '061ee923532440bebc0a0e9d2c70087f'
client_secret = 'd62ccd0bb8434629a611155c55bf46e4'

# Encode client ID and client secret
client_credentials = f"{client_id}:{client_secret}"
client_credentials_b64 = base64.b64encode(client_credentials.encode()).decode()

# Spotify API URL for token
token_url = "https://accounts.spotify.com/api/token"

# Headers and data for POST request
headers = {
    "Authorization": f"Basic {client_credentials_b64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials"
}

# Make the POST request
response = requests.post(token_url, headers=headers, data=data)

# Check if the request was successful
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info['access_token']
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to get access token. Status code: {response.status_code}")
    print(response.json())
