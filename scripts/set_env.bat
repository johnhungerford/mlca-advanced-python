@echo off

set parent=%~dp0
for %%B in (%parent%.) do set grandparent=%%~dpB
pip install -r requirements.txt
python -m venv .venv
echo set PYTHONPATH=%grandparent% >> .venv\Scripts\activate.bat
.venv\Scripts\activate.bat
