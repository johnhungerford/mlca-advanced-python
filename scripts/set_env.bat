@echo off

set parent=%~dp0
for %%B in (%parent%.) do set grandparent=%%~dpB
python -m venv .venv
pip install -r requirements.txt
echo set PYTHONPATH=%grandparent% >> .venv\Scripts\activate.bat
.venv\Scripts\activate.bat
