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

def tinderDislike():
    path = "/home/jBloodless/mysite/tinder/"
    user_id = curr_user_id()
    curr_user = api.users.get(user_ids=str(user_id), fields = 'sex', access_token = s_token)
    curr_sex = curr_user[0]['sex']
    if curr_sex == 1:
        curr_sex_str = 'female'
    elif curr_sex == 2:
        curr_sex_str = 'male'
    first_name = curr_user[0]['first_name']
    last_name = curr_user[0]['last_name']
    hist = api.messages.getHistory(peer_id = user_id, group_id=17379212, offset = 1, count = 1, access_token = token)
    tinderBio = hist['items'][0]['text']
    l = tinderBio.find('d')
    r = tinderBio.find('|')
    dislike_id = tinderBio[l+1:r]

    dirs = os.listdir(path)
    for i in range(len(dirs)):
        if dirs[i].endswith('_{0}_{1}_{2}'.format(curr_sex_str, first_name, last_name)):
            dir_name = re.split(r'_', str(dirs[i]))
            currdest = dir_name[0]

    dislike_user = api.users.get(user_ids=str(dislike_id), fields = 'sex', access_token = s_token)
    dislike_first_name = dislike_user[0]['first_name']
    dislike_last_name = dislike_user[0]['last_name']

    curr_dislike_f= open("/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}/dislikes/{4}_{5}".format(currdest, curr_sex_str, first_name, last_name, dislike_first_name, dislike_last_name), "w")
    curr_dislike_f.write(dislike_id)
    curr_dislike_f.close()

    user_name = first_name
    user_surn = last_name
    sex=''

    dislikes = '/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}/dislikes'.format(currdest, curr_sex_str, first_name, last_name)
    likes = '/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}/likes'.format(currdest, curr_sex_str, first_name, last_name)
    i=0
    if currdest=='toA':
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
            if user_prof not in os.listdir(dislikes) and user_prof not in os.listdir(likes) and first_name!=user_name and last_name!=user_surn:
                break

    elif currdest=='toM':
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

    elif currdest=='toW':
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
            if user_prof not in os.listdir(dislikes) and user_prof not in os.listdir(likes) and first_name!=user_name and last_name!=user_surn and sex!='male':
                break

    #user_dir = "/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}".format(name[0], sex, user_name, user_surn)
    user_pic = "/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}/{2}_{3}.jpg".format(dest, sex, user_name, user_surn)
    user_inf = "/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}/{2}_{3}.txt".format(dest, sex, user_name, user_surn)
    id_txt = "/home/jBloodless/mysite/tinder/{0}_{1}_{2}_{3}/user_id.txt".format(dest, sex, user_name, user_surn)

    bio = open(user_inf, "r", encoding="UTF-8")
    id_to_msg = open(id_txt, "r", encoding="UTF-8")
    message = "@id"+str(id_to_msg.read())+'\n'+str(bio.read())
    #message = currdest

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
    return message, attachment, buttons


tinderDislike_command = command_system.Command()

tinderDislike_command.keys = ['Дизлайк.']
tinderDislike_command.description = 'internal tinder message'
tinderDislike_command.process = tinderDislike