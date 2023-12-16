@echo off

./venv/Scripts/python.exe -m pdoc ./experiments/ -o ./docs
./venv/Scripts/python.exe -m pdoc ./screens/ -o ./docs
./venv/Scripts/python.exe -m pdoc ./widgets/ -o ./docs
./venv/Scripts/python.exe -m pdoc main.py -o ./docs
