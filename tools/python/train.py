#imports
import os
os.system('cls')
import sys
import tqdm
import ast

#paths
train_i = r"yolov5-master/dataset/train/images"
train_l = r"yolov5-master/dataset/train/labels"
val_i= r"yolov5-master/dataset/val/images"
val_l = r"yolov5-master/dataset/val/labels"
data_yaml = r"yolov5-master/data.yaml"

def check_folders():
  checked = True
  if not (os.path.exists(train_i)):
    print(f"\nTraining images folder ({train_i}) does not exist! Aborting training...")
    checked = False
  elif (len(os.listdir(train_i)) == 0):
    print(f"\nWarning!: No images in training images ({train_i})!")
    checked = False

  if not (os.path.exists(train_l)):
    print(f"\nTraining labels folder ({train_l}) does not exist! Aborting training...")
    checked = False
  elif (len(os.listdir(train_l)) == 0):
    print(f"\nWarning!: No labels in training images! ({train_l})")
    checked = False

  if not (os.path.exists(val_i)):
    print(f"\nValidation images folder ({val_i}) does not exist! Aborting training...")
    checked = False
  elif (len(os.listdir(val_i)) == 0):
    print(f"\nWarning!: No images in validation images! ({val_i})")
    checked = False

  if not (os.path.exists(val_l)):
    print(f"\nValidation labels folder ({val_l}) does not exist! Aborting training...")
    checked = False
  elif (len(os.listdir(val_l)) == 0):
    print(f"\nWarning!: No labels in training images!  ({val_l})")
    checked = False

  return checked

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

def yaml_prompt(prompt):
  checked = True
  while True:
    create = input(f"\n{prompt}! Create data.yaml file? (y/n)")
    if create == "y" or create == "Y":
      create_yaml()
      break
    elif create == "n" or create == "N":
      print("\nStopping program...")
      checked = False
      break
    else:
      print("Invalid input")
        
  return checked

def check_data_yaml():
  if not (os.path.exists(data_yaml)):
    return yaml_prompt("data.yaml file does not exist")
  else:
    with open(data_yaml, 'r') as file:
      line = file.readlines()
    if len(line) == 0:
      return yaml_prompt("data.yaml is empty")
    else:
      pass_ = True
      error = ""
      species = get_labels()
      train_path = "/".join(train_i.split("/")[1:])
      val_path = "/".join(val_i.split("/")[1:])

      if line[0].split(": ")[-1].strip() != train_path:
        pass_ = False
        error = "Train path not correct"
      if line[1].split(": ")[-1].strip() != val_path:
        pass_ = False
        error = "Validation path not correct"
      if line[3].split(": ")[-1].strip() != str(len(species)):
        pass_ = False
        error = "Number of classes not correct"
      if ast.literal_eval(line[4].split(": ")[-1].strip()) != species:
        pass_ = False
        error = "Classes not correct"
      if (pass_):
        return pass_
      else:
        return yaml_prompt(f"Error with data.yaml file\n{error}")

while True:
  user_a = input("Please make sure the dataset is checked and split before training. Continue? (y/n)")

  if user_a == "y" or user_a == "Y":
    print("\nChecking all folders...")
    if(check_folders()):
      print("\nChecks complete!")
      print("\nChecking data.yaml file...")
      if(check_data_yaml()):
        print("\nChecks complete!\n")
        sys.exit(1)
      else:
        sys.exit(0)
        break
    else:
      print("\nChecks failed! Please check dataset and rerun")
      sys.exit(0)
    break
  elif user_a == "n" or user_a == "N":
    print("\nStopping program...\n")
    sys.exit(0)
    break
  else:
    print("Invalid input")
