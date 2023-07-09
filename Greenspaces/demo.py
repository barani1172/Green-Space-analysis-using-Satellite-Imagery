import requests
from PIL import Image
from io import BytesIO

# Replace with your own Mapbox access token
access_token = "pk.eyJ1IjoiMWJ5dGUiLCJhIjoiY2xmemk0amYzMGYxODNvbXQ1dm1kNDhldiJ9.RcfNvWx-fmn4UiGbkvokRw"

x, y = 7, 7
c_lon, c_lat, zoom = 76.7821, 30.7466, 15.83
lon, lat = c_lon-(int(x/2)*0.0100), c_lat-(int(y/2)*0.0050)

for i in range(x):
    lat = c_lat-(int(y/2)*0.0050)
    for j in range(y):
        url = f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{lon},{lat},{zoom},0/600x400?access_token=pk.eyJ1IjoiMWJ5dGUiLCJhIjoiY2xmemk0amYzMGYxODNvbXQ1dm1kNDhldiJ9.RcfNvWx-fmn4UiGbkvokRw"
        response = requests.get(url)

        if response.status_code == 200:
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            image.save(f"D:/Datasets/Satellite images/chandigarh{i+1}{j+1}.jpg")
        else:
            print(f"Request failed with status code {response.status_code}")

        lat += 0.0050
    lon += 0.0100