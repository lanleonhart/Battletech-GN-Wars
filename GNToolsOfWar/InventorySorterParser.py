import json
import os

def read_and_sort_json_files(input_paths, output_file):
    inventory_data = []
    error_files = []

    for input_path in input_paths:
        for file_name in os.listdir(input_path):
            if file_name.startswith('.') or not file_name.endswith('.json'):
                continue

            file_path = os.path.join(input_path, file_name)

            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    # Check if 'Custom' and 'InventorySorter' exist
                    if 'Custom' in data and 'InventorySorter' in data['Custom']:
                        inventory_value = data['Custom']['InventorySorter']
                        if inventory_value.isdigit():
                            inventory_data.append((file_name, int(inventory_value)))
                        else:
                            print(f"'InventorySorter' in {file_name} is not a valid number.")
            except json.JSONDecodeError:
                error_files.append(file_name)

    # Sort by the 'InventorySorter' value
    inventory_data.sort(key=lambda x: x[1])

    with open(output_file, 'w') as file:
        for item in inventory_data:
            file.write(f"{item[0]}: {item[1]}\n")

    if error_files:
        print("Errors occurred with the following files:")
        for ef in error_files:
            print(ef)

    print(f"Total items sorted: {len(inventory_data)}")

# Usage
input_paths = [
    r'C:\Program Files (x86)\Steam\steamapps\common\BATTLETECH\Mods\GN Core\GNToolsOfWar\StreamingAssets\data\weapon',
    r'C:\Program Files (x86)\Steam\steamapps\common\BATTLETECH\Mods\GN Core\GNToolsOfWar\weapon'
]
output_file = r'C:\Program Files (x86)\Steam\steamapps\common\BATTLETECH\Mods\GN Core\GNToolsOfWar\sorted_inventory.txt'
read_and_sort_json_files(input_paths, output_file)
