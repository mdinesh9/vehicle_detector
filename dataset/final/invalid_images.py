import argparse
from os import listdir, path, remove

import cv2
from PIL import Image

parser = argparse.ArgumentParser(description='Clean corrupted images.')
parser.add_argument('-d', '--dataset', type=str, required=True, help="Pass the input data directory.")
args = parser.parse_args()

input_dir = args.dataset

extensions = (".bmp", ".jpg", ".jpeg", ".png",
                    ".tif", ".tiff",".gif")

def valid_ext(file):
    return any([file.lower().endswith(ext) for ext in extensions])

def remove_imgs():
    """
    For a given input directory,
    reads each file, and deletes invalid images.
    """
    for file in listdir(input_dir):
        img_path = path.join(input_dir, file)

        if valid_ext(file):
            try:
                # check using Image
                img = Image.open(img_path)
                img.verify()

                # check using cv2
                img = cv2.imread(img_path)
                if img is None:
                    remove(img_path)

            except (IOError, SyntaxError) as e:
                remove(img_path)
        else:
            remove(img_path)


if __name__ == "__main__":
    remove_imgs()
