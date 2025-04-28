import csv
import os

weapons_list = [
     "Weapon_LRM_Thunderbolt10",
"Weapon_LRM_Thunderbolt15",
"Weapon_LRM_Thunderbolt20",
"Weapon_MachineGun_MachineGun_0-STOCK",
"Weapon_MachineGun_MachineGun_1-Brigadier",
"Weapon_MachineGun_MachineGun_1-VMI",
"Weapon_MachineGun_MachineGun_2-Brigadier",
"Weapon_MachineGun_MachineGun_2-VMI",
"Weapon_Mortar4",
"Weapon_Mortar6",
"Weapon_Mortar8",
"Weapon_MRM_MRM10",
"Weapon_MRM_MRM20",
"Weapon_MRM_MRM30",
"Weapon_MRM_MRM40",
"Weapon_AMS",
"Weapon_Autocannon_HeavyRifle",
"Weapon_Autocannon_HVAC2_0-STOCK",
"Weapon_Autocannon_HVAC5_0-STOCK",
"Weapon_Autocannon_HVAC10_0-STOCK",
"Weapon_Autocannon_HVAC20_0-STOCK",
"Weapon_Autocannon_LightRifle",
"Weapon_Autocannon_LONGTOM",
"Weapon_Autocannon_MediumRifle",
"Weapon_Autocannon_SNIPER",
"Weapon_Autocannon_THUMPER",
"Weapon_Gauss_Gauss_Silverbullet",
"Weapon_Gauss_Heavy_0-STOCK",
"Weapon_Gauss_ImprovedHeavy_0-STOCK",
"Weapon_Laser_AMS",
"Weapon_LRM_ArrowIV",
"Weapon_LRM_Thunderbolt5",
"Weapon_SRM_SRM4_1-Irian",
"Weapon_SRM_SRM4_2-Holly",
"Weapon_SRM_SRM4_2-Irian",
"Weapon_SRM_SRM4_2-Valiant",
"Weapon_SRM_SRM4_3-Valiant",
"Weapon_SRM_SRM4_Streak",
"Weapon_SRM_SRM6_0-STOCK",
"Weapon_SRM_SRM6_1-Holly",
"Weapon_SRM_SRM6_1-Irian",
"Weapon_SRM_SRM6_2-Holly",
"Weapon_SRM_SRM6_2-Irian",
"Weapon_SRM_SRM6_2-Valiant",
"Weapon_SRM_SRM6_3-Valiant",
"Weapon_SRM_SRM6_Streak",
"Weapon_Autocannon_AC2_0-STOCK",
"Weapon_Autocannon_AC2_1-Defiance",
"Weapon_Autocannon_AC2_1-Federated",
"Weapon_Autocannon_AC2_1-Kali_Yama",
"Weapon_Autocannon_AC2_1-Mydron",
"Weapon_Autocannon_AC2_2-Defiance",
"Weapon_Autocannon_AC2_2-Federated",
"Weapon_Autocannon_AC2_2-Imperator",
"Weapon_Autocannon_AC2_2-Kali_Yama",
"Weapon_Autocannon_AC2_2-Mydron",
"Weapon_Autocannon_AC2_3-Imperator",
"Weapon_Autocannon_AC5_0-STOCK",
"Weapon_Autocannon_AC5_1-Defiance",
"Weapon_Autocannon_AC5_1-Federated",
"Weapon_Autocannon_AC5_1-Imperator",
"Weapon_Autocannon_AC5_1-Kali_Yama",
"Weapon_Autocannon_AC5_2-Defiance",
"Weapon_Autocannon_AC5_2-Federated",
"Weapon_Autocannon_AC5_2-Imperator",
"Weapon_Autocannon_AC5_2-Kali_Yama",
"Weapon_Autocannon_AC5_2-Mydron",
"Weapon_Autocannon_AC5_3-Mydron",
"Weapon_Autocannon_AC10_0-STOCK",
"Weapon_Autocannon_AC10_1-Defiance",
"Weapon_Autocannon_AC10_1-Imperator",
"Weapon_Autocannon_AC10_1-Kali_Yama",
"Weapon_Autocannon_AC10_1-Mydron",
"Weapon_Autocannon_AC10_2-Defiance",
"Weapon_Autocannon_AC10_2-Federated",
"Weapon_Autocannon_AC10_2-Imperator",
"Weapon_Autocannon_AC10_2-Kali_Yama",
"Weapon_Autocannon_AC10_2-Mydron",
"Weapon_Autocannon_AC10_3-Federated",
"Weapon_Autocannon_AC20_0-STOCK",
"Weapon_Autocannon_AC20_1-Defiance",
"Weapon_Autocannon_AC20_1-Federated",
"Weapon_Autocannon_AC20_1-Imperator",
"Weapon_Autocannon_AC20_1-Mydron",
"Weapon_Autocannon_AC20_2-Defiance",
"Weapon_Autocannon_AC20_2-Federated",
"Weapon_Autocannon_AC20_2-Imperator",
"Weapon_Autocannon_AC20_2-Kali_Yama",
"Weapon_Autocannon_AC20_2-Mydron",
"Weapon_Autocannon_AC20_3-Kali_Yama",
"Weapon_Autocannon_AC20_SPECIAL-Victoria",
"Weapon_Autocannon_LB2X_0-STOCK",
"Weapon_Autocannon_LB2X_1-Defiance",
"Weapon_Autocannon_LB2X_2-Defiance",
"Weapon_Autocannon_LB5X_0-STOCK",
"Weapon_Autocannon_LB5X_1-GM",
"Weapon_Autocannon_LB5X_2-GM",
"Weapon_Autocannon_LB10X_0-STOCK",
"Weapon_Autocannon_LB10X_1-Western",
"Weapon_Autocannon_LB10X_2-Western",
"Weapon_Autocannon_LB20X_0-STOCK",
"Weapon_Autocannon_LB20X_1-Shengli_Arms",
"Weapon_Autocannon_LB20X_2-Shengli_Arms",
"Weapon_Autocannon_UAC2_0-STOCK",
"Weapon_Autocannon_UAC2_1-Imperator",
"Weapon_Autocannon_UAC2_2-Imperator",
"Weapon_Autocannon_UAC5_0-STOCK",
"Weapon_Autocannon_UAC5_1-Mydron",
"Weapon_Autocannon_UAC5_2-Mydron",
"Weapon_Autocannon_UAC10_0-STOCK",
"Weapon_Autocannon_UAC10_1-Federated",
"Weapon_Autocannon_UAC10_2-Federated",
"Weapon_Autocannon_UAC20_0-STOCK",
"Weapon_Autocannon_UAC20_1-Kali_Yama",
"Weapon_Autocannon_UAC20_2-Kali_Yama",
"Weapon_Flamer_Flamer_0-STOCK",
"Weapon_Flamer_Flamer_1-Hotshot",
"Weapon_Flamer_Flamer_2-Olympus",
"Weapon_Flamer_Flamer_SPECIAL-Victoria",
"Weapon_Gauss_Gauss_0-STOCK",
"Weapon_Gauss_Gauss_1-M7",
"Weapon_Gauss_Gauss_2-M9",
"Weapon_Laser_LargeLaser_0-STOCK",
"Weapon_Laser_LargeLaser_1-Diverse_Optics",
"Weapon_Laser_LargeLaser_1-ExoStar",
"Weapon_Laser_LargeLaser_1-Intek",
"Weapon_Laser_LargeLaser_2-Diverse_Optics",
"Weapon_Laser_LargeLaser_2-ExoStar",
"Weapon_Laser_LargeLaser_2-Intek",
"Weapon_Laser_LargeLaser_2-Magna",
"Weapon_Laser_LargeLaser_3-Magna",
"Weapon_Laser_LargeLaserER_0-STOCK",
"Weapon_Laser_LargeLaserER_1-Blankenburg25",
"Weapon_Laser_LargeLaserER_2-BlazeFire",
"Weapon_Laser_LargeLaserPulse_0-STOCK",
"Weapon_Laser_LargeLaserPulse_1-Thunderbolt12",
"Weapon_Laser_LargeLaserPulse_2-Exostar",
"Weapon_Laser_MediumLaser_0-STOCK",
"Weapon_Laser_MediumLaser_1-ExoStar",
"Weapon_Laser_MediumLaser_1-Intek",
"Weapon_Laser_MediumLaser_1-Magna",
"Weapon_Laser_MediumLaser_2-Diverse_Optics",
"Weapon_Laser_MediumLaser_2-ExoStar",
"Weapon_Laser_MediumLaser_2-Intek",
"Weapon_Laser_MediumLaser_2-Magna",
"Weapon_Laser_MediumLaser_3-Diverse_Optics",
"Weapon_Laser_MediumLaserER_0-STOCK",
"Weapon_Laser_MediumLaserER_1-MagnaVI",
"Weapon_Laser_MediumLaserER_2-BrightBloom",
"Weapon_Laser_MediumLaserPulse_0-STOCK",
"Weapon_Laser_MediumLaserPulse_1-RakerIV",
"Weapon_Laser_MediumLaserPulse_2-Magna400P",
"Weapon_Laser_SmallLaser_0-STOCK",
"Weapon_Laser_SmallLaser_1-Diverse_Optics",
"Weapon_Laser_SmallLaser_1-ExoStar",
"Weapon_Laser_SmallLaser_1-Magna",
"Weapon_Laser_SmallLaser_2-Diverse_Optics",
"Weapon_Laser_SmallLaser_2-ExoStar",
"Weapon_Laser_SmallLaser_2-Intek",
"Weapon_Laser_SmallLaser_2-Magna",
"Weapon_Laser_SmallLaser_3-Intek",
"Weapon_Laser_SmallLaserER_0-STOCK",
"Weapon_Laser_SmallLaserER_1-Diverse_Optics",
"Weapon_Laser_SmallLaserER_2-BlazeFire",
"Weapon_Laser_SmallLaserPulse_0-STOCK",
"Weapon_Laser_SmallLaserPulse_1-Maxell",
"Weapon_Laser_SmallLaserPulse_2-Magna200P",
"Weapon_LRM_LRM5_0-STOCK",
"Weapon_LRM_LRM5_1-Delta",
"Weapon_LRM_LRM5_1-LongFire",
"Weapon_LRM_LRM5_1-Telos",
"Weapon_LRM_LRM5_2-Delta",
"Weapon_LRM_LRM5_2-LongFire",
"Weapon_LRM_LRM5_2-Telos",
"Weapon_LRM_LRM5_2-Zeus",
"Weapon_LRM_LRM5_3-Zeus",
"Weapon_LRM_LRM10_0-STOCK",
"Weapon_LRM_LRM10_1-Delta",
"Weapon_LRM_LRM10_1-LongFire",
"Weapon_LRM_LRM10_1-Telos",
"Weapon_LRM_LRM10_2-Delta",
"Weapon_LRM_LRM10_2-LongFire",
"Weapon_LRM_LRM10_2-Telos",
"Weapon_LRM_LRM10_2-Zeus",
"Weapon_LRM_LRM10_3-Zeus",
"Weapon_LRM_LRM15_0-STOCK",
"Weapon_LRM_LRM15_1-Delta",
"Weapon_LRM_LRM15_1-LongFire",
"Weapon_LRM_LRM15_1-Telos",
"Weapon_LRM_LRM15_2-Delta",
"Weapon_LRM_LRM15_2-LongFire",
"Weapon_LRM_LRM15_2-Telos",
"Weapon_LRM_LRM15_2-Zeus",
"Weapon_LRM_LRM15_3-Zeus",
"Weapon_LRM_LRM20_0-STOCK",
"Weapon_LRM_LRM20_1-Delta",
"Weapon_LRM_LRM20_1-LongFire",
"Weapon_LRM_LRM20_1-Telos",
"Weapon_LRM_LRM20_2-Delta",
"Weapon_LRM_LRM20_2-LongFire",
"Weapon_LRM_LRM20_2-Telos",
"Weapon_LRM_LRM20_2-Zeus",
"Weapon_LRM_LRM20_3-Zeus",
"Weapon_PPC_PPC_0-STOCK",
"Weapon_PPC_PPC_1-Ceres_Arms",
"Weapon_PPC_PPC_1-Donal",
"Weapon_PPC_PPC_1-Tiegart",
"Weapon_PPC_PPC_2-Ceres_Arms",
"Weapon_PPC_PPC_2-Donal",
"Weapon_PPC_PPC_2-Tiegart",
"Weapon_PPC_PPCER_0-STOCK",
"Weapon_PPC_PPCER_1-MagnaFirestar",
"Weapon_PPC_PPCER_2-TiegartMagnum",
"Weapon_PPC_PPCSnub_0-STOCK",
"Weapon_PPC_PPCSnub_1-Ceres_Arms",
"Weapon_PPC_PPCSnub_1-Donal",
"Weapon_PPC_PPCSnub_1-Magna",
"Weapon_PPC_PPCSnub_2-Ceres_Arms",
"Weapon_PPC_PPCSnub_2-Donal",
"Weapon_PPC_PPCSnub_2-Magna",
"Weapon_SRM_SRM2_0-STOCK",
"Weapon_SRM_SRM2_1-Holly",
"Weapon_SRM_SRM2_1-Irian",
"Weapon_SRM_SRM2_2-Holly",
"Weapon_SRM_SRM2_2-Irian",
"Weapon_SRM_SRM2_2-Valiant",
"Weapon_SRM_SRM2_3-Valiant",
"Weapon_SRM_SRM2_Streak",
"Weapon_SRM_SRM4_0-STOCK",
"Weapon_SRM_SRM4_1-Holly"
]

exception_artillery = [
    "Weapon_Autocannon_LONGTOM",
    "Weapon_Autocannon_SNIPER",
    "Weapon_Autocannon_THUMPER",
    "Weapon_LRM_ArrowIV",
    "Weapon_Mortar4",
"Weapon_Mortar6",
"Weapon_Mortar8",
]

exception_rifles = [
    "Weapon_Autocannon_HeavyRifle",
    "Weapon_Autocannon_LightRifle",
    "Weapon_Autocannon_MediumRifle",
]

exception_ams = [
    "Weapon_AMS",
    "Weapon_Laser_AMS",
]
exception_support = [
    "Weapon_TAG_Standard_0-STOCK",
"Weapon_TAG_Standard_1-Mendham",
"Weapon_TAG_Standard_2-Ceres_Arms",
"Weapon_Narc_Standard_0-STOCK",
"Weapon_Narc_Standard_1-Ceres_Arms",
"Weapon_Narc_Standard_2-Kali_Yama",
],
exception_UAC = [
 "Weapon_Autocannon_UAC2_0-STOCK",
"Weapon_Autocannon_UAC2_1-Imperator",
"Weapon_Autocannon_UAC2_2-Imperator",
"Weapon_Autocannon_UAC5_0-STOCK",
"Weapon_Autocannon_UAC5_1-Mydron",
"Weapon_Autocannon_UAC5_2-Mydron",
"Weapon_Autocannon_UAC10_0-STOCK",
"Weapon_Autocannon_UAC10_1-Federated",
"Weapon_Autocannon_UAC10_2-Federated",
"Weapon_Autocannon_UAC20_0-STOCK",
"Weapon_Autocannon_UAC20_1-Kali_Yama",
"Weapon_Autocannon_UAC20_2-Kali_Yama",
],
exception_LBX = [
 "Weapon_Autocannon_LB2X_0-STOCK",
"Weapon_Autocannon_LB2X_1-Defiance",
"Weapon_Autocannon_LB2X_2-Defiance",
"Weapon_Autocannon_LB5X_0-STOCK",
"Weapon_Autocannon_LB5X_1-GM",
"Weapon_Autocannon_LB5X_2-GM",
"Weapon_Autocannon_LB10X_0-STOCK",
"Weapon_Autocannon_LB10X_1-Western",
"Weapon_Autocannon_LB10X_2-Western",
"Weapon_Autocannon_LB20X_0-STOCK",
"Weapon_Autocannon_LB20X_1-Shengli_Arms",
"Weapon_Autocannon_LB20X_2-Shengli_Arms"
],
exception_PulseLaser = [
 "Weapon_Laser_SmallLaserPulse_0-STOCK",
"Weapon_Laser_SmallLaserPulse_1-Maxell",
"Weapon_Laser_SmallLaserPulse_2-Magna200P",
"Weapon_Laser_MediumLaserPulse_0-STOCK",
"Weapon_Laser_MediumLaserPulse_1-RakerIV",
"Weapon_Laser_MediumLaserPulse_2-Magna400P",
"Weapon_Laser_LargeLaserPulse_0-STOCK",
"Weapon_Laser_LargeLaserPulse_1-Thunderbolt12",
"Weapon_Laser_LargeLaserPulse_2-Exostar",
]

categories = {}
for weapon in weapons_list:
    category = weapon.split("_")[1]  # Extract category name
    if weapon not in exception_artillery and weapon not in exception_rifles and weapon not in exception_ams:
        categories.setdefault(category, [])

# Add exceptions to categories manually
categories["Artillery"] = exception_artillery
categories["Rifles"] = exception_rifles
categories["Support"] = exception_support
categories["LBX"] = exception_LBX
categories["UAC"] = exception_UAC
categories["PulseLaser"] = exception_PulseLaser
categories["AMS"] = exception_ams

output_directory = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\BATTLETECH\\Mods\\GN Core\\DynamicShops\\Output\\"
os.makedirs(output_directory, exist_ok=True)

for weapon in weapons_list:
    category = weapon.split("_")[1]  # Extract category name

    if weapon in exception_artillery:
        categories.setdefault("Artillery", []).append(weapon)
    elif weapon in exception_rifles:
        categories.setdefault("Rifles", []).append(weapon)
    elif weapon in exception_LBX:
        categories.setdefault("LBX", []).append(weapon)
    elif weapon in exception_UAC:
        categories.setdefault("UAC", []).append(weapon)
    elif weapon in exception_PulseLaser:
        categories.setdefault("PulseLaser", []).append(weapon)
    elif weapon in exception_ams:
        categories.setdefault("AMS", []).append(weapon)
    elif weapon in exception_support:
        categories.setdefault("Support", []).append(weapon)
    else:
        if category not in categories.keys():
            categories[category] = []
        categories[category].append(weapon)

# Write each weapon entry individually with the correct format to CSV files
for category, weapons in categories.items():
    file_path = os.path.join(output_directory, f'GN_{category}.csv')
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Weapon', '1', '1'])  # Write headers for Weapon and values
        for weapon in weapons:
            csvwriter.writerow([weapon, 'Weapon', '1', '1'])  # Write weapon data in the same format
print("Files written successfully.")