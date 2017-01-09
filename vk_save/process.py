"""The module for saving pics localy and zip it."""
import urllib.request
from multiprocessing import Pool
import os
import zipfile
import settings
import random
import glob
import datetime


WORK_DIR = os.path.join(settings.STATICFILES_DIRS[0])+"/media/"


def get_name(url):
    return os.path.join(WORK_DIR, url.split('/')[-1])


def save_one(url):
    file_name = get_name(url)
    urllib.request.urlretrieve(url, file_name)


def save_all(urls):
    p = Pool(5)
    p.map(save_one, urls)


def zip_all(file_names):
    zf = zipfile.ZipFile(WORK_DIR+'/fknshtziprar.zip', mode='w')
    for name in file_names:
        zf.write(name, os.path.basename(name))
    zf.close()


def delete_all(file_names):
    p = Pool(5)
    p.map(os.remove, file_names)


def check_time(zip_file):
    t = datetime.datetime(*zip_file.infolist()[0].date_time[:])
    now = datetime.datetime.now()
    if (now-t).seconds > 3600:
        return 1
    else:
        return 0


def cleaner():
    files = glob.glob(WORK_DIR + "*.zip")
    zippes = [zipfile.ZipFile(name) for name in files]
    tt = list(map(check_time, zippes))
    for i in range(len(tt)):
        zippes[i].close()
        if tt[i] == 1:
            os.remove(files[i])

def process(urls):
    save_all(urls)
    file_names = list(map(get_name, urls))
    zip_all(file_names)
    delete_all(file_names)
    cleaner()

urls = ["https://pp.vk.me/c630725/v630725576/456db/jEu72W_q80s.jpg","https://pp.vk.me/c630725/v630725576/456c2/By-HGGISuM4.jpg"]
filenames = list(map(get_name, urls))
