import random
import urllib

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.urlretrieve(url, full_name)

download_web_image("http://www.mediastaan.com/wp-content/uploads/2013/12/girls-wallpaper-mediastaan-22.jpg")
