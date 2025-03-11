import pandas as pd
from glob import glob

# --------------------------------------------------------------
# Read single CSV file
# --------------------------------------------------------------

single_file_acc = pd.read_csv('../../data/raw/MetaMotion/accelerometer_2021-03-25T14-00-00.000000Z_2021-03-25T14-30-00.000000Z.csv')

single_file_gyr = pd.read_csv('../../data/raw/MetaMotion/gyroscope_2021-03-25T14-00-00.000000Z_2021-03-25T14-30-00.000000Z.csv')


# --------------------------------------------------------------
# List all data in data/raw/MetaMotion
# --------------------------------------------------------------

files = glob('../../data/raw/MetaMotion/*.csv')

# --------------------------------------------------------------
# Extract features from filename
# --------------------------------------------------------------


# --------------------------------------------------------------
# Read all files
# --------------------------------------------------------------


# --------------------------------------------------------------
# Working with datetimes
# --------------------------------------------------------------


# --------------------------------------------------------------
# Turn into function
# --------------------------------------------------------------


# --------------------------------------------------------------
# Merging datasets
# --------------------------------------------------------------


# --------------------------------------------------------------
# Resample data (frequency conversion)
# --------------------------------------------------------------

# Accelerometer:    12.500HZ
# Gyroscope:        25.000Hz


# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------