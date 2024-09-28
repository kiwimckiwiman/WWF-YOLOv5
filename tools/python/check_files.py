#imports
import os
os.system('cls')
import tqdm

#paths
dataset = r"yolov5-master/dataset"
images = r"yolov5-master/dataset/images"
labels = r"yolov5-master/dataset/labels"

image_types = ["jpg", "JPG", "jpeg", "JPEG", "png", "PNG"]

#check files
def check_files(images, labels):
  print(f"Files available\n images: {len(os.listdir(images))}\n labels: {len(os.listdir(labels))}")
  
  print("\nChecking image folder...")
  no_img_type = []
  
  for i in tqdm.tqdm(os.listdir(images)):
    for type in image_types:
      found = False
      if type in i:
        found = True
        break
    if found == False:
      no_img_type.append(i)

  print(f'\nTotal non-image files {len(no_img_type)}\n')
  for i in no_img_type:
    print(f'{i} is a valid image type (jpg, png, and jpegs only). Please check before training')
  
  print("\n==========================================================")

  print("\nChecking if images have matching labels...")
  none_images = []
  for i in tqdm.tqdm(os.listdir(images)):
    found = False
    for j in (os.listdir(labels)):
      if  i.split('.')[0] == j.split('.')[0]:
        found = True
        break
    if found == False:
        none_images.append(i)
  print(f'\nTotal images with no labels {len(none_images)}\n')

  for i in none_images:
    print(f'{i} has no matching label(s). Please check before training')
  
  print("\n==========================================================")

  print("\nChecking if labels have matching images...")
  none_labels = []
  for i in tqdm.tqdm(os.listdir(labels)):
    if i == "classes.txt":
      continue
    else:
      found = False
      for j in (os.listdir(images)):
        if  i.split('.')[0] == j.split('.')[0]:
          found = True
          break
      if found == False:
          none_labels.append(i)
  print(f'\nTotal labels with no images {len(none_labels)}\n')

  for i in none_labels:
    print(f'{i} has no matching image. Please check before training')

  print("\n==========================================================")

  print("\nChecking if labels empty...")
  empty = []
  for i in tqdm.tqdm(os.listdir(labels)):
    if i == "classes.txt":
      continue
    else:
      with open(os.path.join(labels, i), 'r') as file:
        lines = file.readlines()
      if len(lines) == 0:
        empty.append(i)
        print(f"{i} is empty")
  print(f'\nTotal empty labels {len(empty)}\n')

  for i in empty:
    print(f'{i} is empty. Please check before training')

  print("\n==========================================================")

  print("\nChecking if classes file exists...")
  found_classes = False
  for j in (os.listdir(labels)):
    if j == "classes.txt":
      found_classes = True
      break
  if(found_classes):
    print("\nClasses file found!")
  else:
    print("\nClasses file not found! Fix before training!")

  print("\n==========================================================")
  
  print("\nChecking if labels text file exists...")
  found_classes = False
  for j in (os.listdir(dataset)):
    if j == "labels.txt":
      found_classes = True
      break
  if(found_classes):
    print("\nLabels text file found!")
  else:
    print("\nLabels text file not found! Fix before running inferences!")

  print("\n==========================================================")
  
def count_species(labels):
  print("\nChecking class distributions via labels...")
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
#----------
if (os.path.exists(images)) and (os.path.exists(images)):
  if (len(os.listdir(images)) == 0):
    print("Image folder empty! Please check and run again")
  elif (len(os.listdir(labels)) == 0):
    print("Label folder empty!  Please check and run again")
  else:
    check_files(images, labels)
    count_species(labels)
    print("\n")
else:
  print("Image or label files not found or not named 'images' and 'labels'! Please check and run again")