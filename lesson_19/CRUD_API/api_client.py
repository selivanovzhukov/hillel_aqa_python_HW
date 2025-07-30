import requests
import os

BASE_URL = 'http://127.0.0.1:8080'
IMAGE_FILENAME = 'test_image.jpg'
IMAGE_FILE_PATH = os.path.join('.', IMAGE_FILENAME)


def create_dummy_image_file():
    try:
        with open(IMAGE_FILE_PATH, 'w') as f:
            f.write("Test image.")
        print(f"Creating test image file: '{IMAGE_FILE_PATH}'")
    except IOError as e:
        print(f"ERROR while creating test image file: {e}")
        exit()



def cleanup_dummy_file():

    if os.path.exists(IMAGE_FILE_PATH):
        os.remove(IMAGE_FILE_PATH)
        print(f"Deleting test image file: '{IMAGE_FILE_PATH}'")



def main():
    create_dummy_image_file()

    uploaded_filename = None

    try:

        print("\n--- 1. Downloading image ---")
        upload_url = f"{BASE_URL}/upload"
        with open(IMAGE_FILE_PATH, 'rb') as f:
            files = {'image': (IMAGE_FILENAME, f, 'image/jpg')}
            response_upload = requests.post(upload_url, files=files)

        response_upload.raise_for_status()

        if response_upload.status_code == 201:
            upload_data = response_upload.json()
            image_url = upload_data.get('image_url')
            print(f"✅ Downloading successful!")
            print(f"   Server response: {upload_data}")
            uploaded_filename = os.path.basename(image_url)
        else:
            print(f"❌ Cannot download image. Status: {response_upload.status_code}")
            return


        print(f"\n--- 2. Getting information about image '{uploaded_filename}' ---")
        get_url = f"{BASE_URL}/image/{uploaded_filename}"
        headers = {'Content-Type': 'text'}
        response_get = requests.get(get_url, headers=headers)
        response_get.raise_for_status()

        if response_get.status_code == 200:
            get_data = response_get.json()
            print(f"✅ Information about image '{uploaded_filename}' retrieved successfully!")
            print(f"   Server response: {get_data}")
        else:
            print(f"❌ Cannot retrieve information about image. Status: {response_get.status_code}")


        print(f"\n--- 3. Image deletion '{uploaded_filename}' ---")
        delete_url = f"{BASE_URL}/delete/{uploaded_filename}"
        response_delete = requests.delete(delete_url)
        response_delete.raise_for_status()

        if response_delete.status_code == 200:
            delete_data = response_delete.json()
            print(f"✅ Image '{uploaded_filename}' deleted successfully!")
            print(f"   Server response: {delete_data}")
        else:
            print(f"❌ Cannot delete image. Status: {response_delete.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error during request: {e}")
    finally:
        cleanup_dummy_file()


if __name__ == "__main__":
    try:
        requests.get(BASE_URL, timeout=3)
    except requests.exceptions.ConnectionError:
        print(f"Error: Cannot connect to server {BASE_URL}.")
    else:
        main()
