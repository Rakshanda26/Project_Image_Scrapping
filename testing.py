import requests
import os
import platform

# Specify the ChromeDriver version and platform
chrome_driver_version = "88.0.4324.96"  # Replace with your desired version
system_platform = platform.system()
if system_platform == 'Windows':
    driver_filename = 'chromedriver_win32.zip'
    chrome_driver_download_url = f"https://chromedriver.storage.googleapis.com/{chrome_driver_version}/{driver_filename}"
elif system_platform == 'Linux':
    driver_filename = 'chromedriver_linux64.zip'
    chrome_driver_download_url = f"https://chromedriver.storage.googleapis.com/{chrome_driver_version}/{driver_filename}"
elif system_platform == 'Darwin':  # macOS
    driver_filename = 'chromedriver_mac64.zip'
    chrome_driver_download_url = f"https://chromedriver.storage.googleapis.com/{chrome_driver_version}/{driver_filename}"
else:
    raise Exception(f'Unsupported platform: {system_platform}')

# Set the directory where you want to save the ChromeDriver
download_directory = os.path.join(os.getcwd(), 'chromedriver')

# Create the download directory if it doesn't exist
os.makedirs(download_directory, exist_ok=True)

# Download the ChromeDriver zip file
response = requests.get(chrome_driver_download_url)
with open(os.path.join(download_directory, driver_filename), 'wb') as file:
    file.write(response.content)

# Print the downloaded ChromeDriver version
print(f'Downloaded ChromeDriver {chrome_driver_version} for {system_platform}')
