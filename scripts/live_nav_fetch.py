import requests
import pandas as pd
import os

# Folder to save downloaded CSV files
output_folder = "data/raw"

# Create the folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# AMFI Scheme Codes
schemes = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Fetch NAV data for each scheme
for scheme_name, scheme_code in schemes.items():

    print(f"\nFetching data for {scheme_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            # Convert NAV history to DataFrame
            nav_df = pd.DataFrame(data["data"])

            # Save CSV
            file_name = f"{scheme_name}.csv"
            file_path = os.path.join(output_folder, file_name)

            nav_df.to_csv(file_path, index=False)

            print(f"Saved: {file_name}")
            print(f"Records: {len(nav_df)}")

        else:
            print(f"Failed! Status Code: {response.status_code}")

    except Exception as e:
        print("Error:", e)

print("\nAll NAV files downloaded successfully!")