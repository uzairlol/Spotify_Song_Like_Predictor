import requests
import pandas as pd
import re

# Function to extract track ID from URL
def extract_track_id(track_url):
    match = re.search(r'track/([a-zA-Z0-9]+)', track_url)
    if match:
        return match.group(1)
    else:
        print(f"Invalid track URL: {track_url}. Please provide a valid Spotify track URL.")
        return None

# Function to get song attributes from Spotify
def get_song_attributes(track_id, access_token):
    # Construct the track URL
    track_url = f"https://api.spotify.com/v1/audio-features/{track_id}"

    # Headers for the GET request
    headers = {
        "Authorization": f"Bearer BQBvyxTlpdg_LY1E818sn9Rqnq07YX9SmJJJCoeIPBQhxoWwXItZOEzykukrpIH_x49hwZhuPKMJ_T05xUdehoXLBeCM9pwzOWKIvnQqL78w4Iiwa9g"
    }

    # Make the GET request
    response = requests.get(track_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get track attributes. Status code: {response.status_code}")
        print(response.json())
        return None

# Function to save song attributes to CSV
def save_song_attributes_to_csv(song_attributes, file_name):
    # Convert to DataFrame
    df = pd.DataFrame(song_attributes)

    # Save to CSV in append mode without headers
    df.to_csv(file_name, mode='a', index=False, header=not pd.io.common.file_exists(file_name))
    print(f"Song attributes saved to {file_name}")

# Main function
def main():
    # Access token (replace with your actual access token)
    access_token = 'your_access_token'

    # Track URL input (comma-separated)
    track_urls = input("Enter the Spotify track URLs (comma-separated): ")

    # Split the input into a list of URLs
    track_urls_list = track_urls.split(',')

    # Initialize a list to hold all song attributes
    all_song_attributes = []

    for track_url in track_urls_list:
        # Extract track ID from URL
        track_id = extract_track_id(track_url.strip())

        if track_id:
            # Get song attributes
            song_attributes = get_song_attributes(track_id, access_token)

            if song_attributes:
                # Select relevant attributes
                attributes = {
                    'acousticness': song_attributes['acousticness'],
                    'danceability': song_attributes['danceability'],
                    'duration_ms': song_attributes['duration_ms'],
                    'energy': song_attributes['energy'],
                    'instrumentalness': song_attributes['instrumentalness'],
                    'key': song_attributes['key'],
                    'liveness': song_attributes['liveness'],
                    'loudness': song_attributes['loudness'],
                    'mode': song_attributes['mode'],
                    'speechiness': song_attributes['speechiness'],
                    'tempo': song_attributes['tempo'],
                    'time_signature': song_attributes['time_signature'],
                    'valence': song_attributes['valence']
                }
                all_song_attributes.append(attributes)

    if all_song_attributes:
        # Save all song attributes to CSV
        save_song_attributes_to_csv(all_song_attributes, 'song_attributes.csv')

# Run the main function
if __name__ == "__main__":
    main()
