import vk
import random
from settings import s_token

session = vk.Session()
api = vk.API(session, v=5.92)


def get_random_old_picture():
    max_num = api.photos.get(owner_id='-177456743', album_id='264789751', count=0, access_token=s_token)['count']
    num = random.randint(1, max_num)
    photo = api.photos.get(owner_id='-177456743', album_id='264789751', count=1, offset=num, access_token=s_token)['items'][0]['id']
    attachment = 'photo' + '-177456743' + '_' + str(photo)
    return attachment


def send_message(user_id, token, message, buttons, attachment=""):
    rnd_seed = random.randint(0, 2147483647)
    if buttons == None:
        api.messages.send(random_id=rnd_seed, access_token=token, user_id=str(user_id), message=message, attachment=attachment)
    else:
        api.messages.send(random_id=rnd_seed, access_token=token, user_id=str(user_id), message=message, attachment=attachment, keyboard = buttons)