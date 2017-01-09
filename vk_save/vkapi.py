import vk
import os, time
# import requests
# from urllib.request import urlretrieve
# import json
import math


def get_largest_photo(photo_dict, key='src_xxxbig'):
    try:
        return photo_dict[key]
    except KeyError:
        key = key.replace('xbig', 'big')
        return get_largest_photo(photo_dict, key)

def get_photos(url):
    token = os.environ.get("TOKEN")
    session = vk.Session()
    vkapi = vk.API(session)

    # url = 'https://vk.com/album300168576_000'

    album_id = url.split('/')[-1].split('_')[1]
    owner_id = url.split('/')[-1].split('_')[0].replace('album', '')
    if album_id == '000':
        album_id = 'saved'
    elif album_id == '00':
        album_id = 'wall'
    elif album_id == '0':
        album_id = 'profile'


    photos_items = vkapi.photos.get(owner_id=owner_id, album_id=album_id, access_token=token)

    # print(json.dumps(photos_count, sort_keys=True, indent=4))

    for i in range(math.ceil( len(photos_items) / 1000)):
        photos_items += vkapi.photos.get(owner_id=owner_id, album_id=album_id,
                                        access_token=token, offset=1000 * i)
        time.sleep(0.5)

    photos = list(set(list(map(lambda item: get_largest_photo(item), photos_items))))
    return photos