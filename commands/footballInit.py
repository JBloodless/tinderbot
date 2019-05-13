import command_system
import vk

session = vk.Session()
api = vk.API(session, v=5.92)

def footballInit():
    message = 'Совсем скоро состоится серия футбольных матчей на коробке. Попробуй угадать победителя в каждом анонсированном матче. Угадавшие наибольшее количество матчей получат крутые призы от ОКДФ!\nИтак, первая пара — Профком против МКИ!'
    buttons = open("/home/jBloodless/mysite/football1.json", "r", encoding="UTF-8").read()
    return message, '', buttons

footballInit_command = command_system.Command()

footballInit_command.keys = ['legacy']
footballInit_command.description = 'голосование за футбол'
footballInit_command.process = footballInit
