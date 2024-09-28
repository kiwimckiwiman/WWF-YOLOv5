cd /d "%~dp0"
cd ..
cd Scripts
call activate
cd ..
python tools/python/split_dataset.py
pause