#!/bin/bash

HEADER_NPVPY="\"Type\",\"Op\",\"Size\",\"Time\",\"Iters\"";
HEADER_SIZE="\"Type\",\"Size\",\"Bytes\"";

echo $HEADER_NPVPY > npVpy_results.csv
python3 ./npVpy.py >> npVpy_results.csv

echo $HEADER_SIZE > npVpy_size_results.csv
python3 ./npVpy_size.py >> npVpy_size_results.csv
