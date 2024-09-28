cd /d "%~dp0"
cd ..
cd Scripts
call activate
cd ..
python tools/python/train.py
pause
cd yolov5-master
python train.py --data data.yaml --weights yolov5m.pt --img 640 --epochs 100 --batch 32
pause