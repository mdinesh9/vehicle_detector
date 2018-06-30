from google_images_download import google_images_download

KEYWORDS = ["car","bus","van","suv","motorbike","ambulance hartford","fire truck hartford","police car hartford","truck","moped","minivan"] #keywords
CHROMEDRIVER = "./chromedriver" #chromedriver
LIMIT = 2500 # limit


def get_images():
    for keyword in KEYWORDS:
        for additional in ["night", "back"]:
            output_path = "./../raw/1_first_imgs/" + str(keyword) + "_" + str(additional)

            arguments = {
                "keywords": keyword + " " + str(additional),
                "output_directory": output_path,
                # "prefix": keyword.replace(" ","_"),
                "chromedriver": CHROMEDRIVER,
                "limit": LIMIT

            }
            response = google_images_download.googleimagesdownload()
            absolute_image_paths = response.download(arguments)

if __name__ == "__main__":
    get_images()