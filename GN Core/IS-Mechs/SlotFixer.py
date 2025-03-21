import os
import json

# Define the mapping of InventorySlots for each Location
mapping = {
    "Head": 6,
    "CenterTorso": 16,
    "RightTorso": 12,
    "LeftTorso": 12,
    "RightArm": 12,
    "LeftArm": 12,
    "RightLeg": 6,
    "LeftLeg": 6
}

# Set the directory containing the scripts to the directory of this script
scripts_dir = os.path.dirname(os.path.abspath(__file__))

# Walk through the scripts directory and its subdirectories
for root, dirs, files in os.walk(scripts_dir):
    for file in files:
        if file.endswith(".json"):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file {filepath}: {e}")
                continue

            # Check if the JSON data contains "Locations"
            if "Locations" in data and isinstance(data["Locations"], list):
                locations_changed = False
                for location in data["Locations"]:
                    location_name = location.get("Location")
                    if location_name in mapping:
                        old_value = location.get("InventorySlots")
                        new_value = mapping[location_name]
                        if old_value != new_value:
                            location["InventorySlots"] = new_value
                            locations_changed = True
                            print(f"Updated InventorySlots for {location_name} in file {filepath}")
                # Write the changes back to the file if any modifications were made
                if locations_changed:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=4)
            else:
                print(f"No 'Locations' key found in file {filepath}")
