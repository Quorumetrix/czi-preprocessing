#czi_preprocessing.py

import os
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from tqdm import tqdm
import tifffile 
import czifile 
from aicsimageio import AICSImage 


def ask_file_path():
    root = tk.Tk()
    root.withdraw() # Hide the main window
    file_path = filedialog.askopenfilename(title="Select a .czi file")
    return file_path

def ask_folder_path():
    root = tk.Tk()
    root.withdraw() # Hide the main window
    folder_path = filedialog.askdirectory(title="Select export folder")
    return folder_path

# Use filedialog to ask for file and folder paths
file_to_load = ask_file_path()
output_dir = ask_folder_path()
os.makedirs(output_dir, exist_ok=True)

# Extract just the filename
czi_file = os.path.basename(file_to_load)

print(f"Loading file from: {file_to_load}")
print(f"Exporting to folder: {output_dir}")

# Load the .czi file and extract metadata
czi = czifile.CziFile(file_to_load)
metadata_xml = czi.metadata()
root = ET.fromstring(metadata_xml)

# Dictionary to store stage positions
stage_positions = {}

# Extract stage positions from metadata
for scene in root.findall('.//Scene'):
    name = scene.get('Name')
    center_position = scene.find('CenterPosition').text if scene.find('CenterPosition') is not None else 'Not available'
    stage_positions[name] = center_position

# Assuming the first scene is always the center ("Mid")
dunn_center = stage_positions.get("Mid", "Not available")

# Load the image
img = AICSImage(file_to_load)

# Iterate through each scene using enumerate
for index, scene_name in enumerate(tqdm(img.scenes)):
    img.set_scene(scene_name)
    all_timepoints = img.get_image_data("TYX", S=0, C=0)

    tiff_filename = f"{output_dir}/xy point {index}.tiff"

    # Prepare metadata
    metadata = {
        'ImageJ': 'X.xx',
        'Info': f'Scene {scene_name} from {czi_file}',
        'DunnCenter': dunn_center,
        'StagePosition': stage_positions.get(scene_name, "Not available")
    }

    # Save the data as a TIFF file with metadata
    tifffile.imwrite(tiff_filename, all_timepoints, metadata=metadata)
