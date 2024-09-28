#imports
import os
os.system('cls')
import shutil
import random
import tqdm

images = r"yolov5-master/dataset/images"
labels = r"yolov5-master/dataset/labels"
train_i = r"yolov5-master/dataset/train/images"
train_l = r"yolov5-master/dataset/train/labels"
val_i= r"yolov5-master/dataset/val/images"
val_l = r"yolov5-master/dataset/val/labels"

def count_species(labels):
  print(f"\nChecking class distributions via labels {labels}...")
  species = {}
  for i in tqdm.tqdm(os.listdir(labels)):
    if "classes" not in i:
      with open(os.path.join(labels, i), 'r') as file:
        class_ = file.readline()
        class_ = class_[0]
        if class_ in species:
          species[class_] += 1
        else:
          species[class_] = 1
  print("\n")
  for i in species:
    print(f"class {i}: {species[i]} images") 

def get_labels():
  print("\nCollecting labels...")
  species = []
  for i in tqdm.tqdm(os.listdir(val_l)):
    if "classes" not in i:
      with open(os.path.join(val_l, i), 'r') as file:
        class_ = file.readline()
        class_ = class_[0]
        if class_ not in species:
          species.append(class_)
  for i in tqdm.tqdm(os.listdir(train_l)):
    if "classes" not in i:
      with open(os.path.join(train_l, i), 'r') as file:
        class_ = file.readline()
        class_ = class_[0]
        if class_ not in species:
          species.append(class_)
  return species

def create_folders():
  if not (os.path.exists(train_i)):
     print("\n Training images folder does not exist! Creating folder...")
     os.makedirs(train_i)
     print("Training images folder created!")

  if not (os.path.exists(train_l)):
     print("\n Training labels folder does not exist! Creating folder...")
     os.makedirs(train_l)
     print("Training labels folder created!")

  if not (os.path.exists(val_i)):
     print("\n Validation images folder does not exist! Creating folder...")
     os.makedirs(val_i)
     print("Validation images folder created!")

  if not (os.path.exists(val_l)):
     print("\n Validation labels folder does not exist! Creating folder...")
     os.makedirs(val_l)
     print("Validation labels folder created!")  

image_types_3 = ["jpg", "JPG", "png", "PNG"]
image_types_4 = ["jpeg", "JPEG"]

def split_train():
  rand_i = os.listdir(images)
  random.shuffle(rand_i)
  lim = int(len(os.listdir(images))*0.3)

  print("\nMoving files into training folder...")
  for i in tqdm.tqdm(rand_i[lim:]):
    try:
      shutil.move(os.path.join(images, i), os.path.join(train_i, i))
    except:
      print(f"\n Error moving image {i} to training images")
    try:
      if i[-3:] in image_types_3:
        shutil.move(os.path.join(labels, i.replace(i[-3:], "txt")), os.path.join(train_l, i.replace(i[-3:], "txt")))
      elif i[-4:] in image_types_4:
        shutil.move(os.path.join(labels, i.replace(i[-4:], "txt")), os.path.join(train_l, i.replace(i[-4:], "txt")))
    except:
        print(f"\n Error moving label for {i} to training labels")

  print("\nMoving files into validation folder...")
  for i in tqdm.tqdm(rand_i[:lim]):
    try:
      shutil.move(os.path.join(images, i), os.path.join(val_i, i))
    except:
      print(f"\n Error moving image {i} to validation images")
    try:
      if i[-3:] in image_types_3:
        shutil.move(os.path.join(labels, i.replace(i[-3:], "txt")), os.path.join(val_l, i.replace(i[-3:], "txt")))
      elif i[-4:] in image_types_4:
        shutil.move(os.path.join(labels, i.replace(i[-4:], "txt")), os.path.join(val_l, i.replace(i[-4:], "txt")))
    except:
        print(f"\n Error moving label for {i} to validation labels")

  print("\nAll files moved!. Copying classes.txt...")
  shutil.copy(os.path.join(labels, 'classes.txt'), os.path.join(train_l, 'classes.txt'))
  shutil.move(os.path.join(labels, 'classes.txt'), os.path.join(val_l, 'classes.txt'))

  print("\nSuccess!")
  print(f"\nTraining images: {len(os.listdir(train_i))}\nTraining labels: {len(os.listdir(train_l))}\nValidation images: {len(os.listdir(val_i))}\nValidation labels: {len(os.listdir(val_l))}")

def create_yaml():
  print("\nCreating data.yaml...")
  species = get_labels()
  train_path = "/".join(train_i.split("/")[1:])
  val_path = "/".join(val_i.split("/")[1:])
  lines = [f"train: {train_path}", f"val: {val_path}", "test:", f"nc: {len(species)}", f"names: {species}"]
  
  with open("yolov5-master/data.yaml", 'w') as file:
    for line in lines:
      file.write(line + '\n')
  print("Successfully created data.yaml!")

while True:
  user_a = input("Before splitting dataset, ensure files were checked with check_files.bat. Continue? (y/n)")

  if user_a == "y" or user_a == "Y":
    print("\nSplitting dataset to 70:30")
    create_folders()
    split_train()
    print("\nSplitting complete!\n")
    count_species(train_l)
    count_species(val_l)
    create_yaml()
    break
  elif user_a == "n" or user_a == "N":
    print("\nStopping program...\n")
    break
  else:
    print("Invalid input")