#!/usr/bin/env python
import sys
import os

# Get the parent directory of the current file
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Add the parent directory to sys.path
sys.path.append(parent_dir)
from utils.temp_utils import temp_max_min_by_month # noqa E402
from utils.temp_utils import load_temp_data # noqa E402

if __name__ == "__main__":
    df = load_temp_data(data_dir="data")
    max_min_temp = temp_max_min_by_month(df)
    print(max_min_temp)
