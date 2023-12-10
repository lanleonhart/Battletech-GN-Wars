import json
import os

#Items to be used inside LancePool

EnemySpawnChance={
"Difficulty1" :[1, 0.20],
"Difficulty2" :[1, 0.20],
"Difficulty3" :[1, 0.20],
"Difficulty4" :[1, 0.20],
"Difficulty5" :[1, 0.20],
"Difficulty6" :[1, 0.25],
"Difficulty7" :[1, 0.35],
"Difficulty8" :[1, 0.35],
"Difficulty9" :[1, 0.35],
"Difficulty10" :[1, 0.35],
"Difficulty11" :[1, 0.50],
"Difficulty12" :[1, 0.50],
"Difficulty13" :[2, 0.50],
"Difficulty14" :[2, 0.50],
"Difficulty15" :[2, 0.50],
"Difficulty16" :[2, 0.50],
"Difficulty17" :[2, 0.55],
"Difficulty18" :[2, 0.55],
"Difficulty19" :[2, 0.55],
"Difficulty20" :[2, 0.60],
"Difficulty21" :[2, 0.60],
"Difficulty22" :[2, 0.60],
"Difficulty23" :[2, 0.65],
"Difficulty24" :[2, 0.65],
"Difficulty25" :[2, 0.65],
}
AllySpawnChance={
"Difficulty1" :[1, 0.20],
"Difficulty2" :[1, 0.20],
"Difficulty3" :[1, 0.20],
"Difficulty4" :[1, 0.20],
"Difficulty5" :[1, 0.20],
"Difficulty6" :[1, 0.25],
"Difficulty7" :[1, 0.35],
"Difficulty8" :[1, 0.35],
"Difficulty9" :[1, 0.35],
"Difficulty10" :[1, 0.35],
"Difficulty11" :[1, 0.50],
"Difficulty12" :[1, 0.50],
"Difficulty13" :[1, 0.50],
"Difficulty14" :[1, 0.50],
"Difficulty15" :[1, 0.50],
"Difficulty16" :[1, 0.50],
"Difficulty17" :[1, 0.55],
"Difficulty18" :[1, 0.55],
"Difficulty19" :[1, 0.55],
"Difficulty20" :[1, 0.60],
"Difficulty21" :[1, 0.60],
"Difficulty22" :[1, 0.60],
"Difficulty23" :[1, 0.65],
"Difficulty24" :[1, 0.65],
"Difficulty25" :[1, 0.65],
}

AlliedEliteSpawn={
"Difficulty1" : 0.20,
"Difficulty2" : 0.20,
"Difficulty3" : 0.20,
"Difficulty4" : 0.20,
"Difficulty5" : 0.20,
"Difficulty6" : 0.25,
"Difficulty7" : 0.25,
"Difficulty8" : 0.25,
"Difficulty9" : 0.25,
"Difficulty10" : 0.25,
"Difficulty11" : 0.26,
"Difficulty12" : 0.27,
"Difficulty13" : 0.28,
"Difficulty14" : 0.29,
"Difficulty15" : 0.30,
"Difficulty16" : 0.31,
"Difficulty17" : 0.32,
"Difficulty18" : 0.33,
"Difficulty19" : 0.34,
"Difficulty20" : 0.35,
"Difficulty21" : 0.36,
"Difficulty22" : 0.37,
"Difficulty23" : 0.38,
"Difficulty24" : 0.39,
"Difficulty25" : 0.40,
}
EnemyEliteSpawn={
"Difficulty1" : 0.20,
"Difficulty2" : 0.20,
"Difficulty3" : 0.20,
"Difficulty4" : 0.20,
"Difficulty5" : 0.20,
"Difficulty6" : 0.25,
"Difficulty7" : 0.25,
"Difficulty8" : 0.25,
"Difficulty9" : 0.25,
"Difficulty10" : 0.25,
"Difficulty11" : 0.26,
"Difficulty12" : 0.27,
"Difficulty13" : 0.28,
"Difficulty14" : 0.29,
"Difficulty15" : 0.30,
"Difficulty16" : 0.31,
"Difficulty17" : 0.32,
"Difficulty18" : 0.33,
"Difficulty19" : 0.34,
"Difficulty20" : 0.35,
"Difficulty21" : 0.36,
"Difficulty22" : 0.37,
"Difficulty23" : 0.38,
"Difficulty24" : 0.39,
"Difficulty25" : 0.40,   # "Generic_Light_Mixed_Lance" "Generic_Light_Vehicle_Lance"
}


LancePool = {
    "Difficulty1": ["Generic_Light_Battle_Lance", "Generic_Light_Battle_Lance","Generic_Light_Mixed_Lance","Generic_Light_Vehicle_Lance"],
    "Difficulty2": ["Generic_Light_Battle_Lance", "Generic_Light_Battle_Lance","Generic_Light_Mixed_Lance","Generic_Light_Vehicle_Lance"],
    "Difficulty3": ["Generic_Light_Battle_Lance", "Generic_Medium_Battle_Lance","Generic_Light_Mixed_Lance","Generic_Light_Vehicle_Lance","Generic_Medium_Mixed_Lance","Generic_Medium_Vehicle_Lance"],
    "Difficulty4": ["Generic_Light_Battle_Lance", "Generic_Medium_Battle_Lance","Generic_Medium_Mixed_Lance","Generic_Medium_Vehicle_Lance"],
    "Difficulty5": ["Generic_Medium_Battle_Lance", "Generic_Medium_Battle_Lance","Generic_Medium_Mixed_Lance","Generic_Medium_Vehicle_Lance"],
    "Difficulty6": ["Generic_Medium_Battle_Lance", "Generic_Medium_Battle_Lance","Generic_Medium_Mixed_Lance","Generic_Medium_Vehicle_Lance"],
    "Difficulty7": ["Generic_Medium_Battle_Lance", "Generic_Medium_Battle_Lance","Generic_Medium_Mixed_Lance","Generic_Medium_Vehicle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance"],
    "Difficulty8": ["Generic_Medium_Battle_Lance", "Generic_Heavy_Battle_Lance","Generic_Medium_Mixed_Lance","Generic_Medium_Vehicle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance"],
    "Difficulty9": ["Generic_Medium_Battle_Lance", "Generic_Heavy_Battle_Lance","Generic_Medium_Mixed_Lance","Generic_Medium_Vehicle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance"],
    "Difficulty10": ["Generic_Medium_Battle_Lance", "Generic_Heavy_Battle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance"],
    "Difficulty11": ["Generic_Medium_Battle_Lance", "Generic_Heavy_Battle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance"],
    "Difficulty12": ["Generic_Heavy_Battle_Lance", "Generic_Heavy_Battle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance"],
    "Difficulty13": ["Generic_Heavy_Battle_Lance", "Generic_Heavy_Battle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance","Generic_Assault_Mixed_Lance","Generic_Assault_Vehicle_Lance"],
    "Difficulty14": ["Generic_Heavy_Battle_Lance", "Generic_Heavy_Battle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance","Generic_Assault_Mixed_Lance","Generic_Assault_Vehicle_Lance"],
    "Difficulty15": ["Generic_Heavy_Battle_Lance", "Generic_Heavy_Battle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance","Generic_Assault_Mixed_Lance","Generic_Assault_Vehicle_Lance"],
    "Difficulty16": ["Generic_Assault_Battle_Lance", "Generic_Assault_Battle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance","Generic_Assault_Mixed_Lance","Generic_Assault_Vehicle_Lance"],
    "Difficulty17": ["Generic_Assault_Battle_Lance", "Generic_Assault_Battle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance","Generic_Assault_Mixed_Lance","Generic_Assault_Vehicle_Lance"],
    "Difficulty18": ["Generic_Assault_Battle_Lance", "Generic_Assault_Battle_Lance","Generic_Heavy_Mixed_Lance","Generic_Heavy_Vehicle_Lance","Generic_Assault_Mixed_Lance","Generic_Assault_Vehicle_Lance"],
    "Difficulty19": ["Generic_Assault_Battle_Lance", "Generic_Assault_Battle_Lance"],
    "Difficulty20": ["Generic_Assault_Battle_Lance", "Generic_Assault_Battle_Lance"],
    "Difficulty21": ["Generic_Assault_Battle_Lance", "Generic_Assault_Battle_Lance"],
    "Difficulty22": ["Generic_Assault_Battle_Lance", "Generic_Assault_Battle_Lance"],
    "Difficulty23": ["Generic_Assault_Battle_Lance", "Generic_Assault_Battle_Lance"],
    "Difficulty24": ["Generic_Assault_Battle_Lance", "Generic_Assault_Battle_Lance"],
    "Difficulty25": ["Generic_Assault_Battle_Lance", "Generic_Assault_Battle_Lance"]
}

template = {
    "IncludeContractTypes": [],
    "ExcludeContractTypes": [],
    "LancePool": {"ALL": []},
    "Enemy": {
        "Max": 0,
        "ExcludeContractTypes": [],
        "ChanceToSpawn": 0.4,
        "EliteLances": {
            "Conditions": ["IsEnemy"],
            "Suffix": "_Elite",
            "Overrides": {
                "ChanceToSpawn": 0.6
            }
        },
        "LancePool": {"ALL": []}
    },
    "Allies": {
        "Max": 1,
        "ChanceToSpawn": 0.5,
        "EliteLances": {
            "Conditions": ["IsAlly"],
            "Overrides": {
                "Max": 2,
                "ChanceToSpawn": 0.6
            }
        },
        "LancePool": {"ALL": []}
    }
}

# Iterate through the difficulty levels and fill in the template
current_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script

for difficulty_level in range(1, 26):
    difficulty_key = f"Difficulty{difficulty_level}"
    
    # Update the assignment for LancePool
    template["LancePool"]["ALL"] = LancePool[difficulty_key]
    template["Enemy"]["ChanceToSpawn"] = EnemySpawnChance[difficulty_key][1]
    template["Allies"]["ChanceToSpawn"] = AllySpawnChance[difficulty_key][1]
    template["Enemy"]["EliteLances"]["Overrides"]["ChanceToSpawn"] = EnemyEliteSpawn[difficulty_key]
    template["Allies"]["EliteLances"]["Overrides"]["ChanceToSpawn"] = AlliedEliteSpawn[difficulty_key]

    # Write the filled template to a JSON file for each difficulty level
    file_path = os.path.join(current_directory, f"Difficulty{difficulty_level}.json")
    with open(file_path, "w") as outfile:
        json.dump(template, outfile, indent=4)

print("JSON files generated successfully!")