import command_system
import vk
from settings import token, s_token
import urllib
from flask_app import curr_user_id
import os
import shutil

session = vk.Session()
api = vk.API(session, v=5.92)

def tinderProcess():
    user_id = curr_user_id()
    user = api.users.get(user_ids=str(user_id), fields='sex', access_token = s_token)
    sex = user[0]['sex']
    if sex == 1:
        sex_str = 'female'
    elif sex == 2:
        sex_str = 'male'
    first_name = user[0]['first_name']
    last_name = user[0]['last_name']
    #tinderPhoto = api.messages.getHistoryAttachments(peer_id = user_id, group_id=163586862, media_type = 'photo', count = 1, access_token = token)
    #tinderPhotoURL = tinderPhoto['items'][0]['attachment']['photo']['sizes'][6]['url']
    hist = api.messages.getHistory(peer_id = user_id, group_id=17379212, offset=1, count =1, access_token = token)
    attach_photo=hist['items'][0]['attachments'][0]['photo']['sizes']
    width = [None]*len(attach_photo)
    width_s = [None]*len(attach_photo)
    for itr in range(len(attach_photo)):
        width[itr]=attach_photo[itr]['width']
    width_s=sorted(width, reverse = True)
    for nitr in range(len(attach_photo)):
        if attach_photo[nitr]['width']==width_s[0]:
            tinderPhotoURL=attach_photo[nitr]['url']
    tinderBio = hist['items'][0]['text']
    if os.path.isdir("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/".format(sex_str, first_name, last_name)):
        shutil.rmtree("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/".format(sex_str, first_name, last_name), ignore_errors=True)
    elif os.path.isdir("/home/jBloodless/mysite/tinder/toW_{0}_{1}_{2}/".format(sex_str, first_name, last_name)):
        shutil.rmtree("/home/jBloodless/mysite/tinder/toW_{0}_{1}_{2}/".format(sex_str, first_name, last_name), ignore_errors=True)
    elif os.path.isdir("/home/jBloodless/mysite/tinder/toM_{0}_{1}_{2}/".format(sex_str, first_name, last_name)):
        shutil.rmtree("/home/jBloodless/mysite/tinder/toM_{0}_{1}_{2}/".format(sex_str, first_name, last_name), ignore_errors=True)
    try:
        os.mkdir("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}".format(sex_str, first_name, last_name))
    except OSError:
        pass
    try:
        os.mkdir("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/likes".format(sex_str, first_name, last_name))
    except OSError:
        pass
    try:
        os.mkdir("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/dislikes".format(sex_str, first_name, last_name))
    except OSError:
        pass
    photo = urllib.request.urlopen(tinderPhotoURL).read()
    if os.path.isfile("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/{1}_{2}.jpg".format(sex_str, first_name, last_name)):
        os.remove("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/{1}_{2}.jpg".format(sex_str, first_name, last_name))
    f = open("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/{1}_{2}.jpg".format(sex_str, first_name, last_name), "wb")
    f.write(photo)
    f.close()
    if os.path.isfile("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/{1}_{2}.txt".format(sex_str, first_name, last_name)):
        os.remove("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/{1}_{2}.txt".format(sex_str, first_name, last_name))
    bio = open("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/{1}_{2}.txt".format(sex_str, first_name, last_name), "w")
    bio.write(tinderBio)
    bio.close()
    idtxt = open("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}/user_id.txt".format(sex_str, first_name, last_name), "w")
    idtxt.write(str(user_id))
    idtxt.close()
    #message = str(tinderPhotoURL)
    message = 'Отлично. Жми кнопку, если все готово.'
    buttons = open("/home/jBloodless/mysite/tinderToPeople.json", "r", encoding="UTF-8").read()
    return message, '', buttons

tinderProcess_command = command_system.Command()

tinderProcess_command.keys = ['Загрузить']
tinderProcess_command.description = 'internal tinder message'
tinderProcess_command.process = tinderProcess