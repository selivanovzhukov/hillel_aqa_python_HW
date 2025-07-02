import requests


url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}


try:
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    photos = data.get('photos')

    if photos:
        print(f'Found {len(photos)} photos')
        for photo in photos:
            img_url = photo.get('img_src')
            if img_url:
                try:
                    img_response = requests.get(img_url)
                    img_response.raise_for_status()

                    file_name = f'mars_{photo["id"]}.jpg'
                    with open(file_name, 'wb') as file:
                        file.write(img_response.content)
                    print(f'Downloaded {file_name}')
                except requests.exceptions.RequestException as e:
                    print(f"Failed to download from {img_url}: {e}")
            else:
                print(f"No photos found for {img_url}")
        print("\nDownload Complete")
    else:
        print("No photos found")

except requests.exceptions.RequestException as e:
    print(f"Error making request to {url}: {e}")
except ValueError:
    print("Error parsing JSON response")
except Exception as e:
    print(f"Unexpected error: {e}")