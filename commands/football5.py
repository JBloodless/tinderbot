import command_system
import vk
from openpyxl import load_workbook
from flask_app import curr_user_id
from settings import token, s_token

session = vk.Session()
api = vk.API(session, v=5.92)

def football5():
    user_id = curr_user_id()
    user = api.users.get(user_ids=str(user_id), access_token = s_token)
    first_name = user[0]['first_name']
    last_name = user[0]['last_name']
    hist = api.messages.getHistory(peer_id = user_id, group_id=17379212, offset = 0, count = 1, access_token = token)
    vote = hist['items'][0]['text']
    wb = load_workbook('/home/jBloodless/mysite/commands/football.xlsx')
    data = (str(user_id), first_name, last_name, vote)
    sheet=wb.active
    sheet.append(data)
    wb.save('/home/jBloodless/mysite/commands/football.xlsx')
    message = 'Голос учтен!\n Первое межвузовское противостояние — ВШЭ и МФТИ!'
    buttons = open("/home/jBloodless/mysite/football6.json", "r", encoding="UTF-8").read()
    return message, '', buttons


football5_command = command_system.Command()

football5_command.keys = ['no5']
football5_command.description = 'голосование за футбол'
football5_command.process = football5
