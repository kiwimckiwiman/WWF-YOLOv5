cd /d "%~dp0"
cd ..
cd Scripts
call activate
cd ..
python tools/python/train.py
IF ERRORLEVEL 1 (
	echo Failed checks, press any key to continue
	pause
	exit /b
) ELSE (
	pause
	cd yolov5-master
	python train.py --device 0 --data data.yaml --weights yolov5m.pt --img 640 --epochs 100 --batch 32
	pause
)
