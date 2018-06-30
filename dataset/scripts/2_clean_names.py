# !/usr/bin/python
import os
import shutil

KEYWORDS = ["car","bus","van","suv","motorbike","ambulance hartford","fire truck hartford","police car hartford","truck","moped","minivan"]

output_dir = "./../raw/2_cleaned_names"


def destination_foldername(folder):
    if "car" in folder:
        return "car"
    elif "bus" in folder:
        return "bus"
    elif "van" in folder:
        return "van"
    elif "suv" in folder:
        return "suv"
    elif "motorbike" in folder:
        return "motorbike"
    elif "ambulance" in folder:
        return "ambulance"
    elif any([name in folder for name in ["fire truck", "fire_truck", "truck","fire"]]):
        return "truck"
    elif any([name in folder for name in ["police", "police car", "police_car"]]):
        return "police_car"
    elif "moped" in folder:
        return "moped"
    elif "minivan" in folder:
        return "minivan"


for root, dirs, files in os.walk("./../raw/1_first_imgs", topdown=False):
    for name in set(dirs):
        eachdir = os.path.join(root, name)

        # loop through each dir
        for subdir, dirs_each, images in os.walk(eachdir, topdown=False):

            # check the files in sub dirs inside.
            if len(subdir.split("/")) > 5:
                folder = subdir.split("/")[-1].replace(' ','_')

                for img in images:
                    visited = []
                    img = os.path.join(subdir, img)
                    if img not in visited:
                        clean_name = img.split(' ')[-1]
                        dest_folder = os.path.join(output_dir, destination_foldername(folder))

                        if not os.path.exists(dest_folder):
                            os.makedirs(dest_folder)

                        outimg = os.path.join(dest_folder, clean_name)
                        shutil.copy(img, dest_folder)
                        visited.append(img)
                    else:
                        pass



