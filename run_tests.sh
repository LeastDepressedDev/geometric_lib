#!/bin/bash

echo -e "\n\n\n\n\n\n\n\n\nRunning tests for circle:\n"
python -m unittest circle.py

echo -e "\n\n\n\n\n\n\n\n\nRunning tests for rectangle:\n"
python -m unittest rectangle.py

echo -e "\n\n\n\n\n\n\n\n\nRunning tests for square:\n"
python -m unittest square.py

echo -e "\n\n\n\n\n\n\n\n\nRunning tests for triangle:\n"
python -m unittest triangle.py