import command_system
import vk
from settings import token, s_token
from flask_app import curr_user_id
import os
import random
import re
import requests
from flask import json

session = vk.Session()
api = vk.API(session, v=5.92)

def tinderFirstIterM():
    path = "/home/jBloodless/mysite/tinder/"
    user_id = curr_user_id()
    curr_user = api.users.get(user_ids=str(user_id), fields = 'sex', access_token = s_token)
    curr_sex = curr_user[0]['sex']
    if curr_sex == 1:
        sex_str = 'female'
    elif curr_sex == 2:
        sex_str = 'male'
    first_name = curr_user[0]['first_name']
    last_name = curr_user[0]['last_name']
    try:
        os.rename("/home/jBloodless/mysite/tinder/toW_{0}_{1}_{2}".format(sex_str, first_name, last_name), "/home/jBloodless/mysite/tinder/toM_{0}_{1}_{2}".format(sex_str, first_name, last_name))
    except (OSError, FileNotFoundError):
        try:
            os.rename("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}".format(sex_str, first_name, last_name), "/home/jBloodless/mysite/tinder/toM_{0}_{1}_{2}".format(sex_str, first_name, last_name))
        except (OSError, FileNotFoundError):
            pass
    user_name = first_name
    user_surn = last_name
    sex=''

    dislikes = '/home/jBloodless/mysite/tinder/toM_{0}_{1}_{2}/dislikes'.format(sex_str, first_name, last_name)
    likes = '/home/jBloodless/mysite/tinder/toM_{0}_{1}_{2}/likes'.format(sex_str, first_name, last_name)
    i=0
    for i in range(len(os.listdir(path))):
        if i==len(os.listdir(path))-1:
            message = 'Пока новых участников не появилось. Но не стоит отчаиваться — это только начало! Возвращайся позже, и чудо обязательно произойдет!'
            buttons = open("/home/jBloodless/mysite/tinderEnd.json", "r", encoding="UTF-8").read()
            return message, '', buttons
        name = re.split(r'_', str(os.listdir(path)[i]))
        dest = name[0]
        sex = name[1]
        user_name=name[2]
        user_surn=name[3]
        user_prof = user_name+'_'+user_surn
        if user_prof not in os.listdir(dislikes) and user_prof not in os.listdir(likes) and first_name!=user_name and last_name!=user_surn and sex!='female':
            break

    #user_dir = "/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}".format(dest, sex, user_name, user_surn)
    user_pic = "/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}/{2}_{3}.jpg".format(dest, sex, user_name, user_surn)
    user_inf = "/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}/{2}_{3}.txt".format(dest, sex, user_name, user_surn)
    id_txt = "/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}/user_id.txt".format(dest, sex, user_name, user_surn)

    #os.rename("/home/jBloodless/mysite/tinder/{0}_{1}_{2}".format(sex_str, user_name, user_surn), "/home/jBloodless/mysite/tinder/toM_{0}_{1}_{2}".format(sex_str, user_name, user_surn))

    bio = open(user_inf, "r", encoding="UTF-8")
    id_to_msg = open(id_txt, "r", encoding="UTF-8")
    message = "@id"+str(id_to_msg.read())+'\n'+str(bio.read())

    server = api.photos.getMessagesUploadServer(peer_id=curr_user_id(), access_token = token)
    upload_url = server["upload_url"]
    files = {'photo': open(user_pic, 'rb')}
    response = requests.post(upload_url, files=files)
    result = json.loads(response.text)
    uploadResult = api.photos.saveMessagesPhoto(server=result["server"], photo=result["photo"], hash=result["hash"], access_token = token)
    attachment = 'photo'+str(uploadResult[0]["owner_id"])+'_'+str(uploadResult[0]["id"])
    #attachment = ''

    buttons = open("/home/jBloodless/mysite/tinderKeys.json", "r", encoding="UTF-8").read()
    #message = str(uploadResult[0]["id"])
    #os.rename("/home/jBloodless/mysite/tinder/{0}_{1}_{2}".format(sex_str, first_name, last_name), "/home/jBloodless/mysite/tinder/toM_{0}_{1}_{2}".format(sex_str, first_name, last_name))

    return message, attachment, buttons


tinderFirstIterM_command = command_system.Command()

tinderFirstIterM_command.keys = ['С парнями']
tinderFirstIterM_command.description = 'internal tinder message'
tinderFirstIterM_command.process = tinderFirstIterM