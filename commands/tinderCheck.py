import command_system
import vk
import os
from flask_app import curr_user_id
from settings import token, s_token

session = vk.Session()
api = vk.API(session, v=5.92)

def tinderCheck():
    user_id = curr_user_id()
    user = api.users.get(user_ids=str(user_id), fields = 'sex', access_token = s_token)
    sex = user[0]['sex']
    if sex == 1:
        sex_str = 'female'
    elif sex == 2:
        sex_str = 'male'
    first_name = user[0]['first_name']
    last_name = user[0]['last_name']
    if os.path.isdir("/home/jBloodless/mysite/tinder/toA_{0}_{1}_{2}".format(sex_str, first_name, last_name)) or os.path.isdir("/home/jBloodless/mysite/tinder/toM_{0}_{1}_{2}".format(sex_str, first_name, last_name)) or os.path.isdir("/home/jBloodless/mysite/tinder/toW_{0}_{1}_{2}".format(sex_str, first_name, last_name)):
        message = 'Ты вернулся! Хочешь поменять свой профиль или оставить все как было?'
        buttons = open("/home/jBloodless/mysite/tinderYesNo.json", "r", encoding="UTF-8").read()
    else:
        message = 'Обратить на себя внимание можно красивым лицом и метким словцом. Кинь нам свою фотку и расскажи немного о себе, а обо всем остальном я позабочусь.\nСначала отправь фотографию с описанием, через обычную кнопку с самолетиком. При этом клавиатура бота свернется - после отправки ее надо открыть и обязательно нажать Загрузить.  Ничего не перепутай!'
        buttons = open("/home/jBloodless/mysite/tinderInit.json", "r", encoding="UTF-8").read()
    return message, '', buttons

tinderCheck_command = command_system.Command()

tinderCheck_command.keys = ['Поехали!']
tinderCheck_command.description = 'internal tinder message'
tinderCheck_command.process = tinderCheck