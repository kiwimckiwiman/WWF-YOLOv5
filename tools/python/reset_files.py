#imports
import os
os.system('cls')
import shutil
import tqdm

#paths
images = r"yolov5-master/dataset/images"
labels = r"yolov5-master/dataset/labels"
train_i = r"yolov5-master/dataset/train/images"
train_l = r"yolov5-master/dataset/train/labels"
val_i= r"yolov5-master/dataset/val/images"
val_l = r"yolov5-master/dataset/val/labels"

  
def check_folders():
  checked = True
  if not (os.path.exists(train_i)):
    print(f"\nTraining images folder ({train_i}) does not exist! Aborting reset...")
    checked = False
  elif (len(os.listdir(train_i)) == 0):
    print(f"\nWarning!: No images in training images ({train_i})!")

  if not (os.path.exists(train_l)):
    print(f"\nTraining labels folder ({train_l}) does not exist! Aborting reset...")
    checked = False
  elif (len(os.listdir(train_l)) == 0):
    print(f"\nWarning!: No labels in training images! ({train_l})")

  if not (os.path.exists(val_i)):
    print(f"\nValidation images folder ({val_i}) does not exist! Aborting reset...")
    checked = False
  elif (len(os.listdir(val_i)) == 0):
    print(f"\nWarning!: No images in validation images! ({val_i})")

  if not (os.path.exists(val_l)):
    print(f"\nValidation labels folder ({val_l}) does not exist! Aborting reset...")
    checked = False
  elif (len(os.listdir(val_l)) == 0):
    print(f"\nWarning!: No labels in training images!  ({val_l})")

  if not (os.path.exists(images)):
    print(f"\nMain image folder ({images}) does not exist! Create folder and rerun. Aborting reset...")
    checked = False
  elif (len(os.listdir(images)) > 0):
    if(prompt("images", images) == False):
      return False

  if not (os.path.exists(labels)):
    print(f"\nMain labels folder ({labels}) does not exist! Create folder and rerun. Aborting reset...")
    checked = False
  elif (len(os.listdir(labels)) > 0):
    if(prompt("labels", labels) == False):
      return False

  return checked

def prompt(folder, path):
  while True:
    user_a = input(f"\nWarning!: {folder} found in main {folder} folder ({path})! Continue? (y/n)")
    if user_a == "y" or user_a == "Y":
      print("\nContinuing...")
      return True
    elif user_a == "n" or user_a == "N":
      print("\nStopping program...\n")
      return False
    else:
      print("Invalid input")

def move_files():
  print("\nMoving files back to dataset images and labels...")

  print("\n==========================================================")
  print("\nMoving from training images to images...\n")
  for i in tqdm.tqdm(os.listdir(train_i)):
    try:
      shutil.move(os.path.join(train_i, i), os.path.join(images, i))
    except:
      print(f"Error moving file {i}")

  print("\n==========================================================")
  print("\nMoving from training labels to labels...\n")
  for i in tqdm.tqdm(os.listdir(train_l)):
    try:
      shutil.move(os.path.join(train_l, i), os.path.join(labels, i))
    except:
      print(f"Error moving file {i}")

  print("\n==========================================================")
  print("\nMoving from validation images to images...\n")
  for i in tqdm.tqdm(os.listdir(val_i)):
    try:
      shutil.move(os.path.join(val_i, i), os.path.join(images, i))
    except:
      print(f"Error moving file {i}")

  print("\n==========================================================")
  print("\nMoving from validation labels to labels...\n")
  for i in tqdm.tqdm(os.listdir(val_l)):
    try:
      shutil.move(os.path.join(val_l, i), os.path.join(labels, i))
    except:
      print(f"Error moving file {i}")

while True:
  user_a = input("Are you sure you wish to move all labels and images to original folders? (y/n)")

  if user_a == "y" or user_a == "Y":
    print("\nChecking all folders...")
    if(check_folders()):
      print("\nChecks complete!")
      move_files()
    break
  elif user_a == "n" or user_a == "N":
    print("\nStopping program...\n")
    break
  else:
    print("Invalid input")