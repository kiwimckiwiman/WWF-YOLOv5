cd /d "%~dp0"
cd ..
cd Scripts
call activate
cd ..
python tools/python/check_files.py
pause