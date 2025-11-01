import requests

def spacex_latest():
    # API url for the latest SpaceX launch
    url = "https://api.spacexdata.com/v5/launches/latest"
    
    #fetches the data from the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract mission name and date
        mission_name = data.get("name", "N/A")
        launch_date = data.get("date_utc", "N/A")

        # Get rocket ID and fetch rocket details
        rocket_id = data.get("rocket", None)
        rocket_name = "Unknown"

        if rocket_id:
            rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
            rocket_response = requests.get(rocket_url)
            if rocket_response.status_code == 200:
                rocket_data = rocket_response.json()
                rocket_name = rocket_data.get("name", "N/A")

        # Print results
        print(f"Mission Name: {mission_name}")
        print(f"Launch Date: {launch_date[:10]}")
        print(f"Rocket Name: {rocket_name}")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)



spacex_latest()
