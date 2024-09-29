cd /d "%~dp0"
cd ..
cd Scripts
call activate
cd ..
python tools/python/detect.py
IF ERRORLEVEL 0 (
	echo Failed checks, press any key to continue
	pause
	exit /b
) ELSE (
	pause
	cd yolov5-master
	python detect.py --source images --weights runs/train/selected/weights/best.pt --save-csv
	pause
)
