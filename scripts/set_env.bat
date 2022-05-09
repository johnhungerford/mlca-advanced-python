@echo off

set parent=%~dp0
for %%B in (%parent%.) do set grandparent=%%~dpB
python -m venv .venv
echo python -m pip install -r requirements.txt >> .venv\Scripts\activate.bat
echo set PYTHONPATH=%grandparent% >> .venv\Scripts\activate.bat
.venv\Scripts\activate.bat
