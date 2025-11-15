import os
import re
import random

star_systems_path = r"E:\SteamLibrary\steamapps\common\BATTLETECH\Mods\InnerSphereMap\StarSystems"

# Define valid replacements based on available sprites
replacements = {
    '"planet_climate_tropical"': [f'"planet_climate_tropical{i}"' for i in range(1, 20)],
    '"planet_climate_terran"': [f'"planet_climate_terran{i}"' for i in range(2, 49)],
    '"planet_climate_arctic"': [f'"planet_climate_arctic{i}"' for i in range(1, 17)],
    '"planet_climate_desert"': [f'"planet_climate_desert{i}"' for i in list(range(1, 19)) + list(range(20, 22))],
    '"planet_climate_water"': [f'"planet_climate_water{i}"' for i in range(1, 17)],
    '"planet_climate_lunar"': [f'"planet_climate_lunar{i}"' for i in range(1, 23)],
    '"planet_climate_martian"': [f'"planet_climate_mars{i}"' for i in range(1, 14)],
    '"planet_climate_rocky"': [f'"planet_climate_rocky{i}"' for i in range(1, 20)],
}

files_processed = 0
replacements_made = 0

for filename in os.listdir(star_systems_path):
    if filename.endswith('.json'):
        filepath = os.path.join(star_systems_path, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        file_changed = False
        
        for old_tag, new_tags in replacements.items():
            if old_tag in content:
                new_tag = random.choice(new_tags)
                content = content.replace(old_tag, new_tag)
                file_changed = True
                replacements_made += 1
        
        if file_changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            files_processed += 1

print(f"Processed {files_processed} files")
print(f"Made {replacements_made} replacements")
print("Done!")
