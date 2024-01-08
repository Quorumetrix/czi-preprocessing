# CZI File Preprocessing Module

This module provides a simple Python script to process .czi files, extracting image data along with additional metadata related to the motorized stage positions and saving them as TIFF files. The script is designed to be user-friendly, with graphical prompts for file selection and output directory.

## Prerequisites

To use this module, you will need to have Anaconda installed on your system. Anaconda simplifies package management and deployment for Python and is available for Windows, macOS, and Linux.

Download and install Anaconda from [here](https://www.anaconda.com/products/individual).

## Installation

1. **Clone the Repository**:
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/Quorumetrix/czi-preprocessing



## Create and Activate Conda Environment:
Navigate to the cloned repository directory and create a Conda environment using the provided requirements.txt file:

    conda create --name czi-preprocessing python=3.9
    conda activate czi-preprocessing
    pip install -r requirements.txt


# Usage

#### Run the Script:
With the Conda environment activated, navigate to the directory containing the czi_preprocessing.py file and run the preprocessing script:

    python czi_preprocessing.py 

#### Select the CZI File:
A file dialog will appear. Select the .czi file you wish to process.

#### Select the Export Folder:
Next, a folder dialog will prompt you to select the output directory where the processed TIFF files will be saved.

#### Processing:
The script will process the selected .czi file, saving the image data and metadata to the chosen directory. Progress will be displayed in the command line interface.


### Output
The script will output TIFF files in the specified directory. Each file corresponds to a different stage position in the original .czi file. Additional metadata, including the XY position from the motorized stage, is embedded in each TIFF file.

