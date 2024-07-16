# Nasa Wallpaper 🚀

A simple script to fetch the nasa picture of the day, save it and set it as your wallpaper if you want 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Setup

### Dependancies

I recomanded to use venv to setup a virtual environment to install required modules (![venv doc](https://docs.python.org/3/library/venv.html))

First create the virtual environment
```bash
python -m venv .venv
```
This will create a virtual environment in the `.venv` direcotry.

Then activate the virtual environment
```bash
source .venv/bin/activate
```

Now You can install the dependancies
```bash
pip install -r requirements.txt
```

### Environment variables

copy the `.env.sample` file to a `.env` file and fill the requried variables

```
NASA_KEY="YOUR_NASA_API_KEY"
SET_WALLPAPER=1 # 1 for true, 0 for false
```

Get a nasa api key: [click here](https://api.nasa.gov/)

## Run

Execute this to run the script
```bash
python nasa-wallpaper.py
```

This will get the image from teh API, store it into a `pictures` directory and set it as your wallpaper depending on the value set in your environment.

## Features

- Get picture of the day
- Save picture
  
Set picture as wallpaper:
- Linux # Tested with ubuntu 22.04
- Linux: choose between dark and light theme
- Windows : TDOo
- Mac : TODO


## Contribution

All contributions are welcome
