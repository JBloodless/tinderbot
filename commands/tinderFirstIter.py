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

def tinderFirstIter():
    path = "/home/jBloodless/mysite/tinder/"
    user_id = curr_user_id()
    curr_user = api.users.get(user_ids=str(user_id), access_token = s_token)
    first_name = curr_user[0]['first_name']
    last_name = curr_user[0]['last_name']
    user_name = first_name
    user_surn = last_name
    while first_name==user_name and last_name==user_surn:
        first_user=random.choice(os.listdir(path))
        name = re.split(r'_', str(first_user))
        user_name=name[0]
        user_surn=name[1]

    user_dir = "/home/jBloodless/mysite/tinder/{0}_{1}".format(user_name, user_surn)
    user_pic = "/home/jBloodless/mysite/tinder/{0}_{1}/{0}_{1}.jpg".format(user_name, user_surn)
    user_inf = "/home/jBloodless/mysite/tinder/{0}_{1}/{0}_{1}.txt".format(user_name, user_surn)
    id_txt = "/home/jBloodless/mysite/tinder/{0}_{1}/user_id.txt".format(user_name, user_surn)

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
    return message, attachment, buttons


tinderFirstIter_command = command_system.Command()

tinderFirstIter_command.keys = ['legacy_file']
tinderFirstIter_command.description = 'internal tinder message'
tinderFirstIter_command.process = tinderFirstIter