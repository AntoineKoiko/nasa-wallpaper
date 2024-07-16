import requests
import os
import datetime
import json
import sys

from dotenv import load_dotenv

load_dotenv()

now = datetime.datetime.now()
SET_WALPPAPER = bool(os.environ.get('SET_WALLPAPER', '0'))
NASA_KEY = os.environ.get('NASA_KEY')
# muste be an absolute path e.g. /home/user/Pictures
OUPTUT_DIR = os.environ.get('OUPTUT_DIR') # need to be created before running the script

if not NASA_KEY or not OUPTUT_DIR:
    raise ValueError('NASA_KEY or OUPTUT_DIR not set in .env file')

APOD_URL = 'https://api.nasa.gov/planetary/apod?'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


def get_apod():
    date = now.strftime('%Y-%m-%d')

    params = {"api_key": NASA_KEY, "hd": True,'thumbs': True, 'date': date}
    response = requests.get(url=APOD_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code, response.text)
    return None


def load_nasa_image(img_data):
    date = img_data['date']
    try:
        img_url = img_data['hdurl']
    except KeyError:
        img_url = img_data['thumbnail_url']
    img_path = os.path.join(OUPTUT_DIR, f'{date}.jpg')
    img_data = requests.get(img_url).content
    with open(img_path, 'wb') as handler:
        handler.write(img_data)
    return img_path


def set_wallpaper(path):
    if sys.platform == 'linux':
        cmd = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri-dark'
    else:
        raise NotImplementedError('OS not supported')

    abs_path = path #os.path.abspath(path)
    print(f'EXEC: {cmd} {abs_path}')
    os.system(f'{cmd} {abs_path}')


if __name__ == '__main__':
    apod = get_apod()
    print(json.dumps(apod, sort_keys=True, indent=4))
    path = load_nasa_image(apod)
    print(f'Image saved at: {path}')
    if SET_WALPPAPER:
        set_wallpaper(path)
