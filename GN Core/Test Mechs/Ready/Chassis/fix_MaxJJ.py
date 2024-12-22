import os
import json

def modify_max_jumpjets(folder_path="."):
    """
    Modifies the 'MaxJumpjets' field value to 20 for every JSON file in the specified folder.
    
    Args:
        folder_path (str): The path to the folder containing the JSON files. Defaults to the current folder.
    """
    print(f"Scanning for JSON files in: {folder_path}")
    
    json_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]
    
    if not json_files:
        print("No JSON files found in the folder. Exiting.")
        return

    for json_file in json_files:
        file_path = os.path.join(folder_path, json_file)
        try:
            # Load the JSON file
            print(f"Processing file: {json_file}")
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Modify the 'MaxJumpjets' field
            if "MaxJumpjets" in data:
                print(f"'MaxJumpjets' found in {json_file}. Updating value to 20.")
                data["MaxJumpjets"] = 20
            else:
                print(f"'MaxJumpjets' field not found in {json_file}. Skipping.")
                continue

            # Save the modified JSON file
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
                print(f"Updated 'MaxJumpjets' in {json_file}.")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in file {json_file}: {e}")
        except Exception as e:
            print(f"An error occurred while processing {json_file}: {e}")

if __name__ == "__main__":
    # Get the current working directory
    current_folder = os.path.dirname(os.path.realpath(__file__))
    print(f"Script running in: {current_folder}")
    
    modify_max_jumpjets(current_folder)
