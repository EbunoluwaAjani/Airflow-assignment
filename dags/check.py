import requests
import os

def download_specific_file(download_dir='downloads'):
    """Download a specific pageviews file."""
    os.makedirs(download_dir, exist_ok=True)  # Create the directory if it doesn't exist
    print(f"{download_dir} created!!")


    file_url = "https://dumps.wikimedia.org/other/pageviews/2024/2024-10/pageviews-20241001-010000.gz"
    file_name = os.path.join(download_dir, file_url.split("/")[-1])  # Save in the specified directory
    response = requests.get(file_url)
    print("Request successful!")
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            print("Writing into file!")
            f.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download {file_name}: {response.status_code}")

# Example usage
download_specific_file()  