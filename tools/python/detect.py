#imports
import os
os.system('cls')
import sys
import tqdm
import ast

#paths
labels = r"yolov5-master/dataset/labels.txt"
model = r"yolov5-master/runs/train/selected"
source = r"yolov5-master/source"

def check_folders():
  checked = True
  if not (os.path.exists(source)):
    print(f"\nSource images folder ({source}) does not exist! Aborting inference...")
    checked = False
  elif (len(os.listdir(source)) == 0):
    print(f"\nWarning!: No images in source images ({source})!")
    checked = False

  if not (os.path.exists(labels)):
    print(f"\nLabels text file ({labels}) does not exist! Aborting inference...")
    checked = False

  with open(labels, 'r') as file:
      line = file.readlines()

  if (len(line) == 0):
    print(f"\nWarning!: Labels text file is empty ({labels})!")
    checked = False
  
  if not (os.path.exists(model)):
    print(f"\nModel folder ({model}) does not exist! Aborting inference...")
    checked = False

  weights = os.path.join(model, 'weights')

  if not (os.path.exists(weights)):
    print(f"\nModel weights folder ({weights}) does not exist! Aborting inference...")
    checked = False

  if not (os.path.exists(os.path.join(weights, 'best.pt'))):
    print(f"\nModel file folder ({os.path.join(weights, 'best.pt')}) does not exist! Aborting inference...")
    checked = False

  return checked

while True:
  user_a = input("Please make sure the:\n\n1)source image folder\n2)model weights folder\n3)labels textfile\nall exist.\n\nContinue? (y/n)")

  if user_a == "y" or user_a == "Y":
    print("\nChecking all folders...")
    if(check_folders()):
      print("\nChecks complete!")
      sys.exit(0)
    else:
      print("\nChecks failed! Please check dataset and rerun")
      sys.exit(1)
    break
  elif user_a == "n" or user_a == "N":
    print("\nStopping program...\n")
    sys.exit(1)
    break
  else:
    print("Invalid input")
