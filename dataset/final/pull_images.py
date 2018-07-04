import os
import shutil
import requests
from requests.exceptions import ConnectionError, ReadTimeout, HTTPError, SSLError, Timeout, ReadTimeout, URLRequired, TooManyRedirects, RetryError
from urllib3.exceptions import ProtocolError

vehicles = ["van"] #["bus","car"]


for vehicle in vehicles:
    inp_urls = vehicle + "/" + vehicle + "_images.txt"
    imgs = [img.decode('utf-8')
            for img in open(inp_urls, "rb").read().splitlines() if img.decode('utf-8')]


    for imgurl in imgs:
        try:
            response = requests.get(imgurl, stream=True)
            outimg = imgurl.split("/")[-1]
            outdir = os.path.join(vehicle, outimg)
            with open(outdir, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
        except SSLError:
            print("Cannot pull: ", imgurl)
        except ConnectionError:
            print("Cannot pull: ", imgurl)
        except ReadTimeout:
            print("Cannot pull: ", imgurl)
        except HTTPError:
            print("Cannot pull: ", imgurl)
        except ReadTimeout:
            print("Cannot pull: ", imgurl)
        except Timeout:
            print("Cannot pull: ", imgurl)
        except TooManyRedirects:
            print("Cannot pull: ", imgurl)
        except RetryError:
            print("Cannot pull: ", imgurl)
        except ProtocolError:
            print("Cannot pull: ", imgurl)
