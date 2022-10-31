#!/bin/bash
rm /Users/cheetoalonso/Desktop/CAPSTONE/Color-Recognition/data.csv
source /Users/cheetoalonso/Desktop/CAPSTONE/Color-Recognition/venv/bin/activate
python3 /Users/cheetoalonso/Desktop/CAPSTONE/Color-Recognition/data_gen.py &
python3 /Users/cheetoalonso/Desktop/CAPSTONE/Color-Recognition/run.py &
