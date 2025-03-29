import os
import json

# Define the directories for source and target JSON files
source_directories = [
    r"C:\Users\Silver\Documents\GitHub\White-Fire\BattleTech-Advanced\Heavy Metal Unit Module\mech",
    r"C:\Users\Silver\Documents\GitHub\White-Fire\BattleTech-Advanced\Urban Warfare Unit Module\mech",
    r"C:\Users\Silver\Documents\GitHub\White-Fire\BattleTech-Advanced\Flashpoint Unit Module\mech",
    r"C:\Users\Silver\Documents\GitHub\White-Fire\BattleTech-Advanced\BT Advanced Mechs\mech"
]
target_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "StreamingAssets", "data", "mech")

# Function to load a JSON file
def load_json(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file {filepath}: {e}")
        return None

# Function to save a JSON file
def save_json(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

# Function to find the matching source file and extract the ComponentDefID
def get_component_def_id_from_source(filename):
    for source_directory in source_directories:
        source_path = os.path.join(source_directory, filename)
        if os.path.exists(source_path):
            source_data = load_json(source_path)
            if source_data and "inventory" in source_data:
                for item in source_data["inventory"]:
                    # Assuming we're looking for a HeatSink component
                    if item.get("ComponentDefType") == "HeatSink":
                        return item.get("ComponentDefID")
    return None

# Function to check and add the missing block
def check_and_add_missing_block(inventory, component_def_id):
    for item in inventory:
        if item.get("ComponentDefID") == component_def_id:
            return False  # Block already present, no need to add
    # Block not found, so we add the new block with the component_def_id
    new_block = {
        "MountedLocation": "CenterTorso",
        "ComponentDefID": component_def_id,
        "SimGameUID": None,
        "ComponentDefType": "HeatSink",
        "HardpointSlot": -1,
        "GUID": None,
        "DamageLevel": "Functional",
        "prefabName": None,
        "hasPrefabName": False
    }
    inventory.append(new_block)
    return True

# Function to process the target JSON files
def process_json_files(target_directory):
    for filename in os.listdir(target_directory):
        if filename.endswith(".json"):
            filepath = os.path.join(target_directory, filename)
            data = load_json(filepath)

            if data is None:
                continue  # Skip files with JSON errors

            # Ensure the 'inventory' section exists in the target file
            if "inventory" in data:
                # Get the component_def_id from the source files
                component_def_id = get_component_def_id_from_source(filename)
                if component_def_id:
                    # Check if the block is missing and add it if necessary
                    if check_and_add_missing_block(data["inventory"], component_def_id):
                        print(f"Fixed missing block in {filename}   {component_def_id}")
                        save_json(filepath, data)
                    else:
                        print(f"No missing block found in {filename}")
                else:
                    print(f"ComponentDefID not found for {filename}")

# Process all JSON files in the target directory
process_json_files(target_directory)
