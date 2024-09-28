cd /d "%~dp0"
cd ..
cd Scripts
call activate
cd ..
python tools/python/reset_files.py
pause