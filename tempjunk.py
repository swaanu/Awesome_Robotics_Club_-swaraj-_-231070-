# Define your string lists here
countries = [
    "UK", "USA", "Germany", "Saudi Arabia", "China", "Australia", "India",
    "Brazil", "Kazakhstan", "Canada", "Chile", "Peru", "Mexico",
    "Indonesia", "Japan", "South Korea"
]

parts = [
    "Shim Coils", "RF Coils", "Gradient Coil", "Patient Table", "PDU",
    "Gradient Amplifier", "RF Amplifier", "RF Receiver Assembly",
    "Image Reconstruction Computer", "Peripheral Devices", "MRI Safety System",
    "RF Shielding", "System Integration & Testing"
]

components = [
    # You can list all 42 components here in order
]

packaging_types = [
    "Fiberboard Boxes", "Plastic Drums", "Steel Drums", "Wooden Crates",
    "Vacuum-Sealed Foil Bags", "Anti-Static Bags", "Polyethylene Bags",
    "Bubble/Foam Wrap", "IBC Totes", "Cardboard Tubes",
    "Shrink-Wrapped Pallets", "Cushioned Metal Boxes", "Thermal Insulated Boxes"
]

labour_types = [
    "Unskilled", "Semi-Skilled", "Skilled", "Highly Skilled"
]

# Mapping function
def make_mapping(lst):
    return {name: idx + 1 for idx, name in enumerate(lst)}

# Generate mappings
I_map = make_mapping(countries)
J_map = make_mapping(parts)
R_map = make_mapping(components)  # Add actual list of 42 items
K_map = make_mapping(packaging_types)
M_map = make_mapping(labour_types)
D_map = I_map.copy()  # Destination countries same as `I`



Wi = {
    from_country: {to_country: 0 for to_country in countries}
    for from_country in countries
}

Zi = {
    "UK": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "USA": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Germany": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Saudi Arabia": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "China": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Australia": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "India": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.18, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Brazil": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.17, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Kazakhstan": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.12,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Canada": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Chile": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.19, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Peru": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Mexico": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Indonesia": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "Japan": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    },
    "South Korea": {
        "UK": 0.20, "USA": 0.00, "Germany": 0.19, "Saudi Arabia": 0.2075, "China": 0.13,
        "Australia": 0.10, "India": 0.2685, "Brazil": 0.3338, "Kazakhstan": 0.176,
        "Canada": 0.05, "Chile": 0.2614, "Peru": 0.18, "Mexico": 0.16,
        "Indonesia": 0.11, "Japan": 0.10, "South Korea": 0.10
    }
}

unit_to_kg_factor = {
    "Liquid helium (L)": 0.125,                 # kg per L
    "Epoxy resin (L)": 1.15,
    "De-ionized water (L)": 1.0,
    "EMI paint (L)": 1.6,
    "Silicon gel (L)": 0.97,
    "Teflon tape (m)": 0.04,
    "Kapton tape (m)": 0.02,
    "Fibre-optic cable (m)": 0.027,
    "RF coaxial (m)": 0.20,
    "PET sheet (m²)": 0.20,
    "Anti-bacterial vinyl (m²)": 0.30,
    "Capacitor (unit)": 0.03,
    "Non-magnetic motor (unit)": 2.5,
    "LED (unit)": 0.0035,
    "LCD monitor (unit)": 1.2,
    "Li-ion battery (unit)": 0.65,
    "Inductor (unit)": 0.10,
    "MOSFET / LDMOS / GaN / SiGe device (unit)": 0.006,
    "FGA / LC filter (unit)": 0.10,
    "VSWR device (unit)": 0.20,
    "Optical isolator (unit)": 0.15,
    "Gold (g)": 1 / 1000,                       # 1 g = 1/1000 kg
    "Magnet": 3500.0                            # kg per unit
}
unit_to_kg_factor = {
    "Magnets (superconducting)": 3500.0,                    # unit
    "Liquid Helium": 0.125,                                 # liters
    "Copper (Cu)": 1.0,                                     # already in kg
    "Aluminum (Al)": 1.0,                                   # kg
    "Niobium (Nb)": 1.0,
    "Titanium (Ti)": 1.0,
    "Capacitors": 0.03,                                     # units
    "Fiber Glass": 1.0,
    "Epoxy Resin": 1.15,                                    # liters
    "ABS Plastic": 1.0,
    "GaAs": 1 / 1000,                                       # grams → kg
    "316 Stainless Steel": 1.0,
    "Deionized Water": 1.0,                                 # liters
    "Teflon": 0.04,                                         # meters
    "Kapton Tape": 0.02,                                    # meters
    "Foam Damper": 1.0,
    "Plastic (misc.)": 1.0,
    "Polypropylene": 1.0,
    "Non-Magnetic Motors": 2.5,                             # units
    "Silicon Gel": 0.97,                                    # liters
    "Fiber Optic Wire": 0.027,                              # meters
    "PET Sheet": 0.20,                                      # m²
    "Anti-Bacterial Vinyl": 0.30,                           # m²
    "EMI Paint": 1.6,                                       # liters
    "LEDs": 0.0035,                                         # units
    "LCD Monitor": 1.2,                                     # unit
    "Li-ion Battery": 0.65,                                 # kg
    "Brass": 1.0,
    "Inductors": 0.10,                                      # units
    "MOSFETs": 0.006,                                       # units
    "FGA / FPGA": 0.10,                                     # units
    "LC Filters": 0.10,                                     # units
    "LDMOS": 0.006,                                         # units
    "GaN Chips": 0.006,                                     # units
    "SiGe BJTs (LNAs)": 0.006,                              # units
    "VSWR Modules": 0.20,                                   # units
    "RF Coaxial Cable": 0.20,                               # meters
    "SiGe Transistors (other)": 0.006,                      # units
    "Gold": 1 / 1000,                                       # grams → kg
    "Optical Isolators": 0.15,                              # units
    "Rubber": 1.0,
    "Galvanized Steel": 1.0
}

# === Insurance multipliers ===
Ki = [
    0.0040, 0.0035, 0.0040, 0.0055, 0.0030, 0.0035, 0.0060, 0.0065, 0.0075,
    0.0030, 0.0055, 0.0065, 0.0040, 0.0065, 0.0030, 0.0040
]

# === Setup overhead multipliers ===
Li = [
    2.5, 3.0, 2.8, 3.2, 2.0, 2.6, 2.4, 3.0, 3.1,
    2.7, 2.5, 2.5, 2.9, 2.3, 3.0, 2.8
]

# === Internal logistics + Labour multipliers ===
Si = [
    1.8, 2.4, 2.6, 2.8, 1.5, 1.9, 1.7, 2.5, 2.6,
    2.0, 1.8, 1.8, 2.3, 1.6, 2.5, 2.2
]

# === Uplift overhead multipliers ===
Zi = [
    1.1695, 1.2486, 1.0904, 1.2034, 1.3051, 1.1356, 1.0000, 1.3955,
    1.3390, 1.1582, 1.2938, 1.2260, 1.2712, 1.1808, 1.0678
]


from collections import defaultdict

# Define the parts and their corresponding components with quantities
part_component_mapping = {
    "Shim coils": {
        "Nb": 2.5, "Ti": 1.5, "Cu": 15, "Epoxy resin": 4, "ABS": 2
    },
    "RF coils": {
        "Cu": 10, "Capacitor": 2, "Fibre Glass": 5, "Epoxy Resin": 3,
        "ABS": 2, "Al": 1, "GaAs": 0.5, "RN-316": 0.2, "Nb": 0.8
    },
    "Gradient coil": {
        "Cu": 50, "Epoxy Resin": 3, "Deionized water": 20, "RN-316": 2
        # "12 hour" entry ignored as it's not a material
    },
    "Patient Table": {
        "Polypropylene": 10, "Non Magnetic motor": 1, "Silicon gel": 2,
        "Ti": 3, "Al": 2, "Steel": 8, "Fiber optic wire": 1,
        "PET Sheet": 2, "Anti-Bacterial Vinyl": 1, "Plastic": 1
    },
    "Operation Console": {
        "Steel": 8, "EMI Paint": 1, "Al": 2, "LCD Monitor": 2,
        "Li-ion battery": 1, "Capacitor": 2, "Cu": 5, "Inductor": 2,
        "Optical Fiber": 0.3, "Brass": 1, "LC Filters": 1
    },
    "PDU": {
        "Cu": 3, "Al": 2, "GAN Chips": 2, "FGA / FPGA": 1,
        "Ferrite": 1, "Steel": 2, "SiGe BJTs": 1
    },
    "Gradient Amplifier": {
        "MOSFETs": 6, "LDMOS": 3, "Cu": 8, "Al": 2,
        "SiGe Trans": 8, "FR-4": 6, "Kapton Tape": 20
    },
    "RFA": {
        "Cu": 4, "Poly Carbonate": 4, "GaAs": 0.12,
        "Optical isolator": 1, "Steel": 6, "Al": 4
    },
    "RF Receiver Assembly": {
        "Gold": 6, "Cu": 5, "Al": 4, "FR-4": 5, "Al": 4,
        "Brass": 3, "ABS": 2, "Kapton Tape": 2, "LEDs": 2,
        "Rubber": 6
    },
    "Image Reconst. Computer": {
        "Silicon": 0.12, "Cu": 4, "FR-4": 5, "Kapton Tape": 10,
        "ABS": 4, "LEDs": 2, "Brass": 3, "Plastic": 2
    },
    "Peripheral Devices": {
        "Ag/AgCl Electrodes": 0.5, "Optical Isolator": 1,
        "Rubber": 4, "Poly Carbonate": 4, "ABS": 2,
        "LEDs": 2, "Optical Fiber": 1
    },
    "MRI Safety System": {
        "Poly Carbonate": 4, "Steel": 6, "Cu": 5, "Brass": 3
    },
    "RF shielding": {
        "Galvanized Steel": 6, "Al": 4, "Brass": 3,
        "Steel": 5, "Kapton Tape": 2, "Plastic": 2
    }
}

# import ace_tools as tools; tools.display_dataframe_to_user(name="Part-Component Mapping", dataframe=part_component_mapping)

PRik = {
    "UK":           [0.15, 0.23, 0.3, 0.4, 0.45, 0.27, 0.1, 0.18, 0.24, 0.12, 0.08, 0.65, 0.5],
    "USA":          [0.15, 0.23, 0.3, 0.4, 0.45, 0.27, 0.1, 0.18, 0.2,  0.12, 0.08, 0.65, 0.5],
    "Germany":      [0.15, 0.23, 0.3, 0.4, 0.45, 0.27, 0.1, 0.18, 0.24, 0.12, 0.08, 0.65, 0.5],
    "Saudi Arabia": [0.15, 0.23, 0.3, 0.4, 0.54, 0.27, 0.1, 0.18, 0.2,  0.14, 0.08, 0.78, 0.60],
    "China":        [0.15, 0.23, 0.3, 0.4, 0.45, 0.27, 0.1, 0.18, 0.2,  0.12, 0.08, 0.65, 0.60],
    "Australia":    [0.15, 0.23, 0.3, 0.4, 0.45, 0.27, 0.1, 0.18, 0.24, 0.12, 0.08, 0.65, 0.5],
    "India":        [0.15, 0.23, 0.3, 0.4, 0.54, 0.27, 0.1, 0.18, 0.24, 0.14, 0.08, 0.78, 0.60],
    "Brazil":       [0.15, 0.23, 0.3, 0.4, 0.54, 0.27, 0.1, 0.18, 0.24, 0.12, 0.08, 0.78, 0.60],
    "Kazakhstan":   [0.15, 0.23, 0.3, 0.4, 0.54, 0.27, 0.1, 0.18, 0.24, 0.14, 0.08, 0.78, 0.60],
    "Canada":       [0.15, 0.23, 0.3, 0.4, 0.45, 0.27, 0.1, 0.18, 0.24, 0.12, 0.08, 0.65, 0.5],
    "Chile":        [0.15, 0.23, 0.3, 0.4, 0.54, 0.27, 0.1, 0.18, 0.24, 0.14, 0.08, 0.78, 0.60],
    "Peru":         [0.15, 0.23, 0.3, 0.4, 0.54, 0.27, 0.1, 0.18, 0.24, 0.14, 0.08, 0.78, 0.60],
    "Mexico":       [0.15, 0.23, 0.3, 0.4, 0.54, 0.27, 0.1, 0.18, 0.24, 0.14, 0.08, 0.78, 0.60],
    "Indonesia":    [0.15, 0.23, 0.3, 0.4, 0.54, 0.27, 0.1, 0.18, 0.24, 0.14, 0.08, 0.78, 0.60],
    "Japan":        [0.15, 0.23, 0.3, 0.4, 0.45, 0.27, 0.1, 0.18, 0.24, 0.12, 0.08, 0.65, 0.5],
    "South Korea":  [0.15, 0.23, 0.3, 0.4, 0.45, 0.27, 0.1, 0.18, 0.24, 0.12, 0.08, 0.65, 0.5],
}

ACi = {

    "USA": 16000,

    "Germany": 14400,

    "UK": 14080,

    "Japan": 14720,

    "South Korea": 13600,

    "Australia": 13920,

    "Saudi Arabia": 12800,

    "China": 10400,

    "Brazil": 9920,

    "India": 8000,

    "Mexico": 9280,

    "Vietnam": 8800,

    "Thailand": 8960,

    "Indonesia": 8480,

    "Poland": 11200,

    "Turkey": 10560

}


# Mapping of country names to integer indices for I: Countries (1 to 16)
country_index = {
    "UK": 1, "USA": 2, "Germany": 3, "Saudi Arabia": 4, "China": 5,
    "Australia": 6, "India": 7, "Brazil": 8, "Kazakhstan": 9, "Canada": 10,
    "Chile": 11, "Peru": 12, "Mexico": 13, "Indonesia": 14, "Japan": 15, "South Korea": 16
}

PMim = {
    1: {1: 12.2, 2: 15, 3: 22.5, 4: 40},
    2: {1: 10.5, 2: 15, 3: 22.5, 4: 40},
    3: {1: 12.8, 2: 17, 3: 26, 4: 45},
    4: {1: 4.5, 2: 6.5, 3: 11, 4: 21.5},
    5: {1: 3, 2: 5, 3: 10, 4: 17.5},
    6: {1: 15, 2: 19, 3: 26, 4: 40},
    7: {1: 0.8, 2: 1.75, 3: 4.25, 4: 10},
    8: {1: 2.5, 2: 4.25, 3: 7, 4: 13.5},
    9: {1: 1.5, 2: 3, 3: 5, 4: 10},
    10: {1: 14, 2: 18, 3: 24, 4: 40},
    11: {1: 4, 2: 5.5, 3: 9, 4: 13.5},
    12: {1: 2.5, 2: 3.5, 3: 6, 4: 10},
    13: {1: 4, 2: 5, 3: 8.5, 4: 14},
    14: {1: 1.5, 2: 2, 3: 4, 4: 8},
    15: {1: 10, 2: 12, 3: 16.5, 4: 30},
    16: {1: 7.2, 2: 9, 3: 13.5, 4: 25},
}
PMOim = {
    1: {1: 18.3, 2: 22.5, 3: 33.8, 4: 60},
    2: {1: 15.8, 2: 22.5, 3: 33.8, 4: 60},
    3: {1: 19.2, 2: 25.5, 3: 39, 4: 67.5},
    4: {1: 6.8, 2: 9.8, 3: 16.5, 4: 32.3},
    5: {1: 4.5, 2: 7.5, 3: 15, 4: 26.3},
    6: {1: 22.5, 2: 28.5, 3: 39, 4: 60},
    7: {1: 1.2, 2: 2.63, 3: 6.38, 4: 15},
    8: {1: 3.8, 2: 6.38, 3: 10.5, 4: 20.3},
    9: {1: 2.3, 2: 4.5, 3: 7.5, 4: 15},
    10: {1: 21, 2: 27, 3: 36, 4: 60},
    11: {1: 6, 2: 8.25, 3: 13.5, 4: 20.3},
    12: {1: 3.8, 2: 5.3, 3: 9, 4: 15},
    13: {1: 6, 2: 7.5, 3: 12.8, 4: 21},
    14: {1: 2.3, 2: 3, 3: 6, 4: 12},
    15: {1: 15, 2: 18, 3: 24.8, 4: 45},
    16: {1: 10.8, 2: 13.5, 3: 20.3, 4: 37.5},
}
ICim = PMim.copy()
OCim = PMOim.copy()


Tr = [
    [0.0, 6.9, 0.65, 5.0, 9.2, 17.0, 7.9, 9.4, 5.6, 5.7, 11.6, 10.3, 8.8, 11.7, 9.6, 8.9],
    [6.9, 0.0, 7.3, 11.2, 11.6, 14.5, 13.4, 7.8, 11.1, 1.3, 8.2, 5.9, 1.8, 15.6, 10.6, 10.7],
    [0.65, 7.3, 0.0, 4.4, 8.7, 16.2, 7.2, 9.9, 4.5, 6.4, 12.0, 10.8, 9.4, 11.3, 9.2, 8.6],
    [5.0, 11.2, 4.4, 0.0, 7.3, 12.2, 4.3, 12.0, 3.5, 11.3, 14.0, 13.3, 14.0, 8.1, 8.5, 7.7],
    [9.2, 11.6, 8.7, 7.3, 0.0, 8.0, 2.3, 17.8, 4.3, 10.2, 19.1, 18.0, 14.3, 4.5, 1.8, 0.85],
    [17.0, 14.5, 16.2, 12.2, 8.0, 0.0, 7.9, 13.4, 10.6, 15.5, 11.2, 12.6, 13.2, 5.5, 7.1, 8.1],
    [7.9, 13.4, 7.2, 4.3, 2.3, 7.9, 0.0, 15.4, 2.6, 12.3, 17.0, 17.0, 14.5, 2.3, 5.3, 4.2],
    [9.4, 7.8, 9.9, 12.0, 17.8, 13.4, 15.4, 0.0, 15.0, 8.1, 2.6, 3.1, 7.6, 16.2, 18.6, 18.2],
    [5.6, 11.1, 4.5, 3.5, 4.3, 10.6, 2.6, 15.0, 0.0, 10.0, 17.2, 17.1, 14.1, 5.2, 5.7, 5.1],
    [5.7, 1.3, 6.4, 11.3, 10.2, 15.5, 12.3, 8.1, 10.0, 0.0, 9.5, 7.0, 3.6, 14.7, 10.1, 10.0],
    [11.6, 8.2, 12.0, 14.0, 19.1, 11.2, 17.0, 2.6, 17.2, 9.5, 0.0, 2.5, 6.7, 16.3, 18.3, 18.6],
    [10.3, 5.9, 10.8, 13.3, 18.0, 12.6, 17.0, 3.1, 17.1, 7.0, 2.5, 0.0, 5.2, 16.4, 17.6, 18.0],
    [8.8, 1.8, 9.4, 14.0, 14.3, 13.2, 14.5, 7.6, 14.1, 3.6, 6.7, 5.2, 0.0, 16.6, 12.2, 12.6],
    [11.7, 15.6, 11.3, 8.1, 4.5, 5.5, 2.3, 16.2, 5.2, 14.7, 16.3, 16.4, 16.6, 0.0, 5.9, 4.5],
    [9.6, 10.6, 9.2, 8.5, 1.8, 7.1, 5.3, 18.6, 5.7, 10.1, 18.3, 17.6, 12.2, 5.9, 0.0, 1.2],
    [8.9, 10.7, 8.6, 7.7, 0.85, 8.1, 4.2, 18.2, 5.1, 10.0, 18.6, 18.0, 12.6, 4.5, 1.2, 0.0]
]


Trs = [
    [0.0, 0.177, 0.0255, 0.186, 0.57, 0.69, 0.483, 0.288, 0.237, 0.516, 0.387, 0.399, 0.408, 0.525, 0.6, 0.588],
    [0.177, 0.0, 0.192, 0.348, 0.606, 0.72, 0.639, 0.222, 0.408, 0.249, 0.276, 0.231, 0.138, 0.618, 0.66, 0.642],
    [0.0255, 0.192, 0.0, 0.168, 0.552, 0.675, 0.462, 0.309, 0.222, 0.51, 0.408, 0.42, 0.417, 0.516, 0.582, 0.57],
    [0.186, 0.348, 0.168, 0.0, 0.378, 0.525, 0.171, 0.432, 0.12, 0.594, 0.516, 0.504, 0.528, 0.321, 0.39, 0.381],
    [0.57, 0.606, 0.552, 0.378, 0.0, 0.21, 0.168, 0.714, 0.276, 0.288, 0.561, 0.552, 0.51, 0.093, 0.057, 0.048],
    [0.69, 0.72, 0.675, 0.525, 0.21, 0.0, 0.249, 0.57, 0.411, 0.408, 0.333, 0.393, 0.447, 0.165, 0.219, 0.24],
    [0.483, 0.639, 0.462, 0.171, 0.168, 0.249, 0.0, 0.654, 0.0, 0.567, 0.621, 0.612, 0.612, 0.0945, 0.1944, 0.1833],
    [0.288, 0.222, 0.309, 0.432, 0.714, 0.57, 0.654, 0.0, 0.519, 0.474, 0.102, 0.132, 0.186, 0.705, 0.744, 0.735],
    [0.237, 0.408, 0.222, 0.12, 0.276, 0.411, 0.0, 0.519, 0.0, 0.459, 0.567, 0.558, 0.528, 0.306, 0.348, 0.333],
    [0.516, 0.249, 0.51, 0.594, 0.288, 0.408, 0.567, 0.474, 0.459, 0.0, 0.42, 0.414, 0.246, 0.429, 0.342, 0.348],
    [0.387, 0.276, 0.408, 0.516, 0.561, 0.333, 0.621, 0.102, 0.567, 0.42, 0.0, 0.045, 0.189, 0.534, 0.594, 0.585],
    [0.399, 0.231, 0.42, 0.504, 0.552, 0.393, 0.612, 0.132, 0.558, 0.414, 0.045, 0.0, 0.174, 0.549, 0.579, 0.576],
    [0.408, 0.138, 0.417, 0.528, 0.51, 0.447, 0.612, 0.186, 0.528, 0.246, 0.189, 0.174, 0.0, 0.516, 0.552, 0.558],
    [0.525, 0.618, 0.516, 0.321, 0.093, 0.165, 0.0945, 0.705, 0.306, 0.429, 0.534, 0.549, 0.516, 0.0, 0.165, 0.156],
    [0.6, 0.66, 0.582, 0.39, 0.057, 0.219, 0.1944, 0.744, 0.348, 0.342, 0.594, 0.579, 0.552, 0.165, 0.0, 0.042],
    [0.588, 0.642, 0.57, 0.381, 0.048, 0.24, 0.1833, 0.735, 0.333, 0.348, 0.585, 0.576, 0.558, 0.156, 0.042, 0.0]
]


D_labour=30
D_assem=30
M_qty=10
M_day=500
M_people=100
